"""
 *  NOTICE:
 *  This document contains information that is confidential and proprietary
 *  to Global Edge Software Limited. No part of this document may be
 *  reproduced in any form whatsoever without written prior approval by
 *  Global Edge Software Limited.
 *
 *  Global Edge Software Limited. reserve the right to revise this
 *  publication and make changes without obligation to notify any person of
 *  such revisions or changes.

File :Utils.py 
    All generic methods of endpoint like iperf,ping.., are defined
"""

import getpass
import logging
import subprocess
import os
import re
import sys
from time import gmtime, strftime, sleep
from robotremoteserver import RobotRemoteServer
import xmltodict
from subprocess import PIPE
import time
import commands
import socket
import json
import paramiko
from ftplib import FTP
import ftplib
import ast
import iptools

CONFIG_FILE = "../Config/StaConfig.xml"

with open(CONFIG_FILE) as fd:
    CONFIGHASH = xmltodict.parse(fd.read())
DEVICE = CONFIGHASH['ConfigInformation']['STA']


def sta_get_ip(interface):

    """the function to get the ip address of the station

    Args:
      data (str): None

    Returns:
      bool: True for success, False otherwise.
    """
    try:
        output = commands.getoutput("ifconfig " + interface)
        ip = re.search(r"(\d+\.){3}(\d+)", output, re.I)
        if ip:
            return ip.group()
        return False
    except Exception as err_msg:
        logging.info('error_messge' + str(err_msg))
        return False

def sta_set_ip(param):
    """ the function to set ip of the station

    Args:
        data (str): dictionary conatining ip

    Returns:
      bool: True for success, False otherwise.
    """
    try:
        if os.system("sudo ifconfig " + DEVICE['interface'] + " " + param['IP'] + " up"):
            return False
        return True
    except (IndexError, Exception) as error_message:
        logging.info(error_message)
        return False

def sta_ping(pinghashref):
    """the function to ping to check the initial connectivity

    Args:
      data (str): Dictionary containing ping parameters

    Returns:
      bool: True for success, False otherwise.
    """
    try:
        destinationip = pinghashref['DestinationIp']
        wifiduration = pinghashref['Wifi_Duration'] or "10"
        size = pinghashref['Size'] or "1500"
        interval = pinghashref['Interval'] or "1"
        mypingoutput = CONFIGHASH['ConfigInformation']['LogPath']['PingLog'] + "Pinglog_" \
        + strftime("%d%m%Y_%H_%M_%S", gmtime()) + ".txt"
        pingfailcnt = 0
        passcnt = 0
        errormsg = ""
        #command = "xterm -e 'ping -c " + wifiduration + " -s " \
        command = "ping -c " + wifiduration + " -s " \
        + size + " -i " + interval + " " + destinationip

        if 'Interface' in pinghashref:
            command += " -I %s " % pinghashref['Interface']
        if pinghashref.has_key('Qos'):
            command += " -Q " + pinghashref['Qos']
        #command += "| tee " + mypingoutput + "'"
        command += "| tee " + mypingoutput
        logging.info(command)
        result = subprocess.Popen(command, shell=True,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT)
        output, err = result.communicate()
        logging.info("output " + str(output) + " error " + str(err))
        with open(mypingoutput, 'r') as filehandler:
            data = ''
            for line in filehandler:
                data = data + line
                logging.info(line)
                if re.match(r"Request\s+timed\s+out", line):
                    pingfailcnt += 1
                    errormsg += line + "\n"
                elif re.match(r"Destination\s+host\s+unreachable", line):
                    pingfailcnt += 1
                    errormsg += line + "\n"
                elif re.search(r"bytes from", line):
                    passcnt += 1
                elif re.match(r"TTL\s+expired\s+in\s+transit", line):
                    pingfailcnt += 1
                    errormsg += line + "\n"
                elif re.match(r"ICMP\s+host\s+unreachable\s+from\s+gateway",
                              line):
                    pingfailcnt += 1
                    errormsg += line + "\n"
                elif re.match(r"no\s+reply\s+from\s+destination", line):
                    pingfailcnt += 1
                    errormsg += line + "\n"
                elif re.match(r"General\s+failure", line):
                    pingfailcnt += 1
                    errormsg += line + "\n"
                elif re.match(r"connect:\s+Network\s+is\s+unreachable",
                              line):
                    pingfailcnt += 1
                    errormsg += line + "\n"
        passpercentage = (passcnt * 100) / int(wifiduration)
        msg = str(passpercentage) + "#" + output
        if passpercentage >= 50:
            logging.info('1 ' + msg + "")
            return 'True' + data
        logging.info(msg)
        return False
    except (IndexError, Exception) as error_message:
        logging.info(error_message)
        return False

def sta_start_iperf(cmd):
    """the function start server and client

    Args:
      data (str): Iperf parameter in dictionay format

    Returns:
      bool: message and error messege, False otherwise.
    """
    try:
        wmm = {'AC_VO':' 0xe0', 'AC_VI':' 0xa0', 'AC_BE':' 0x00', 'AC_BK':' 0x21',}
        filename = CONFIGHASH['ConfigInformation']['LogPath']['IperfLog'] + \
                   cmd['IPERF_MODE'] + \
                   strftime("%Y-%m-%d_%H%M%S", gmtime()) + '.log'
        if cmd['PROTO'].upper() == 'UDP':
            if cmd['IPERF_MODE'].lower() == 'server':
                command = 'iperf -s -u '
            elif cmd['IPERF_MODE'].lower() == 'client':

                if cmd.has_key('TRANSMISSION_TYPE') and cmd['TRANSMISSION_TYPE'] == 'BIDI':
                    command = 'iperf -c ' + cmd['IP'] + ' -u -b ' + cmd.get(
                        'BANDWIDTH', \
                        CONFIGHASH['ConfigInformation']['iperf'][
                            'bandwidth']) + ' -d'
                else:
                    command = 'iperf -c ' + cmd['IP'] + ' -u -b ' + cmd.get(
                        'BANDWIDTH', CONFIGHASH['ConfigInformation']['iperf']['bandwidth'])
            else:
                return (False, 'Invalid Iperf Mode')
        elif cmd['PROTO'].upper() == 'TCP':
            if cmd['IPERF_MODE'].lower() == 'server':
                command = 'iperf -s '
            elif cmd['IPERF_MODE'].lower() == 'client':

                #if cmd['TRANSMISSION_TYPE'] == 'BIDI':
                if cmd.has_key('TRANSMISSION_TYPE') and cmd['TRANSMISSION_TYPE'] == 'BIDI':
                    command = 'iperf -c ' + cmd['IP'] + ' -w ' + cmd.get(
                        'WINDOW',
                        CONFIGHASH['ConfigInformation']['iperf']['window']) + ' -d'
                else:
                    command = 'iperf -c ' + cmd['IP'] + ' -w ' + cmd.get(
                        'WINDOW',
                        CONFIGHASH['ConfigInformation']['iperf']['window'])
            else:
                return (False, 'Invalid Iperf Mode')
        else:
            return (False, 'Invalid Iperf Proto')

        d = cmd.get('DURATION',
                    CONFIGHASH['ConfigInformation']['iperf'][
                        'duration'])
        if cmd.has_key('DURATION'):
            d = cmd['DURATION']
        command += ' -t ' + d
        if cmd['IPERF_MODE'].lower() == 'client':
            if cmd.has_key('wmm'):
                command += '-S ' + str(wmm[cmd['wmm']])
        p = cmd.get('PORT',
                    CONFIGHASH['ConfigInformation']['iperf'][
                        'iperfport'])
        if cmd.has_key('PORT'):
            p = cmd['PORT']
        command += ' -p ' + p

        command += ' -f ' + str(cmd.get('IPERF_OPTION', CONFIGHASH['ConfigInformation']['iperf']['format'])) \
                   + ' -i ' + str(cmd.get('TIME_INTERVAL', CONFIGHASH['ConfigInformation']['iperf']['interval'])) \
                   + ' | tee ' + filename
        logging.info('IPERF cmd ' + command)
        #command = "xterm -e '" + command + "'"
        subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
        sleep(5)
        if cmd['IPERF_MODE'].lower() == 'client':
            sleep(int(d))
        return str(True)+str({cmd['IPERF_MODE'].upper(): filename})
    except (IndexError, Exception) as error_message:
        logging.info('IPERF ERROR ' + str(error_message))
        logging.info('IPERF ERROR ' + str(sys.exc_info()))
        #print ('IPERF ERROR ' + str(sys.exc_info()))
        return False

def sta_get_throughput(cmd):
    """the function to get throughput value

    Args:
      data (str): Iperf parameter in dictionay format

    Returns:
      bool: status value, message and error messege, False otherwise.
    """
    print 'cmd : ', cmd
    try:
        tpt = []
        if cmd['SERVER']:
            with open(cmd['SERVER'], "r") as fh:
                data = fh.read()
                print 'File data : ', data

                streams = re.findall("\[\s+(\d*)\]", data)
                stream_nos = set(streams)
                #print stream_nos

            for no in stream_nos:
                print no
                re_x = '\[\s+'+no+'\].*'
                #print re_x
                stream = re.findall(re_x, data)
                stream = '\n'.join(stream)
                #print stream

                throughput_list = re.findall(
                    r'.*\s+0\.0\-\s*(\d+\.\d)+\s+sec.*\s+([\d+\.\d+]+)\s+'
                    r'([GMK](bits|bytes)/sec)', \
                    stream, re.MULTILINE)
                print throughput_list
                if not throughput_list:
                    print 'No data'
                    continue
                    # return (False,'Error in iperf traffic')
                if float(throughput_list[-1][0]) > float(throughput_list[0][0]):
                    tput = float(throughput_list[-1][1])
                    print tput
                else:
                    tput_list = re.findall(
                        r'^.*\s+\d+\.\d+\-\s+\d+\.\d+\s+sec.*\s+([\d+\.\d+]+)\s'
                        r'+[GMK]b.*/sec',
                        stream, re.MULTILINE)
                    if not tput_list:
                        print 'No tput'
                        continue
                        # return(False, 'Error in iperf traffic')
                    tput_sum = reduce(lambda x, y: float(x) + float(y),
                                      tput_list)
                    tput = tput_sum / len(tput_list)
                if re.match("Bytes", throughput_list[0][3], re.I):
                    tput = tput * 8
                if re.match("K", throughput_list[0][2]):
                    tpt.append(str(tput / 1000) + " Mbps")
                elif re.match("G", throughput_list[0][2]):
                    tpt.append(str(tput * 1000) + " Mbps")
                else:
                    tpt.append(str(tput) + " Mbps")
        #return *tpt if tpt else return False
        if tpt: return 'True' + str(tpt)
        return False
    except NameError:
        print sys.exc_info()
        return (False, 'iperf server file not found')
    except Exception, e:
        print 'Exception in iperf tput : ', e
        return False

def sta_enable_dhcp(interface=DEVICE['interface']):
    """to enable DHCP

    Args:
      data (str): None

    Returns:
      bool: True for success, False otherwise.
    """
    try:
        #os.system("killall dhclient " + DEVICE['interface'])
        #if os.system("dhclient " + DEVICE['interface'] + " &"):
        #    return False
        command = "ps -ef | grep \"dhclient " + interface + "\" | " \
                                                                      "cut -d' ' -f6"
        result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT)
        (output, err) = result.communicate()
        runningDhcpClient = len(output.split('\n'))-2
        print runningDhcpClient
        temp = 0
        while temp is not runningDhcpClient:
            print "--"+output.split('\n')[temp]
            os.system("kill -9 " + output.split('\n')[temp] + " &")
            temp = temp + 1
        os.system('dhclient -r %s' % interface)
        if os.system("dhclient " + interface + " &"):
            return False
        return True
    except (IndexError, Exception) as error_message:
        logging.info(error_message)
        return False

def stop_iperf():
    """function to kill the iperf process

    Args:
      data (str): None

    Returns:
      bool: True for success, False otherwise.
    """
    try:
        os.system("sudo killall -9 iperf")
        process = subprocess.Popen(["ps -e | grep iperf"], shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        (output, err) = process.communicate()
        logging.info("output " + str(output) + " error " + str(err))
        #pid = re.findall(r'(\d+\s)p', output)
        #os.system("kill -9 " + ''.join(pid))
        return True
    except (IndexError, Exception) as error_message:
        logging.info(error_message)
        return False

def do_ssh(host, user, pwd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(host, username=user, password=pwd)
        except:
            print sys.exc_info()[1]
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls')
        output = ssh_stdout.read()
        logging.info("output:"+str(output))
        error = ssh_stderr.read()
        if error != "":
            print "err:", error
            return False
        ssh.close()
        return output
    except (IndexError, Exception) as error_message:
        logging.info(error_message)
        return False


def do_ftp(ip, user, passwd, port=21):
    """ FTP fucntions """
    try:
        print ip, user, passwd, port
        ftp_obj = FTP()
        ftp_obj.connect(ip, port)
        ftp_obj.login(user, passwd)
        print ftp_obj.welcome
        print ftp_obj.nlst()
        print ftp_obj.dir()
        ftp_obj.close()
        return True
    except Exception, e:
        print 'Exception in do_ftp : %s' % e
        return False

def sta_add_route_gw(gateway_ip):
    """
     Adding the Route gateways
     Args: Gateway_ip
    """
    try:
        command = "sudo route add default gw " + gateway_ip
        os.system(command)
        return True
    except (Exception) as error_message:
        logging.info('Route Gateway ERROR ' + str(error_message))
        logging.info('Route Gateway Error ' + str(sys.exc_info()))
        return False

def sta_delete_route_gw(gateway_ip):
    """
     Deleting the Route gateways
     Args: Gateway_ip
    """
    try:
        command = "sudo route delete " + gateway_ip
        os.system(command)
    except (Exception) as error_message:
        logging.info('Route Gateway ERROR ' + str(error_message))
        logging.info('Route Gateway Error ' + str(sys.exc_info()))


def set_dhcp_interface(interface=None):
    """ Configures the /etc/default/isc-dhcp-server with provided  file interface
    Args:
      data (str): interface 

    Returns:
      bool: True for success, False otherwise.


   """
    f = '/etc/default/isc-dhcp-server'
    logging.info('Trying to edit /etc/network/isc-dhcp-server to configure DHCP')
    try:
        if not interface and dhcps_conf and 'interface' in dhcps_conf:
            interface = dhcps_conf['interface']
        data = ''
        print interface
        if not os.path.exists(f):
            with open(f, 'w') as fp:
                fp.write('INTERFACES="%s"' % interface)
        else:
            with open(f, 'r') as fp:
                data = fp.read()
            print data
            if not data:
                replace = 'INTERFACES="%s"' % interface
            else:
                replace = re.sub(r'INTERFACES="[^"]+"', 'INTERFACES="%s"' % interface, data)
            print '\n\n', replace
            if replace:
                with open(f, 'w') as fp:
                    fp.write(replace)
                return True
            return False
    except Exception, e:
        logging.info('Exception in configuring DHCP Interface : %s' % e)
        return False
    return True

def get_dhcp_config_dict(dhcps_conf=None):
    """ Creates dhcps_conf dictionary for DHCP Server configuration
    if it is None or any filed is missing this functions adds default value for it
    Args:
      data (str): dhcps_conf

    Returns:
      bool: True for success, False otherwise.
    """
    conf_file = "../../Controller/Config/TestBedManifest.xml"

    with open(conf_file) as fd:
      data = xmltodict.parse(fd.read())
    dhcp_data = CONFIGHASH['ConfigInformation']['DHCP_SERVER']

    if not dhcps_conf or dict != type(dhcps_conf):
      dhcps_conf = {}
    return dhcp_data.update(dhcps_conf)

def config_dhcp_server(dhcps_conf=None):

    """ Creates /etc/dhcp/dhcpd.conf from dhcps_conf 
    Args:
      data (str): dhcp_conf

    Returns:
      bool: True for success, False otherwise.

    """
    #dhcps_conf = get_dhcp_config_dict(dhcps_conf)
    dhcps_conf_contetnt = 'ddns-update-style none;\ndefault-lease-time %s;\nmax-lease-time %s;\noption routers %s;\noption broadcast-address %s;\noption domain-name "%s";\n'
    dhcps_conf_contetnt = dhcps_conf_contetnt % (dhcps_conf['d_lease_time'], dhcps_conf['max_lease_time'],
                                                 dhcps_conf['routers'], dhcps_conf['broadcast_addr'],
                                                 dhcps_conf['domain_name'])
    #dhcps_conf_contetnt += '\n'.join('option domain-name-servers %s;' % dns_addr for dns_addr in filter(None, dhcps_conf['dns'].split(',')))
    dhcps_conf_contetnt += '\noption domain-name-servers %s;'% (dhcps_conf['dns'])
    dhcps_conf_contetnt += '\nlog-facility local7;\n'
    dhcps_conf_contetnt += ''.join('\nsubnet %s netmask %s {\n\trange %s;\n}\n' % (e.split(':')[0], e.split(':')[1], e.split(':')[2].replace('-', ' ')) for e in filter(None, dhcps_conf['subnet'].split(';')))
    logging.info('Trying to Configure /etc/dhcp/dhcpd.conf with \n%s' % dhcps_conf_contetnt)
    try:
      # os.system('cp /etc/dhcp/dhcpd.conf /etc/dhcp/dhcpd_%s.conf' %int(time.time()))
        with open('/etc/dhcp/dhcpd.conf', 'w') as fp:
            fp.write(dhcps_conf_contetnt)
    except Exception, e:
        logging.info('Exception in configuring DHCPS : %s' % e)
        return False
    return True

def config_dhcp_nak_server(dhcps_conf=None):
    """ Creates /etc/dhcp/dhcpd.conf from dhcps_conf
     Args:
      data (str): dhcp_conf

    Returns:
      bool: True for success, False otherwise.
  
    """

    #dhcps_conf = get_dhcp_config_dict(dhcps_conf)
    dhcps_conf_contetnt = 'ddns-update-style none;\ndefault-lease-time %s;\nmax-lease-time %s;\noption routers %s;\noption broadcast-address %s;\noption domain-name "%s";\n'
    dhcps_conf_contetnt = dhcps_conf_contetnt % (dhcps_conf['d_lease_time'], dhcps_conf['max_lease_time'],
                                                 dhcps_conf['routers'], dhcps_conf['broadcast_addr'],
                                                 dhcps_conf['domain_name'])
    #dhcps_conf_contetnt += '\n'.join('option domain-name-servers %s;' % dns_addr for dns_addr in filter(None, dhcps_conf['dns'].split(',')))
    dhcps_conf_contetnt += '\noption domain-name-servers %s;'% (dhcps_conf['dns'])
    dhcps_conf_contetnt += '\nlog-facility local7;\n'
    dhcps_conf_contetnt += ''.join('\nsubnet %s netmask %s { \n\tpool{\n\t\trange %s;\n}\n' % (e.split(':')[0], e.split(':')[1], e.split(':')[2].replace('-', ' ')) for e in filter(None, dhcps_conf['dhcp_nak_pool1'].split(';')))
    dhcps_conf_contetnt += ''.join('\n\tpool{\n\t\trange %s;\n\t\t%s;\n\t}\n}' % (dhcps_conf['dhcp_nak_pool2'].replace('-', ' '),dhcps_conf['dhcp_deny']))
    logging.info('Trying to Configure /etc/dhcp/dhcpd.conf with \n%s' % dhcps_conf_contetnt)
    try:
      # os.system('cp /etc/dhcp/dhcpd.conf /etc/dhcp/dhcpd_%s.conf' %int(time.time()))
        with open('/etc/dhcp/dhcpd.conf', 'w') as fp:
            fp.write(dhcps_conf_contetnt)
    except Exception, e:
        logging.info('Exception in configuring DHCPS : %s' % e)
        return False
    return True


def configure_interface(interface_info):
    """ Configure a provided interface Using the provided ip addrs
    ex : interface_info = {'interface': 'eth0', 'ip': '172.168.10.1',
                           'bcast': '172.168.10.255', 'netmask': '255.255.255.0'}
    Args:
     data (str): interface_info

    Returns:
      bool: True for success, False otherwise.
    """
    # ifconfig eth0 192.168.1.102 netmask 255.255.255.0 broadcast 192.168.1.255
    result = False
    if 'ip' not in interface_info:
        return result
    try:
        cmd = 'ifconfig %s %s' % (interface_info['interface'], interface_info['ip'])
        if 'bcast' in interface_info:
            cmd += ' broadcast %s' % interface_info['bcast']
        if 'netmask' in interface_info:
            cmd += ' netmask %s' % interface_info['netmask']
        stop_interface(interface_info['interface'])
        logging.info('Command : %s' % cmd)
        if 0 == os.system(cmd):
            cmd += ' up'
            logging.info('Command : %s' % cmd)
            if 0 == os.system(cmd):
                if 'gateway' in interface_info:
                    cmd = 'route add default gw %s' % interface_info['gateway']
                    if os.system(cmd):
                        return False
                if 'dns' in interface_info:
                    cmd = 'echo "nameserver %s" > /etc/resolv.conf' % interface_info['dns']
                    if os.system(cmd):
                        return False
                result = True
    except Exception, e:
        logging.info('Failed to Configure interface\n%s' % e)
    return result

def get_interface_info(interface):
    """ Returns ifconfig command output on interface """
    output = ''
    info = {'interface': interface}
    try:
        output = commands.getoutput('ifconfig %s' % interface)
    except Exception, e:
        logging.info('Failed to get interface info\n%s' % e)
    if output:
        if 'mac' in output:
            info['HWaddr'] = re.search(r'HWaddr\s+(.*)', output).group(1).strip()
        if 'inet addr:' in output:
            info['ip'] = re.search(r'inet addr:([^\s]+)', output).group(1).strip()
        if 'Mask:' in output:
            info['netmask'] = re.search(r'Mask:([^\s]+)', output).group(1).strip()
        if 'Bcast:' in output:
            info['bcast'] = re.search(r'Bcast:([^\s]+)', output).group(1).strip()
        if 'Link encap:' in output:
            info['type'] = re.search(r'Link encap:([^\s]+)', output).group(1).strip()
    return output, info

def start_interface(interface):
    """ Provided interface will be started using ifconfig iface up """
    result = False
    try:
        if 0 == os.system('ifconfig %s up' % interface):
            result = True
    except Exception, e:
        logging.info('Failed to Start interface\n%s' % e)
    return result

def stop_interface(interface):
    """ Provided interface will be stopped using ifconfig iface up """
    result = False
    try:
        if 0 == os.system('ifconfig %s down' % interface):
            result = True
    except Exception, e:
        logging.info('Failed to stop interface\n%s' % e)
    return result

def get_interface_ip():
    """ Returns the IP addrs of provided interface """
    ip = ''
    data, info = GetDhcpInterfaceInfo()
    if 'ip' in info:
        ip = info['ip']
    elif 'inet addr:' in str(data).lower():
        try:
            ip = re.search(r'inet addr:([^\s]+)', output, re.I).group(1).strip()
        except Exception, e:
            logging.info('Failed to fetch IP address from data : %s' % data)
    return ip

def ctrller_dhcp_server_start(retry=1):
    """This function starts the DHCP Server in controller machine

    Returns:
      bool: retVal. 1 for success, 0 otherwise.
    """
    if ctrller_dhcp_server_get_status() == 'running':
        return 1
    cmd = '/etc/init.d/isc-dhcp-server start'
    logging.info('\nCmd : %s' %cmd)
    try:
        retry = abs(int(retry))
    except:
        retry = 1
    while retry >= 0:
        out = commands.getoutput(cmd)
        if '...done.' in out or 'start/running,' in out:
            return 1
        retry -= 1
    return 0

def ctrller_dhcp_server_stop():
    """This function stops the DHCP Server in controller machine

    Returns:
      bool: retVal. 1 for success, 0 otherwise.
    """
    if ctrller_dhcp_server_get_status() == 'not running':
        return 1
    cmd = '/etc/init.d/isc-dhcp-server stop'
    logging.info('\nCmd : %s' %cmd)
    out = commands.getoutput(cmd)
    if '...done.' in out or 'stop/waiting' in out:
        return 1
    return 0

def ctrller_dhcp_server_restart():
    """This function restarts the DHCP Server in controller machine

    Returns:
      bool: retVal. 1 for success, 0 otherwise.
    """
    cmd = '/etc/init.d/isc-dhcp-server restart'
    logging.info('\nCmd : %s' %cmd)
    out = commands.getoutput(cmd)
    if '...done.' in out or 'start/running,' in out:
        return 1
    return 0

def ctrller_dhcp_server_get_status():
    """This function returns the DHCP Server status in controller machine

    Returns:
      bool: retVal. Status of the DHCP server
    """
    status = 'not running'
    cmd = '/etc/init.d/isc-dhcp-server status'
    logging.info('\nCmd : %s' %cmd)
    proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = proc.communicate()[0]
    if 'Status of ISC DHCP server: dhcpd is ' in out:
        try:
            status = out[36:].strip(' .\n')
        except Exception, e:
            logging.info('Exception in getting DHCP Server status : %s' % e)
    elif '/running,' in out or 'active(running)' in out:
        status = 'running'
    elif 'stop/waiting':
        status = 'not running'
    return status

def get_partial_ip(ip):
    return '.'.join(str(ip).split(':')[0].split('.')[:-1])

def add_gateway_in_route_table(wan_ip):
    """
    Takes default gateway
    Returns True if gateway add otherwise False
    """
    cmd = 'sudo route add default gw ' + wan_ip
    res = os.system(cmd)
    logging.info('add gateway in route cmd : %s' % cmd)
    if res == 0:
        return True 
    else:
        return False

def delete_gateway_in_route_table(wan_ip):
    """
    Delete default gateway
    Returns True if gateway delete otherwise False
    """
    cmd = 'sudo route delete default gw ' + wan_ip
    res = os.system(cmd)
    logging.info('delete gateway in route cmd : %s' % cmd)
    if res == 0:
        return True
    else:
        return False

def gatway_validation(wan_ip):
    """
    # returns True if the Gate way is added else False
    """
    data = commands.getoutput('route -n')
    match = re.search(wan_ip, data)
    if match:
        return True
    else:
        return False

def split_ms_dns(msdns):
    return str(msdns).split(',')[0]

def set_secrets(username, password, secret_file='/etc/ppp/chap-secrets'):
    """ Configures the /etc/ppp/chap-secrets file with provided interface """
    logging.info('Trying to edit %s to configure PPPoE Server' % secret_file)
    try:
        content = '"{username}" * "{password}" *\n'.format(username=username, password=password)
        with open(secret_file, 'w') as fp:
            fp.write(content)
    except Exception, e:
        logging.info('Exception in configuring PPPoE : %s' % e)
        return False
    return True

def config_pppoe_server(PPPoE_conf):
    """ Creates /etc/ppp/pppoe-server-options from PPPoE_conf """


    PPPoE_conf_contetnt = '%s\nlcp-echo-interval %s\nlcp-echo-failure %s\n' % (PPPoE_conf['method'], PPPoE_conf['echo-interval'], PPPoE_conf['echo-failure'])
    PPPoE_conf_contetnt += '\n'.join('ms-dns %s' % dns_addr for dns_addr in filter(None, PPPoE_conf['ms-dns'].split(',')))
    PPPoE_conf_contetnt += '\nnetmask %s\n%s\n%s\n%s\n' % (PPPoE_conf['netmask'], PPPoE_conf['route'], PPPoE_conf['noip'], PPPoE_conf['peerdns'])
    try:
        with open('/etc/ppp/pppoe-server-options', 'w') as fp:
            fp.write(PPPoE_conf_contetnt)
            print '/etc/ppp/pppoe-server-options PPPoE_conf_contetnt : ', PPPoE_conf_contetnt
    except Exception, e:
        logging.info('Exception in configuring DHCPS : %s' % e)
        return False
    return True

def kill_all_pppoe_server():
    """
    Args: None

    Returns:
      bool: True or False otherwise.
    """
    output = commands.getoutput('ps -aux | grep pppoe-server')
    try:
        for line in filter(None, output.split('\n')):
            if ' grep ' not in line and ' pppoe-server ':
                pid = filter(None, line.split(' '))[1]
                cmd = 'kill -9 %s' % pid
                logging.info('\n\nCMD : %s' % cmd)
                os.system(cmd)
    except Exception, e:
        logging.info('Failed kill pppoe process with pid %s\n%s' % (pid, e))
        return False
    return True

def pppoe_set_server_ip_range(ip_range='10.0.0.100-200'):
    """
    Args:

    Returns:
      bool: True or False otherwise.
    """
    cmd = 'echo "%s" > /etc/ppp/allip' % ip_range
    if os.system(cmd):
        logging.info('Failed to configure PPPoE IP Range')
        return False
    logging.info('Configured PPPoE IP Range to %s' % ip_range)
    return True

def pppoe_start_server(interface, server_ip='10.0.0.50'):
    cmd = 'sudo apt-get install pppoe'
    if os.system(cmd):
        logging.info('Installing PPPoE Server')
    cmd = 'pppoe-server isp -L %s -p /etc/ppp/allip -I %s' % (server_ip, interface)
    if os.system(cmd):
        logging.info('Failed to Start PPPoE Server')
        return False
    logging.info('PPPoE Server started')
    return True

def enable_ip_forward():
    """ The Function to enable the ip forwording
    Args: None
    Returns:
      bool: True or False otherwise.
    """
    cmd = 'echo 1 > /proc/sys/net/ipv4/ip_forward'
    if os.system(cmd):
        logging.info('Failed to Enable IP Forward')
        return False
    logging.info('IP Forward Enabled')
    return True

def nat_post_routing(pppoe_ip):
    """ Function Add ip tables nat rule to wan pc
    Args:

    Returns:
      bool: True or False otherwise.
    """

    mask = iptools.ipv4.netmask2prefix(pppoe_ip['netmask'])
    ip = iptools.ipv4.cidr2block(pppoe_ip['pppoeserver'] + "/" + str(mask))[0]
    print ip
    cmd = 'iptables -t nat -A POSTROUTING -s %s/%s -o %s -j MASQUERADE'  % (ip,mask,pppoe_ip['interface'])
    if os.system(cmd):
        logging.info('Failed to Enable Post Routing')
        return False
    logging.info('Enabled Post Routing')
    return True

def nat_delete_post_routing(pppoe_ip):
    """ Function deleted ip tables nat rule from wan pc
    Args: pppoe_ip

    Returns:
      bool: True or False otherwise.
    """
    mask = iptools.ipv4.netmask2prefix(pppoe_ip['netmask'])
    ip = iptools.ipv4.cidr2block(pppoe_ip['pppoeserver'] + "/" + str(mask))[0]
    cmd = 'iptables -t nat -D POSTROUTING -s %s/%s -o %s -j MASQUERADE'  % (ip,mask,pppoe_ip['interface'])
    if os.system(cmd):
        logging.info('Failed to Remove Post Routing')
        return False
    logging.info('Removed Post Routing')
    return True

def sta_start_iperf_scenario(cmd):
    """The function start server and client

    Args:
      data (str): Iperf parameter in dictionay format

    Returns:
      bool: message and error messege, False otherwise.
    """
    try:
        filename = CONFIGHASH['ConfigInformation']['LogPath']['IperfLog'] + \
                   cmd['IPERF_MODE'] + \
                   strftime("%Y-%m-%d_%H%M%S", gmtime()) + '.log'
        if cmd['PROTO'].upper() == 'UDP':
            if cmd['IPERF_MODE'].lower() == 'server':
                command = 'iperf -s -u '
            elif cmd['IPERF_MODE'].lower() == 'client':

                if cmd.has_key('TRANSMISSION_TYPE') and cmd['TRANSMISSION_TYPE'] == 'BIDI':
                    command = 'iperf -c ' + cmd['IP'] + ' -u -b ' + cmd.get(
                        'BANDWIDTH', \
                        CONFIGHASH['ConfigInformation']['iperf'][
                            'bandwidth']) + ' -d'
                else:
                    command = 'iperf -c ' + cmd['IP'] + ' -u -b ' + cmd.get(
                        'BANDWIDTH', CONFIGHASH['ConfigInformation']['iperf']['bandwidth'])
            else:
                return (False, 'Invalid Iperf Mode')
        elif cmd['PROTO'].upper() == 'TCP':
            if cmd['IPERF_MODE'].lower() == 'server':
                command = 'iperf -s '
            elif cmd['IPERF_MODE'].lower() == 'client':

                if cmd.has_key('TRANSMISSION_TYPE') and cmd['TRANSMISSION_TYPE'] == 'BIDI':
                    command = 'iperf -c ' + cmd['IP'] + ' -w ' + cmd.get(
                        'WINDOW',
                        CONFIGHASH['ConfigInformation']['iperf']['window']) + ' -d'
                else:
                    command = 'iperf -c ' + cmd['IP'] + ' -w ' + cmd.get(
                        'WINDOW',
                        CONFIGHASH['ConfigInformation']['iperf']['window'])
            else:
                return (False, 'Invalid Iperf Mode')
        else:
            return (False, 'Invalid Iperf Proto')

        d = cmd.get('DURATION',
                    CONFIGHASH['ConfigInformation']['iperf'][
                        'duration'])
        if cmd.has_key('DURATION'):
            d = cmd['DURATION']
        command += ' -t ' + d

        p = cmd.get('PORT',
                    CONFIGHASH['ConfigInformation']['iperf'][
                        'iperfport'])
        if cmd.has_key('PORT'):
            p = cmd['PORT']
        command += ' -p ' + p

        command += ' -f ' + str(cmd.get('IPERF_OPTION',
                                      CONFIGHASH['ConfigInformation'][
                                          'iperf']['format'])) \
                   + ' -i ' + str(cmd.get('TIME_INTERVAL',
                                      CONFIGHASH['ConfigInformation'][
                                          'iperf']['interval'])) \
                   + ' | tee ' + filename
        logging.info('IPERF cmd ' + command)
        #command = "xterm -e '" + command + "'"
        subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
        sleep(5)
        #if cmd['IPERF_MODE'].lower() == 'client':
            #sleep(int(cmd.get('DURATION', CONFIGHASH['ConfigInformation']['iperf']['duration'])))
             #sleep(int(d))
        return str(True)+str({cmd['IPERF_MODE'].upper(): filename})
    except (IndexError, Exception) as error_message:
        logging.info('IPERF ERROR ' + str(error_message))
        logging.info('IPERF ERROR ' + str(sys.exc_info()))
        #print ('IPERF ERROR ' + str(sys.exc_info()))
        return False

def wait_untill_sta_get_ip(interface, timeout=30):
    """ Wait for a STA to get IP on provided interface for given timeout """
    try:
        timeout = int(timeout)
    except Exception, e:
        timeout = 30
    ip = None
    interface = str(interface)
    if (interface + ' ') in commands.getoutput('ifconfig -a'):
        while(timeout > 0):
            ip = sta_get_ip(interface)
            if ip:
                break
            timeout -= 2
            time.sleep(2)
    return ip
def sta_dig(dig_server, dig_type="A"):
    """The function execute dig with type or class in client host

    Args(str):
                  dig_server(website name)
                  dig_type( either type or class )

    Returns:
      bool: message and error messege, False otherwise."""
    try:
        dig_stat={}	
    	command = "dig" + " " +  str(dig_server) + " " +  str(dig_type)
        print command
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        result = process.communicate()
        result = result[0].replace('\n',":")
        if "*** Can't find " + dig_server in result:
            dig_stat['status'] = False
            return json.dumps(dig_stat)
        else:
            dig_stat['status'] = True
            dig_stat['output'] = result.replace("\t", " ")
            return json.dumps(dig_stat)
    except Exception as key:
        logging.info(key)
        dig_stat['status'] = False
        return json.dumps(dig_stat)


def sta_nslookup_type(nslookup_server, nslookup_type="A"):
    """The function execute nslookup with type in client host

    Args:
      data (str): nslookup_server(website name),nslookup_type(type like A or MX etc...)
    Returns:
      bool: message and error messege, False otherwise.
    """
    
    try:
	lookup_stat = {'status':False, 'output':None}
        command = "nslookup -type=" + str(nslookup_type) + " " +  str(nslookup_server)
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        result = process.communicate()
        result = result[0].replace('\n'," ")
        if "*** Can't find " + nslookup_server in result:
            #return json.dumps(lookup_stat)
            return lookup_stat
        else:
            lookup_stat['status'] = True
            lookup_stat['output'] = result
            lookup_stat['output'] = result.replace("\t", " ")
            return json.dumps(lookup_stat)
            #return lookup_stat
    except Exception as key:
        logging.info(key)
        return json.dumps(lookup_stat)

def sta_nslookup_class(nslookup_server, nslookup_class="IN"):
    """The function execute nslookup with class in client host

    Args:
      data (str): nslookup_server(website name), nslookup_class(class like IN)

    Returns:
      bool: message and error messege, False otherwise."""
    
    try:
	lookup_stat = {}
        command = "nslookup -class=" + str(nslookup_class) + " " +  str(nslookup_server)
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        result = process.communicate()
     
        result = result[0].replace('\n',":")
        if "*** Can't find " + nslookup_server in result:
            lookup_stat['status'] = False
            lookup_stat['output'] = result.replace("\t", " ")
            return json.dumps(lookup_stat)
        else:
            lookup_stat['status'] = True
            return json.dumps(lookup_stat)
    except Exception as key:
        logging.info(key)
	lookup_stat['status'] = False
        return json.dumps(lookup_stat)

def sta_clear_dns_cache():
    """The function clear DNS cache in client host

    Args:  no args

    Returns:
      bool: message and error messege, False otherwise."""
    try:
        result = os.system('/etc/init.d/nscd restart')
	if result == 0:
	    return True
	else:
	    return False
    except Exception as key:
        logging.info(key)
	return False


def sta_conf_reslove_conf ( nameserver):
    """The function configure reslove.conf file with provide nameserver IP

    Args(str): nameserver (IP address)
     
    Returns:
      bool: message and error messege, False otherwise."""
    
    try:
        with open('/etc/resolv.conf', 'w') as fp:
            fp.write( 'nameserver %s' %nameserver )
            return True
    except Exception as key:
        logging.info( key )
        return False



#s=sta_nslookup_type('google.com','CNAME')
#print s
#get_key = sta_get_field('mail exchanger',s['output'])
#print(get_key)
#print do_ssh('172.16.6.102', 'gtest', 'g@ssw0rd')
#print do_ssh('192.168.0.5', 'gtest', 'g@ssw0rd')
#print do_ssh('127.0.0.1', 'ganesh', 'p@ssw0rd')

#if __name__ == '__main__':
#  PPPoE_conf = CONFIGHASH['ConfigInformation']['pppoe_configuration']
#  config_pppoe_server(PPPoE_conf)
#  set_secrets(PPPoE_conf['username'], PPPoE_conf['password'])
#  pppoe_set_server_ip_range()
#  kill_all_pppoe_server()
#  pppoe_start_server(PPPoE_conf['wan_interface'], PPPoE_conf['pppoeserver'])
#  enable_ip_forward()
#  nat_post_routing(PPPoE_conf['internet_interface'])

  # Gotoechoshell reboot
#  configure_interface({'interface': PPPoE_conf['wan_interface'], 'ip': PPPoE_conf['pppoeserver'], 'netmask': PPPoE_conf['pppoenetmask'],
#                      'gateway': PPPoE_conf['pppoegateway'], 'dns': '172.16.2.31'})
#  print get_interface_info(PPPoE_conf['wan_interface'])


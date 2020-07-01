#compile,filterall,search,match


import os
import commands
import re
'''
cmd = commands.getoutput("ifconfig eth0")
print cmd
#cmd = 'HWaddr 14:91:82:3b:97:db' 
#cmd1 = re.search(r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})',cmd)
#ccmd1 = re.search(r'([0-9A-Fa-f::]{4}){5}([0-9A-Fa-f/\d+]{4})',cmd)
cmd1 = re.search(r'(\d+\.){3}(\d+)',cmd)
print cmd1.group()
'''

output = commands.getoutput("ifconfig wlp3s0")
print output
ipv6 = re.search(r'(\w+\.){3}(\w+)',output)
#ipv6 = re.findall(r'\w+::\w+:\w+:\w+:\d+',output)
print (ipv6.group())

ipv6 = re.search(r'\w+<\w+>',output)
print ipv6.group()


#\W
output = re.search('\W+','1@#$%')
print output.group()
output = re.match('\W+','@#$%')
print output.group()

output = output.splitlines()
print output

#\S
output = re.search(r'\S',"abcdsd")
print output


#\s
output = re.search(r'\s',"abc dsd")
print output

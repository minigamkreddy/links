import commands
import re
import os
def sta_get_ip():

    """the function to get the ip address of the station

    Args:
      data (str): None

    Returns:
      bool: True for success, False otherwise.
    """
    value = (1,2,3,4)
    value = list(value)
    #value = tuple(vlaue)
    value[0] = 5
    print value
    i = os.system("ifconfig")
    print i
    output = commands.getoutput("ifconfig wlp3s0")
    ip = re.search(r"(\d+\.){3}(\d+)", output, re.I)
    print ip
    print type(ip.group())
    print ip.group(1)


sta_get_ip()

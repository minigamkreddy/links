import commands
import re
cmd = commands.getoutput("ifconfig wlp3s0")
print cmd
match = re.search(r'(\d+\.){3}(\d+)',cmd,re.I)
print match.group(0)

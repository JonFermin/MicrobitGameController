#!/usr/bin/python
import subprocess, sys
## command to run - tcp only ##
cmd = "python3 controller.py"
 
## run it ##
print "here4"
p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
 
## But do not wait till netstat finish, start displaying output immediately ##
while True:
    out = p.stderr.read(1)
    print "here"
    if out == '' and p.poll() != None:
        break
    if out != '':
    	blah = sys.stdout.replace("/wek/", "")
        print "here2"
        # sys.stdout.flush()
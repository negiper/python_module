#!/usr/bin/python

import pexpect
import sys

child = pexpect.spawn('ftp 172.16.2.55')
child.expect('Name.*:')
child.sendline('wx')
child.expect('Password:')
child.sendline('wx123')
child.expect('ftp>')
child.sendline('ls')
child.expect('ftp>')
sys.stdout.write(child.before)
sys.stdout.write(child.after)

child.interact()

child.sendline('bye')
child.close()
import sys
from subprocess import run
import os

filename, line_number, pwd = sys.argv[1:]

pycharm_path = "/Applications/PyCharm.app/Contents/MacOS/pycharm"

# strip quotes before and after file name
filename = filename.strip(':"\'')

# absolute path
filename = os.path.join(pwd, filename)

# Construct line number
linenumber = "--line %s" % line_number

# Two caveats here:
# 1. This form doesn't work but a pure string does work:
#    >>> run([pycharm_path, linenumber, filename])
# 2. `shell=True` is required. Otherwise, it'll confuse the pycharm
#    command which is a thin wrapper.
cmd = "%s %s %s" % (pycharm_path, linenumber, filename)
#fp = open('/tmp/script.log', 'w')
#fp.writelines([cmd])
#fp.close()
#print(cmd)

# open
run([cmd], shell=True)
run(["osascript", "-e", 'tell application "PyCharm" to activate'])

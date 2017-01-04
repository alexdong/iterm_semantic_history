import sys
from subprocess import run
import os

pycharm_path = "/Applications/PyCharm.app/Contents/MacOS/pycharm"

"""
There is no good way for this script to report any errors.
Whenever something isn't quite right, it just quietly crashed.
Leaving nothing for us to debug. So the debug strategy here
is quite arcane. We manually append log messages to a file.

To help debugging, run the following command in another window.

    tail -f /tmp/script.log

"""

def debug(s):
    fp = open('/tmp/script.log', 'w+')
    fp.writelines([s + os.linesep])
    fp.close()

filename, line_number, pwd = sys.argv[1:]

# strip quotes, backslash, () and [] before and after file name
filename = filename.strip(':"\\\'').strip('[(').strip('])')

# If filename starts with webpack:///
if filename.startswith('http:') or filename.startswith('https:'):
    run(["open " + filename])


if filename.startswith('webpack:///'):
    filename = filename[len('webpack:///'):]

# If the filename is like "file.js:line:column", parse out the line number
if len(filename.split(':')) > 1:
    parts = filename.split(':')
    filename = parts[0]
    if parts[1].isdigit():
        line_number = parts[1]

#debug(filename)

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
#debug(cmd)

# open
run([cmd], shell=True)
run(["osascript", "-e", 'tell application "PyCharm" to activate'])

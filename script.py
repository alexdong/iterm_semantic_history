import sys
from subprocess import call
import re
import os

filename, line_number, text_before_click, text_after_click, pwd = sys.argv[1:]

def debug(s):
    call(["osascript", "-e", 'tell app "Finder" to display dialog "%s"' % s.replace("'", 'SQUOTE').replace('"', 'DQUOTE')])

# handle URL paths
if filename.startswith('http:') or filename.startswith('https:'):
    call(["open", filename])

# handle file paths
else:
    pycharm_path = "/usr/local/bin/charm"

    # strip quotes before and after file name
    filename = filename.strip(':"\'')

    # handle flake8 paths -- with an extra ##: on the end
    if re.search(r'\d+\:\d+:$', filename):
        filename = filename.rsplit(':', 2)[0]

    # remove first two directories from vagrant paths
    if filename.startswith('/vagrant/'):
        filename = filename.split('/', 3)[-1]

    # absolute path
    filename = os.path.join(pwd, filename)

    # open
    call([pycharm_path, filename])
    call(["osascript", "-e", 'tell application "PyCharm" to activate'])
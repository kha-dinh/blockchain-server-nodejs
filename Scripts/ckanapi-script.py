#!"c:\users\kha\google drive\shared\projects\blockchain-server\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'ckanapi==4.3','console_scripts','ckanapi'
__requires__ = 'ckanapi==4.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('ckanapi==4.3', 'console_scripts', 'ckanapi')()
    )

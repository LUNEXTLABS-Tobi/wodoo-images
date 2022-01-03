#!/usr/bin/env python3
import time
import shutil
import tempfile
import os
import sys
import subprocess
from wodoo.module_tools import Module
from wodoo.odoo_config import get_odoo_addons_paths
from pathlib import Path
from tools import exec_odoo
if len(sys.argv) == 1:
    print("Usage: import_i18n de_DE pofilepath")
    sys.exit(-1)
if len(sys.argv) == 2:
    print("Language Code and/or Path missing!")
    print("")
    print("Please provide the path relative to customs e.g. modules/mod1/i18n/de.po")
    sys.exit(-1)

LANG = sys.argv[1]
FILEPATH = sys.argv[2]

addon_paths = get_odoo_addons_paths()
for path in addon_paths:
    if (path / FILEPATH).exists():
        filepath = path / FILEPATH
        break
else:
    path = Path("/opt/src") / FILEPATH
    if path.exists():
        filepath = path
    else:
        print(f"File not found: {FILEPATH}")
        time.sleep(3)
        sys.exit(-1)
print(f"Importing lang file {FILEPATH}")

exec_odoo(
    'config_i18n',
    '--stop-after-init',
    '-l', LANG,
    '--i18n-import={}'.format(filepath),
    '--i18n-overwrite',
)

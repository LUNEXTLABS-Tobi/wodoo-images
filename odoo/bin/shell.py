#!/usr/bin/env python3
import os
import sys
import subprocess
from wodoo.module_tools import Module
from wodoo.odoo_config import customs_dir
from wodoo.odoo_config import current_version
from pathlib import Path
from tools import exec_odoo
from tools import prepare_run

prepare_run()

os.environ['PYTHONBREAKPOINT'] = 'pudb.set_trace'

# make path relative to links, so that test is recognized by odoo
cmd = [
    '--stop-after-init',
]
if current_version() >= 11.0:
    cmd += ["--shell-interface=ipython"]

if len(sys.argv) > 1:
    odoo_cmd = sys.argv[1]
else:
    odoo_cmd = ""

os.environ["ODOO_SHELL_CMD"] = odoo_cmd
stdin = None
if odoo_cmd:
    stdin = odoo_cmd # 'echo "$ODOO_SHELL_CMD"'

exec_odoo(
    "config_shell",
    *cmd,
    odoo_shell=True,
    stdin=stdin,
    dokill=False,
)

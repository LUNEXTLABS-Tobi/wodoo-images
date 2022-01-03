import re
import base64
import click
import yaml

def after_compose(config, settings, yml, globals):
    dirs = config.dirs

    # make dummy history file for pgcli
    file = dirs['run'] / 'pgcli_history'
    if not file.exists():
        file.write_text("")

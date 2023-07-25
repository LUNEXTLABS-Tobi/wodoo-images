#!/bin/bash
set -e

function make_entrypoint_with_params() {
python3 <<EOF
print("Version 1.0")
import os
with open('/config') as file:
    conf = file.read().splitlines()
conf += os.getenv('POSTGRES_CONFIG').split(",")
conf = list(filter(lambda x: bool((x or '').strip()) and not (x or '').strip().startswith("#"), conf))

print("Applying configuration:\n" + '\n'.join(conf))

conf = list(map(lambda x: f"-c {x}", conf))

with open('/start.sh', 'w') as f:
    f.write('/usr/local/bin/docker-entrypoint.sh postgres ' + ' '.join(conf))

EOF
}
make_entrypoint_with_params

if [[ "$1" == "postgres" ]]; then
    exec gosu postgres bash /start.sh
else
    exec gosu postgres "$@"
fi

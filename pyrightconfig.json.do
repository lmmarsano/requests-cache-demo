#!/usr/bin/env bash
set -e
redo-always
VENV_PATH=$(poetry env info -p) || {
	exec poetry install >&2
	VENV_PATH=$(poetry env info -p)
}
cat <<EOF >$3
{
	"venvPath": "${VENV_PATH%/*}",
	"venv": "${VENV_PATH##*/}"
}
EOF
exec redo-stamp <$3

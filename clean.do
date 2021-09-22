#!/usr/bin/env bash
set -e
: ${ARGS:=-f}
exec >&2 git clean $ARGS -dxe .redo -e .save -e local-setup -e .python-version -e \*.egginfo -e .env -e pyrightconfig.json

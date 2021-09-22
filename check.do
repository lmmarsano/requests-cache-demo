#!/usr/bin/env bash
set -e
redo-ifchange dependencies
exec poetry run pytest $PYTEST_ARGS >&2

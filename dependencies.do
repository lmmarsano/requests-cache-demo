#!/usr/bin/env bash
set -e
redo-ifchange pyrightconfig.json pyproject.toml
exec poetry install >&2

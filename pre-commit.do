#!/usr/bin/env bash
set -e
exec >&2
redo-ifchange git .pre-commit-config.yaml dependencies
exec poetry run pre-commit install

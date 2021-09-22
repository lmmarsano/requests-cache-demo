#!/usr/bin/env bash
set -e
exec redo-ifchange pyrightconfig.json pre-commit dependencies

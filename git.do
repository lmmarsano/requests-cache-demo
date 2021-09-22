#!/usr/bin/env bash
set -e
[[ -d .git ]] || exec git init >&2

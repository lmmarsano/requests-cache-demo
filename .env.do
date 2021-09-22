#!/usr/bin/env bash
set -e
if [[ ! -e $1 ]]
then : >"$3"
fi

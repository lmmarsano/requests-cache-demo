#!/usr/bin/env bash
set -e
{
	echo README.md
	find src \( -name \*.py -o -name \*.pyi \)
} | xargs redo-ifchange
exec poetry build $BUILD_ARGS >&2

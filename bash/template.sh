#!/bin/bash
# Author: Thomas Schmidt
# Last edit:

# Variables
LOG="/var/log/temp.log"
TIME=$(date "+%Y-%m-%dT%H:%M:%S")

# Print usage function
printUsage() {
cat << ENDHERE
Usage: $(basename "$0") [ARGUMENTS]
This is a description.

Arguments:
  -h, --help	print usage
ENDHERE
}

# Input control variant 1
#if [[ $# -ne 0 || $@ == "--help" || $@ == "-h" ]]; then printUsage; exit 1; fi

# Input control variant 2
# ${1+string} expands to 'string' as long as $1 is set (may be empty string)
while [[ "${1+defined}" ]]; do
 case "$1" in
  -h | --help) printUsage; exit 1;;
#  -a | --arg) ARG=$2; shift 2;;
  --) break;;
  -*) echo "Unknown option: $1" >&2; printUsage; exit 1;;
  *) break;;
 esac
done

# Start of script

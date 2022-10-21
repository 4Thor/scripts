#!/bin/sh
# Author: Thomas Schmidt
# Last edit: 22.12.2020

# Variables
DESCRIPTION="Creates a new script with a description header"
USAGE="createScript.sh SCRIPTNAME"
TEMPLATE="/beit/thomas/scripts/template.sh"

# Print usage
if [[ $# -lt 1 || $@ == "--help" || $@ == "-h" ]]; then echo -e "$DESCRIPTION\n\nUsage: $USAGE\n"; exit 1; fi

# Start of script
for SCRIPTNAME in "$@"; do
 # Check if file exists
 if [[ -f "$SCRIPTNAME" ]]; then
  echo "$SCRIPTNAME already exists, aborting.."
  exit 2
 fi
 # Copy template and insert date
 cp "$TEMPLATE" "$SCRIPTNAME" 
 sed -i "/Last edit:/s/\$/ $(date +%d.%m.%Y)/" "$SCRIPTNAME"
done

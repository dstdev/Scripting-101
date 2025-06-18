#!/bin/bash

# bash_looper1.sh
# 21 May 2025 | datainscience.com 
# 
# This file is the bare minimum for a readable and maintainable shell script 
#  The key elements are:
#     1) A usage/help function 
#     2) Command line arguments - miniumon of "-h" for "help/usage"
#     3) Live/Dry-run flag 
#         - I like the default to be non-live so I can review the commnads

# Usage output  
function usage(){
    echo "bash_tempalte.sh - basic bash script boilerplate"
    echo "  Options: "
    echo "      -h : print this message"
    echo "      -l : 'live-run mode' - evaluate and run commands.  "
    echo "            default is 'dry-run mode' comands are only printed" 
    echo "      -c : command loop count - run the command this many times" 
    echo "     " 
    exit
}

# Set our default values 
live_mode=0 
count=0 

# Loop over input options 
# getopts "hlc:" means:
#  h - define "-h" flag with no options 
#  l - define "-l" flag with no options 
#  c: - ( note the ":" ) define "-c" flag with one option - and save in "OPTARG"
while getopts "hlc:" arg; do
  case $arg in
    h)
     # Found -h, show usage() 
      usage
      ;;
    l)
      # Found a -l, use live mode"
      live_mode=1
      ;;
    c)
      # Found -c, argument value is stored in 'OPTARG'
      count=$OPTARG
      ;;      
  esac
done

echo "Live Mode: $live_mode " 
echo "Count count: $count" 

cmd_base="./test_script.py"

# Use the linux "sequence" command to loop $count times 
# We'll use the "live mode" flag here - it's helpful when reviewing 
# what a script will do when it runs live 
for i in $(seq 1 $count); do
  echo "++===============================++"
  cmd="$cmd_base --arg1 some_text_$i --failpct 30"
  echo "cmd to run: $cmd"

  # If we're in live mode, actually run the command 
  # for "not live_mode" the command is just skipped
  if [[ $live_mode == 1 ]]; then
      # Most command line programs will output to the console by default 
      $cmd
  fi
  echo "--===============================--"
  echo
done 

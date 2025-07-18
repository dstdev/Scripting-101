#!/bin/bash

# bash_template3.sh
# 21 May 2025 | cruhl@datainscience.com 
# 
# This file is the bare minimum for a readable and maintainable shell script 
#  The key elements are:
#     1) A usage/help function 
#     2) Command line arguments - miniumon of "-h" for "help/usage"
#     3) Live/Dry-run flag 
#         - I like the default to be non-live so I can review the commnads
#     4) A command wrapper function with logger output 
# Usage output  

function usage(){
    echo "bash_tempalte.sh - basic bash script boilerplate"
    echo "  Options: "
    echo "      -h : print this message"
    echo "      -l : 'live-run mode' - evaluate and run commands.  "
    echo "            default is 'dry-run mode' comands are only printed" 
    echo "      -d : debug mode - print debug output"
    echo "      -q : quiet mode - do not print command before running"
    echo "      -c <count>    : command loop count - run the command this many times"
    echo "      -g <log_file> : log file name default is bash_template2.log"
    echo "     " 
    exit
}

function iso_date(){
  date +"%Y-%m-%dT%H:%M:%S%z"
}

function log_output(){
  echo -n "$(iso_date) - " >> $log_file 
  echo $1 >> $log_file
}

function do_cmd_log(){
  # Grab all of the commands into $cmd
  cmd=$@
  
  # Do this when debug_mode is set 
  [[ $debug_mode == 1 ]] && echo "do_cmd_log - start"
  
  # Do this when quiet is NOT set
  [[ $quiet_mode == 0 ]] && echo $cmd

  # If we're in live_mode, actually run the command 
  if [[ $live_mode == 1 ]]; then 
      output=$($cmd 2>&1)
      echo $output
      log_output "$output"
  fi

}

# Set our default values 
debug_mode=0
# Not quiet by default, we print all command lines before running 
quiet_mode=0
live_mode=0 
count=0 
log_file="bash_looper3.log"

# Loop over input options 
# getopts "hlc:" means:
#  h - define "-h" flag with no options 
#  l - define "-l" flag with no options 
#  c: - ( note the ":" ) define "-c" flag with one option - and save in "OPTARG"
while getopts "qdhlc:" arg; do
  case $arg in
    h)
     # Found -h, show usage() 
      usage
      ;;
    l)
      # Found a -l, use live mode"
      live_mode=1
      ;;
    q)
      # Found a -q, use quiet mode"
      quiet_mode=1
      ;;    
    d)
      # Found a -d, use debug mode"
      debug_mode=1
      ;;            
    c)
      # Found -c, argument value is stored in 'OPTARG'
      count=$OPTARG
      ;;      
    g)
      # Found -c, argument value is stored in 'OPTARG'
      log_file=$OPTARG
      ;;        
  esac
done

echo "Live Mode:   $live_mode " 
echo "Count count: $count" 
echo "Log file:    $log_file"
echo "Debug Mode:  $debug_mode"
echo "Quiet Mode:  $quiet_mode"
echo "==========================================="
echo 

cmd_base="./test_script.py"

# Use the linux "sequence" command to loop $count times 
# We'll use the "live mode" flag here - it's helpful when reviewing 
# what a script will do when it runs live 
for i in $(seq 1 $count); do
    echo "+++=====================================+++"
    
    cmd="$cmd_base --arg1 hello_$i --failpct 30"
    
    do_cmd_log $cmd

    echo "---=====================================---"
    echo 
done 

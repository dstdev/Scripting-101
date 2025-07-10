#!/usr/bin/env python

# python_template1.sh
# 27 May 2025 | datainscience.com 
# 
# This file is the bare minimum for a readable and maintainable shell script 
#  The key elements are:
#     1) A usage/help function 
#     2) Command line arguments - miniumon of "-h" for "help/usage"
#     3) Live/Dry-run flag 
#         - I like the default to be non-live so I can review the commnads
#     4) Input for 'count' how many times to run the command 

import os 
import argparse

# Create the parser
# https://docs.python.org/3/library/argparse.html 
parser = argparse.ArgumentParser(prog="looper", description="Looper run a command some number of times")

# Add the arguments - argparse builds help automatically 
# We'll dd two arguments here 
parser.add_argument( "-l", "--live",
                     action="store_true",
                     required=False, 
                     default=False, 
                     help="Acturally run commands.  Default is to just print the command lines")

parser.add_argument( "-c", "--count", 
                    type=int, 
                    required=True, 
                    help="How many times to run the command")

# Parse the arguments
args = parser.parse_args()

cmd_base = "./test_script.py"

# Python needs a "range()" function for 'for loops' 
for c in range(0,args.count):
  
  # Build up the command string 
  print("++===============================++")
  cmd=f"{cmd_base} --arg1 some_text_{c} --failpct 30"
  # Always print the ccommand that will be run 
  print(f"Running: {cmd}")
  # If we're in 'live mode' run the command 
  if args.live:
    os.system(cmd)
  print("--===============================--\n")
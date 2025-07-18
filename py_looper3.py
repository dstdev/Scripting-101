#!/usr/bin/env python3

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


import argparse
from subprocess import Popen, PIPE 

# Get a logger 

import logging 
logging.basicConfig(
    filename=f"py_looper3.log",  # Specify the log file name
    level=logging.INFO,  # Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)
    filemode='a', # 'a' for append, 'w' for overwrite
    format='%(asctime)s - %(levelname)s - %(message)s',  # Define the log message format
    datefmt='%Y-%m-%d %H:%M:%S' # Format for the timestamp
)
logger = logging.getLogger("looper3")

# Create the parser
# https://docs.python.org/3/library/argparse.html 
parser = argparse.ArgumentParser(prog="looper3", description="Looper run a command some number of times")

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

def do_cmd(cmd: str) -> tuple: 
    # Always print the ccommand that will be run - the syntax " ".join(cmd)
    # translates to - take the elements of the list cmd and joint them to a string 
    # separted by spaces 
    print(f"Running: {" ".join(cmd)}")
    logger.info(f"cmd to run: {' '.join(cmd)}")
    # If we're in 'live mode' run the command 
    if args.live:
        proc = Popen(cmd, stdout=PIPE, stderr=PIPE, stdin=None)
        std_out, std_err = proc.communicate() 
        
        if proc.returncode != 0: # The command failed!
            msg = f"looper: std_err: {std_err.decode('utf-8')}"
            print(msg)
            logger.error(msg)
        
        else: 
            print(f"looper: std_out: {std_out.decode('utf-8')}")
        print(f"looper rc: {proc.returncode }")    
        logger.info(f"complete: {' '.join(cmd)}")
    return (std_out, std_err, proc.returncode) 


def main():
    cmd_base = "./test_script.py"

    # Python needs a "range()" function for 'for loops' 
    for c in range(0,args.count):
        print("++===============================++")
        # Build up the command arument list, the Popen command expects 
        # the command to be in the form of a list, with one arg per list
        # element 
        cmd = [f"{cmd_base}", "--arg1", f"some_text_{c}", "--failpct", "30"]
        do_cmd(cmd)
        print("--===============================--\n")

if __name__ == "__main__":
    logger.info("starting.")
    main() 
    logger.info("ended.")



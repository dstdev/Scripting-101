#!/usr/bin/env python3

""""test_script.py is a useful for testing other command wrappers
    usage: 
    test_script.py --arg1 argstring --success | --fail | --failpct pct [ --arg2 argstring ] 

    example:

        test_script.py --arg1 'a few words' --arg2 hello --success
            test_script success!
            arg1: a few words - arg2: hello
            exiting with rcr: 0

        test_script.py --arg1 'a few words' --arg2 goodbye --fail
            test_script failed!
            arg1: a few words - arg2: goodbye
            exiting with rc: 5

"""

import argparse 
import sys 
from subprocess import Popen, PIPE 
from random import randint 


parser = argparse.ArgumentParser(prog='test_script.py')
# One required and two optional string input args 
parser.add_argument("--arg1", type=str, help="String arg one", required=True)
parser.add_argument("--arg2", type=str, help="String arg two", default="")

# Can't use both --success and --fail so set up mutex group 
group = parser.add_mutually_exclusive_group()
group.add_argument('--success','-s', action='store_true', default=False)
group.add_argument('--fail', '-f', action='store_true', default=False)
group.add_argument('--failpct','-p', type=int, help='failure percentage, 0-100', default=False)  

args = parser.parse_args()

def main():
    
    arg_line = f"arg1: {args.arg1} - arg2: {args.arg2}\n"
    rc = 0

    if args.failpct is not False:
        # this is short and for generate a random integer, it it's 
        # higher than args, failpct, then fail is true, 
        failed = randint(0, 100) < args.failpct
    elif args.success is True:
        failed = False 
    else: 
        failed = True 
    
    # If we want a "good run", make some success output and set set the return code to zero 
    if not failed: 
        # success!
        rc = 0
        out_str  = f"test_script - success!\n"
        out_str += f"test_script - {arg_line}"
        out_str += f"test_script - rc: {rc}"
        print(out_str)

    
    # If we want a "bad run", make some failure output and set set the return code to 5    
    if failed:
        rc = 5
        out_str  = f"test_script - failed!\n"
        out_str += f"test_script - {arg_line}"
        out_str += f"test_script - rc: {rc}"
        print(out_str, file=sys.stderr)
    sys.exit(rc)

if __name__ == '__main__':
    main() 
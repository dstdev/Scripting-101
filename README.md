## About Scripting-101
Scripting 101 is a short comparison between Bash scripts, Python Scripting and an Asible Playbook 
Templates all run a command some number of times. The bash and python scripts follow the same format. #1 - mvp (minimum viable product) - Help function, counter, and a "live" flag. 

`test_script.py`  
This is a script used to test other wrapper scripts. It takes one or two arguments and will optionally fail for succeed. 
```
usage: test_script.py [-h] --arg1 ARG1 [--arg2 ARG2] [--success | --fail | --failpct FAILPCT]

optional arguments:
  -h, --help            show this help message and exit
  --arg1 ARG1           String arg one
  --arg2 ARG2           String arg two
  --success, -s         Return Code is 0
  --fail, -f            Return Codes is not 0
  --failpct FAILPCT, -p FAILPCT
                        failure percentage, 0-100
```

`bash_looper1.sh`  
This script will run `test_script.py` some number of times 
```
[chris@ajo-h1 Scripting-101]$ ./bash_looper1.sh -h
bash_tempalte.sh - basic bash script boilerplate
  Options: 
      -h : print this message
      -l : 'live-run mode' - evaluate and run commands.  
            default is 'dry-run mode' comands are only printed
      -c : command loop count - run the command this many times
```

## Install and Run
`git clone https://github.com/dstdev/Scripting-101.git`  
`cd Scripting-101`  
Run Example: 

`test_script.py` example:  
<pre><code>
[chris@ajo-h1 Scripting-101]$ <span style="color: green">./test_script.py --arg1 Hello --success </span>
test_script - success!
test_script - arg1: Hello - arg2: 
test_script - rc: 0
</code></pre>

`bash_looper1.sh` example: 
<pre><code>
[chris@ajo-h1 Scripting-101]$ <span style="color: green">./bash_looper1.py --arg1 Hello --success </span>

[chris@ajo-h1 Scripting-101]$ ./bash_looper1.sh -l -c 3
Live Mode: 1 
Count count: 3
++===============================++
cmd to run: ./test_script.py --arg1 some_text_1 --failpct 30
test_script - success!
test_script - arg1: some_text_1 - arg2: 
test_script - rc: 0
--===============================--

++===============================++
cmd to run: ./test_script.py --arg1 some_text_2 --failpct 30
test_script - failed!
test_script - arg1: some_text_2 - arg2: 
test_script - rc: 5
--===============================--

++===============================++
cmd to run: ./test_script.py --arg1 some_text_3 --failpct 30
test_script - failed!
test_script - arg1: some_text_3 - arg2: 
test_script - rc: 5
--===============================--


</code></pre> 

Script Requirements:  

**Requirement List - Script \*_1** 

    - Run a given command in a loop the number of times specified 
    - Script Level Notes at the top 
    - Help function 
    - '-h' argument for help 
    - '-c' argument for command loop count 
    - '-l' argument to actually run the command 
           the default is to just print the command to be run
    - output to console should not be captured 
    - errors should be ignored 

**Requirement List - Script \*_2** 

    - Run a given command in a loop the number of times specified 
    - Script Level Notes at the top 
    - Help function 
    - '-h' argument for help 
    - '-c' argument for command loop count 
    - '-l' argument to actually run the command 
           the default is to just print the command to be run
    - output to console should not be captured 
    - command return codes should be checked and errors noted on
      the console 

**Requirement List - Script \*_3** 

    - Run a given command in a loop the number of times specified 
    - Script Level Notes at the top 
    - Help function 
    - '-h' argument for help 
    - '-c' argument for command loop count 
    - '-l' argument to actually run the command 
           the default is to just print the command to be run
    - command output to the console and to a log file
    - command return codes should be checked and errors noted on
      the console 
  
  #### Log File
    - log file lines must be prepended with a time stamp 
    - timestamp format %Y-%m-%dT%H:%M:%S%z 

## Help and Contributing to the project
Contact Chris Ruhl :) 
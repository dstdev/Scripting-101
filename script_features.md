Templates all run a command some number of times.
Requirements: 
  ### Template 1 
    - Run a given command in a loop the number of times specified 
    - Script Level Notes at the top 
    - Help function 
    - '-h' argument for help 
    - '-c' argument for command loop count 
    - '-l' argument to actually run the command 
           the default is to just print the command to be run
    - output to console should not be captured 
    - errors should be ignored 

  ### Template 2 
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

  ### Template 3
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

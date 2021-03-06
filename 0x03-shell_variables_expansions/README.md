## Shell, Init Files, Variables and Expansions

### Read

- Read the pages Expansions, Shell Arithmetic, Variables, Shell initialization files and The alias Command.
- Read your /etc/profile, /etc/inputrc and ~/.bashrc files.
- Look at some files in the /etc/profile.d directory.
- Man or help: printenv, set, unset, export, alias, unalias, ., source, printf and previously learned commands.

### What you should learn from this project

#### Shell initialization files
- What are the /etc/profile file and the /etc/profile.d directory
- What is the ~/.bashrc file
#### Variables
- What is the difference between a local and a global variable
- What is a reserved variable
- How to create, update and delete shell variables
- What are the roles are the following reserved variables: HOME, PATH, PS1
- What are special parameters
- What is the special parameter $??
#### Expansions
- What is expansion and how to use them
- What is the difference between single and double quotes and how to use them properly
- How to do command substitution with $() and backticks
#### Expansions & Shell Arithmetic
- How to perform arithmetic operations with the shell
#### The alias Command
- How to create an alias
- How to list aliases
- How to temporary disable an alias
#### Other help pages
- How to execute commands from a file in the current shell
#### And
- What happens when you type $ ls -l *.txt

- Note: You do not have to learn about awk, tar, bzip2, date, scp, ulimit, umask, or shell scripting, yet.

### Requirements

- Allowed editors: vi, vim, emacs
- All your scripts will be tested on Ubuntu 14.04 LTS
- All your scripts should be exactly two lines long ($ wc -l file should print 2)
- All your files should end with a new line (why?)
- The first line of all your files should be exactly #!/bin/bash
- You are not allowed to use &&, || or ;
- You are not allowed to use bc, sed or awk
- All your files must be executable

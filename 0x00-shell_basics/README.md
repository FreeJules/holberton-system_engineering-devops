### Shell Basics

- In this project we learn following commands through writing scripts for each of them and making them executable.

## List of what each script does:

- 0-current_working_directory - Prints the absolute path name of the current working directory
- 1-listit - Displays the contents list of your current directory
- 2-bring_me_home - Changes the working directory to the user’s home directory
- 3-listfiles - Displays current directory contents in a long format
- 4-listmorefiles - Displays current directory contents, including hidden files (starting with .) using the long format
- 5-listfilesdigitonly - Displays current directory contents
- 6-firstdirectory - Creates a directory named holberton in the /tmp/ directory
- 7-movethatfile - Moves the file betty from /tmp/ to /tmp/holberton
- 8-firstdelete - Deletes the file betty
- 9-firstdirdeletion - Deletes the directory holberton that is in the /tmp directory
- 10-back - Changes the working directory to the previous one
- 11-lists - Lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
- 12-file_type - Prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script
- 13-symbolic_link - Creates a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory
- 14-copy_html - Copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory
- 15-lets_move - Moves all files beginning with an uppercase letter to the directory /tmp/u
- 16-clean_emacs - Deletes all files in the current working directory that end with the character ~
- 17-tree - Creates the directories welcome/, welcome/to/ and welcome/to/holberton in the current directory. You are only allowed to use two spaces in your script, not more.
- 18-commas - Lists all the files and directories of the current directory, separated by commas (,).

## Read:

- Read the page A Guided Tour of Emacs from the GNU, and go through the Emacs tutorial: Open emacs by typing emacs in your shell. Then type C-h t* to open the tutorial and go through it.

- * C-h t means hold the CONTROL key while typing the character h and then type t.

## What you should learn from this project

- What is Emacs
- Who is Richard Stallman
- The basic Emacs commands
- Opening and saving files
- What is a buffer and how to switch from one to the other
- Using the mark and the point to set the region
- Cutting and pasting lines and regions
- Searching forward and backward
- Invoking commands by name
- Undo
- Cancelling half-entered commands
- Quitting

## Requirements

- If Emacs is not installed on the VM, you can use this command to install it: sudo apt-get update; sudo apt-get install emacs
- Allowed editors: Emacs
- A README.md file, at the root of the folder of the project, describing what this project is about
- Each answer should be written in a file with the same syntax as Emacs's documentation (ex: C-h t)
- Your file should only contain the command, and nothing else

## Install emacs

- In your terminal:
- $ sudo apt-get update
- $ sudo apt-get upgrade
- $ sudo apt-get install emacs

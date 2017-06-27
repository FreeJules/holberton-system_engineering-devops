In this project we learn following commands through writing scripts for each of them and making them executable.
List of what each script does:
0-current_working_directory - Prints the absolute path name of the current working directory
1-listit - Displays the contents list of your current directory
2-bring_me_home - Changes the working directory to the user’s home directory
3-listfiles - Displays current directory contents in a long format
4-listmorefiles - Displays current directory contents, including hidden files (starting with .) using the long format
5-listfilesdigitonly - Displays current directory contents
6-firstdirectory - Creates a directory named holberton in the /tmp/ directory
7-movethatfile - Moves the file betty from /tmp/ to /tmp/holberton
8-firstdelete - Deletes the file betty
9-firstdirdeletion - Deletes the directory holberton that is in the /tmp directory
10-back - Changes the working directory to the previous one
11-lists - Lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
12-file_type - Prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script
13-symbolic_link - Creates a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory
14-copy_html - Copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory
15-lets_move - Moves all files beginning with an uppercase letter to the directory /tmp/u
16-clean_emacs - Deletes all files in the current working directory that end with the character ~
17-tree - Creates the directories welcome/, welcome/to/ and welcome/to/holberton in the current directory. You are only allowed to use two spaces in your script, not more.
18-commas - Lists all the files and directories of the current directory, separated by commas (,).
Directory names should end with a slash (/)
Files and directories starting with a dot (.) should be listed
The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning
Only digits and letters are used to sort; Digits should come first
You can assume that all the files we will test with will have at least one letter or one digit
The listing should end with a new line
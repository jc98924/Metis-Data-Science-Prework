# Command Line Crash Course

### root directory

**bin** *contains binaries for commands typed into command line. When a command is typed, the OS will search /bin for a matching executable. 

**dev**

**etc** *config files for the system

**home** *home base of Unix system. For Linux it is located at /home/; Mac is located at /Users/

**usr** *user-specific bin and lib directories. 

**lib** *system libraries and other essentials that the system needs to run various programs under the hood

**var**

**vol**

**tmp** *where temp files that may be needed during running programs will/can be stored


## General Command Structure
### Options and Arguments
There are generally 3 parts to a command  
* The name of the command; e.g. cd, ls, cat, etc
* Arguments <directory_name>; e.g cd <directory_name> or ls <directory_name>
* Optional Flags; options that you can set on the given command to dictate the way it runs
	* -l for ls -l, -rf for rm -rf <dir_to_remove>
	* Options are specified with leading -
	* You can combined multiple options in one - (for instance -rf is like -r -f)
	* Options have more informative alternatives by using --, -V or --version

### Getting Help 
* man <command_name> : calls out to the help manual with documentation of the given command
	* ex. man ls
* man -k <command_name> : works like apropos; search for all commands that you may mean
* info <command_name> : works like 'man, gives you documentation on the desired command
* <command_name> --help : Not unique to unix, but many commands you can run will accept a --help parameter; similar documentation to **man** and **info**.  
* apropos <command_name> : works like man-kl search for commands the system thinks you may mean

### Common Basic Commands
---
#### Filesystem Navigation
* **cd**: 'Change Directory'
	** cd <directory_to_go_to>
	** cd takes you to home directory, cd / takes you to root, cd .. takes you up one directory level
* **pwd**: 'Print (Present) Working Directory- : Checks the directory that you're currently in and prints it out for you. 
* **ls**: 'List'; List the files and directories in your present working directory, or whatever directory you explicity specify
	** ls <path_to_file/directory>
	** -l : displays more detailed information about the various files
	** -a : includes hidden files starting with a '.'
	** -h : human readable file sizes like MB or GB
#### Viewing Files
* **cat**: 'Concatenate' : Prints the content of the file to standard output (console by default)
	** cat <filename>
	** echo 'Hello World' > hello.txt
	   cat hello.txt 
* **less**: Allows scrolling through files, good for large files so it doesn't have to be all dumped to the console
	** less <filename>
	** space bar = page down, arrow keys = scroll up/down by line, q = quit
* **head**: View the beginning of the file. 
	** head <filename>
	** -n: set number of lines; ex head <filename> -n: 20  (first 20 lines)
* **tail**: View the end of the file 
	** tail <filename>
	** -n: set number of lines; ex tail <filename> -n: 20 (last 20 lines)
	** -f: Allow it to keep printing out if new lines are added

#### Moving Files Around
* **cp**: 'Copy': copy files(s) or directorie(s) from one location to another
	** cp <from_file> <to_location>
	** -R: recursive, allows you to copy directories
* **mv**: 'Move': move file(s) or directories from one place to another 
	** mv <file> <file> *renaming a file 
	** mv <file> <location> ; ex mv hello.txt /home/jc98924/Metis
* **mkdir**: 'Make Directory': creates a directory with given filename
	** mkdir <dirname>

* **rm**: 'Remove': deletes given file 
	** rm <file>
	** -r: recursive, allows you to delete directories
	** -f: force it, do not ask if sure
	** -rf:
#### Examining Disk Space
* **df**: 'Disk Free': check total diskspace used/availabl
* **du**: 'Disk Usage': check out the disk space used by a file or directory
	** du <directory>
* **find**: seach for files in the file system
	** find <path_to_search> <expressions_to_look_for>
* **grep**: search text for lines matching a specific pattern.
	** grep <expression_to_look_for> <file>
* **wc**: 'Word Count'
	** wc <file>
	** -1 : count lines instead of words
* **sort**: sort lines of file and output it to terminal; does not sort actual file
	** sort <input_to_sort>
* **who**: displays active users
* **which**: find the location of a binary file (command) that you are trying to run
	** which <program_to_examine>
* **gzip**: zip files in the gzip format
	** gzip <files>
* **gunzip**: unzip gzipped files
	** gunzip test.gz
* **tar**: tar or untar (archive/unarchive) a batch of files
* **zcat**: peak into gzipped files without unzipping them
* **echo**: print a string to standard output (console by default)

### Standard Input and Output
**Standard Input (stdin)**: what is entered into the terminal; inherited from parent shell by sys.stdin
**Standard Output (stdout)**: the place where the results of the command will be sent

**Redirection Operators**

* **Pipe: |** : will 'pipe' the reults of the command preceding it into the input for the command following it. Redirects stdout for command 1 to be the input args for the command 2 and the stdin for the command 2 is now the output of command 1
	** Ex. $ du -d 1 ~ | sort -n -r | head
	** take the summary of disk usage, sort it in descending order numerically and show the top 10 results

* **>**: take output of a preceding command and sends it to a specific file; will overwrite
* **>>**: takes output of a preceding command but does not overwrite the file if it exists, just appends it
* **<**: preceding command gets as arguments the contents of the file following the <

### Permissions
For all files in a Unix system, there are 3 access classes with 3 types of access for each

#### Access Classes
* **User (u)**
* **Write (w)**
* **Systemwide (a: all or o: other)**

#### Access Types
* **Read (r)**
* **Write (w)**
* **Execute (x)**  

There are 3 x 3 = 9 permission specifications for every file.  
When you run ls -lh, you will see a string of rwx - characters.  

drwxr-xr-x 26 jc98924 jc98924 4.0K Jun 18 14:57  anaconda3
-rw-rw-r--  1 jc98924 jc98924 655M Jun 18 01:45  Anaconda3-2019.03-Linux-x86_64.sh
drwxr-xr-x  3 jc98924 jc98924 4.0K Jun 18 01:55  Desktop
drwxr-xr-x  2 jc98924 jc98924 4.0K Jun 18 14:30  Documents
drwxr-xr-x  2 jc98924 jc98924 4.0K Jun 19 14:58  Downloads

The string will start with either d (directory) or - (file)  
Each three letter combination represents user, group, and/or systemwide in order  

Under anaconda3:
* The user jc98924 has full rwx access
* The group jc98924 has read and execute access
* The system/others has read and execute access

### Changing Permissions
* **chmod**: change the access permissions on the file
	** chmod {access_specifier} {file_or_directory}

**List of specifier options**
* |--------|---------| 
* | u | User | 
* | g | Group | 
* | o | Other | 
* | a | All | 
* | r | Read | 
* | w | Write | 
* | x | Execute | 
* | + | Add permission | 
* | - | Remove Permission |

* **chown**: change the owner of a file 
	** chown {user} {file}
* **chgrp**: change the group of a file
	** chgrp {group} {file}

### Processes
Anything that is running on a Unix OS is a process
* **ps**: list running processes
	** -e : display process environment details
	** -f : display various process details
* **top**: brings up an interactive monitor for checking running processes; similar to task manager in Windows
* **kill and pkill**: kill running processes by various means

### Scripts
You can create scripts that run any number of commands. These are run through the shells (Bash or others).
If a file ends with extensions .sh, they are shell scripts. 

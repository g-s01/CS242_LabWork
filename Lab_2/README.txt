Question 1:
In this question, we needed to back up a set of files whose names/path were supplied in another file 
and the directory to which we needed to store the backups was also given.

Firstly, I check that the number of inputs is exactly 2, if not then the program terminates then and there.

Secondly, I checked if the file path and directory path supplied is genuine or not, that is to check
if the files is really a regular file and the directory is also a regular directory. 
If not, then the program terminates then and there.

Finally, I run a while loop to read the contents of the file.
Firstly, I create a file named as filename.bak, then copy the contents of the original file into this file.
Then, I move this backup file to the required directory given in the input.

Note: The variable names might not be appropriate to the question but this has been done 
delibrately to avoid plagriaism as the genuine and common names will be used by everybody.

Question 2:
In this question, we needed to output a random string of the required length. 
There may be any number of same character substrings. However, at no time the length of 
such a substring may exceed the count.

Firstly, I store the input in a string variable. Then, I take the input of count and length.
Then, starting the procedure I randomly print a character of the string.
After that, I run a for-loop to output the next randomly generated character while 
maintaining the condition that there may be any number of same character substrings, however,
at no time the length of such a substring may exceed the count.

Note: This script assumes that the number of distinct alphabets in the input string is greater than 1, 
if any arbitrary value of count and length shall be given.
If the number of distinct alphabets in the input string is 1, then the count should be greater than the
length for a defined output.

Note: The variable names might not be appropriate to the question but this has been done 
delibrately to avoid plagriaism as the genuine and common names will be used by everybody.
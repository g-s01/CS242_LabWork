Question 1:
In this question we need to compute the minimum number of denominations to 
provide change for a given amount of money in some currency having
1, 5, 10, 20, 25, and 50 units. Also, we need to print the optimal construction.

Approach:
Make a dictionary (named minimum in the question, but will be referred to as m 
in this file) to store the minimum number of coins required to make any 
amount i, obviously, we need to print m[n], where n is the amount entered by 
the user. Also, we need to make another dictionary (named minimum_denomination 
in the question, but will be referred to as l in this file) to store the 
first denommination that will be used in the optimal construction of the 
required amount. Obviously, we will run a while-loop to store the optimal 
construction of the required amount as follows:

while(n > 0)
	store(l[n])
	n -= l[n]
print stored values
as we store l[n], we need to now construct only n-l[n] now so we decrement n 
till we reach zero.

To calculate m[n], l[n] we can use iterative dynamic programming as follows:
Base case: m[0] = 0
Recursion step: Iterate through the denomination array and 
m[n] = minimum(m[n-denomination]+1) which essentially translates into: 
we try each denomination to construct n, so after using the denomination 
we are left to construct a sum of (n-denomination) we set m[n] as the 
minimum of m[n-denomination]+1 among all the denominations, note we use 
m[n-denomination]+1 as we have used one denomination already, so we need to add 
a 1 in m[n-denomination].
Also, l[n] = denomination for which m[n-denomination]+1 is minimum as the 
denomination for which that value is minimum, will surely be used in the 
construction of the optimal solution.

Do the above for all amounts between 1 and n inclusive to find m[n], l[n].

Algorithm:
(1) Take the input, if input<0, exit the program
(2) Make the denomination array
(3) Make the maps m and l, set the base conditions
(4) Run a for loop from i = 1 to i = n, and applying the 
		recursion step discussed above.
(5) Run a while loop to store the optimal construction of n
(6) Print the required results

Now, the above works in reasonable time and memory for input <= 10^6, to optimise
the time and space required for inputs > 10^6, the following optimisation is 
proposed:
Number of coins required to construct n = n//100 + Number of coins required to 
construct n%100
Proof: As the least-common-multiple (LCM) of the denominations is 100, to 
construct any sum greater than 100, we need to replace it with multiples of 100, 
till we can't make more, then apply the algorithm discussed above for n%100.
The LCM of the values provides a minimum upper bound on the "break point", 
that point at which we cannot blithely assume that the highest-denomination 
coin is part of the solution.

Running the file: $ python3 fileName.py
Input: The user only needs to input an integer n

Question 2:
In this question we need to make two LaTeX files we should produce the output 
as desired in the question statement.
In every latex file, we need to specify the encoding, packages and the document 
class before starting anything, and therefore each page has it's specific 
settings which can be read at the top of the file.

Page 1:
I have used the \title, \author, \date methods to display the information such as
the title of the document, it's author and the date, then I begin my document.
In the page, the text mode is used to write normal text and 
math mode (starts and ends with $ or special \begin{} \end{}) to write 
mathematical formulas. \begin{equation} and \end{equation} is used to align 
one equation while \begin{flalign} and \end{flalign} is used to align 
more than one equation. Equations are labelled so as to create hyperlinks 
in the future. Matrices tags such as \pmatrix, \bmatrix and \matrix are used 
depending on the bracket required to enclose the matrix, which is given in 
the question statement.

Page 2:
Here, as we don't need to display the equation numbers while displaying the 
equations, we will use \begin{align*} and \end{align*} etc, to display various 
equations. Also, use & to align equations continuing to the next line. 
All the other things in the page include matrix similar to page 1 and printing 
some standard LaTeX symbols. 

Running the files:
It is recommended to run the files on Overleaf IDE. If the user intends to run
the files on his/her OS, then the following packages must be installed along
with a standard LaTeX compiler (use TeXLive preferrably):

(1) inputenc package to specify the encoding
(2) amsmath package to enhance the representation of math formulas
(3) hyperref package to create hyperlinks in the documentation

Also, quoting- An introduction to the LATEX cross-referencing system, 
Thomas Thurnherr, TUGboat, Volume 38 (2017), No. 1:

"
A document generally requires two typesetting runs to generate reference numbers.
.....
Whenever references cannot be generated correctly by the system, double question
marks (??) are produced in the output document 
"

Due to this reason, the first file needs to be compiled twice for the hyperlinks
to work correctly. So, kindly do the same.

Note: If you are unable to compile the given two LaTeX files on your system, I 
have included a folder named "Latex_Support_Files_and_PDF" which contains
the PDF files generated by my compiler and the corresponding support files, 
in a situation where nothing is available, kindly refer to that folder.

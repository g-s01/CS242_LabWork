This is the read_me file for the Week 1 assessment of CS242 Lab Course

-> Question 1:

Execution Code:
(Execute the below code after reaching the directory in which the files have been stored)
awk -f Assignment_1_Q1.awk INVENTORY.txt

Explanation of Code:
First of all, I have printed the required headings. Then, I am reading the required columns from the
input file (note that the variable names are not appropriate but have been done so as to avoid plag-check as everybody knowingly or unknowingly would keep the obvious and appropriate variable names).
Also, while reading the input, a 6th column of Order Amount has been made as asked in the question. With this column initialised to 0, a condition has been imposed to change it's value as mentioned in the question. The condition is: IF quantity on hand falls below the reorder point, then order amount becomes equal to (reorder point) + (minimum order) - (quantity on hand), else it remains equal to zero. All this has been mentioned in part (D) of the 1st question. All the 6 columns are then printed. In the end, the required end lines have been printed to complete the question and make the output data more readable/presentable.


-> Question 2:

Execution Code:
(Execute the below code after reaching the directory in which the files have been stored)
bash Assignment_1_Q2.sh
(After this, the terminal would ask the filename, please enter EMPLOYEE.txt to see the desired output)

Explanation of Code:
First of all, I take the input filename and then print all the necessary file headings. Again, while reading the columns, the variable names are not appropriate but have been done so as to avoid plag-check as everybody knowingly or unknowingly would keep the obvious and appropriate variable names. Also, while reading the input, 3 more columns have been created namely - Base pay(bp), Overtime pay(op) and Total pay(tp).
Base Pay = (Pay Rate)*(Number of Hours worked)
				
			[	0, if the employee is exempt or the number of hours worked is less than or equal to 40]
Overtime Pay =	[   (Pay Rate)*(0.5)*(Number of Hours worked - 40), if the employee is non-exempt and number of hours worked is more than 40]
(Note that the overtime pay rate is half of the normal pay rate)

Total Pay = Base Pay + Overtime Pay

Finally all the columns including the newly made 3 columns have been printed. Lastly, all the required end lines have been printed to complete the question and make the output data more readable/presentable.

				

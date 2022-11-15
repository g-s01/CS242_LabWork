# For coloring the output
class color:
	DARKCYAN = '\033[36m'
	GREEN = '\033[92m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	END = '\033[0m'

# Taking input
n = float(input("Enter the amount of money (in corresponding currency units): "))
# If n<0, then the input is practically impossible to construct
if (n < 0): 
	print("Error: Amount can't be less than 0")
	quit()
# If n is fractional number, then also the input is practically impossible
# to construct
if (n//1 != n):
    print("Error: Amount can't be fractional")
    quit()
# List of all the available denominations
n = int(n)
denominations = [1, 5, 10, 20, 25, 50]
# Dictionary to store the minimum number of denominations to represent the key
minimum = {}
# Dictionary to store the first  denomination in the optimal solution of constructing the amount
minimum_denomination = {}
# Dictionary to store the optimal solution for constructing the amount
optimal_solution = {}
# It takes 0 coins to represent 0
minimum[0] = 0
for i in range(len(denominations)):
 minimum[denominations[i]] = 1
 optimal_solution[denominations[i]] = 0
# Calculating the minimum number of denominations to represent numbers from 2 to n
for i in range(2, min(n+1, 1000000)):
# setting minimum[i] to an arbitrary large value which is nearly impossible to achieve for any i
 minimum[i] = 1e100
 for j in range(len(denominations)):
  if (denominations[j] <= i):
# if number of notes required to make amount of i-denominations[j] + 1 < current number of notes required to make amount of i, then we update the number of notes required to make amount of i, also this would mean the first denomination in the optimal solution would be denominations[j] so we also update 
   if (minimum[i-denominations[j]]+1 < minimum[i]):
    minimum[i] = minimum[i-denominations[j]]+1
    minimum_denomination[i] = denominations[j]

if(n <= 1e6):
 print(f'Minimum number of coins to construct the amount:')
 print(color.GREEN) 
 print(f'{minimum[n]}')
 print(color.END)

 print('The optimal construction is as follows:')
 while(n > 0):
	 optimal_solution[minimum_denomination[n]] = optimal_solution[minimum_denomination[n]]+1
	 n -= minimum_denomination[n]
# Printing the optimal solution
 print(color.GREEN)
 for i in range(len(denominations)):
     if(optimal_solution[denominations[i]]) > 0:
         print(f'The number of coins of denomination {denominations[i]} used is {optimal_solution[denominations[i]]}')
 print(color.END)

# Since the program will run quit slow for inputs greater than 10^6, I propose an optimisation.
# Number of coins required to make the input = 2*(input//100) + Number of coins required to make the remainder when input is divided by 100. Proof of this is given in the README file. (where x//y denotes taking the floor of the division x/y)
# Hence the process is done for n%100 while we precalculate the number of 50 coins required as 2*(n//100).
else:
    print(f'Minimum number of coins to construct the amount:')
    print(color.GREEN)
    # Minimum number of coins required = 2*(n//100) + minimum[n%100], we add 2*(n//100) as it takes minimum 2-50 denomination coins to make a 100-denomination
    print(f'{2*(n//100) + minimum[n%100]}')
    print(color.END)

    print('The optimal construction is as follows:')
    optimal_solution[50] = 2*(n//100)
    n %= 100
    while(n > 0):
        optimal_solution[minimum_denomination[n]] = optimal_solution[minimum_denomination[n]]+1
        n -= minimum_denomination[n]
# Printing the optimal solution
    print(color.GREEN)
    for i in range(len(denominations)):
        if(optimal_solution[denominations[i]]) > 0:
            print(f'The number of coins of denomination {denominations[i]} used is {optimal_solution[denominations[i]]}')
    print(color.END)

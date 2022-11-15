# For coloring the output
class color:
	DARKCYAN = '\033[36m'
	GREEN = '\033[92m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	END = '\033[0m'

# Taking input
n = int(input("Enter the amount of money (in corresponding currency units): "))
# If n<0, then the input is practically impossible to construct
if (n < 0): 
	print("Error: Amount can't be less than 0")
	quit()
# List of all the available denominations
denominations = [1, 5, 10, 20, 25, 50]
# Dictionary to store the minimum number of denominations to represent the key
minimum = {}
# Dictionary to store the first  denomination in the optimal solution of constructing the amount
minimum_denomination = {}
# List to store the optimal solution for constructing the amount
optimal_solution = []
# It takes 0 coins to represent 0
minimum[0] = 0
for i in range(len(denominations)):
 minimum[denominations[i]] = 1
# Calculating the minimum number of denominations to represent numbers from 2 to n
for i in range(2, n+1):
# setting minimum[i] to an arbitrary large value which is nearly impossible to achieve for any i
 minimum[i] = 1e100
 for j in range(len(denominations)):
  if (denominations[j] <= i):
# if number of notes required to make amount of i-denominations[j] + 1 < current number of notes required to make amount of i, then we update the number of notes required to make amount of i, also this would mean the first denomination in the optimal solution would be denominations[j] so we also update 
   if (minimum[i-denominations[j]]+1 < minimum[i]):
    minimum[i] = minimum[i-denominations[j]]+1
    minimum_denomination[i] = denominations[j]

print(f'Minimum number of coins to construct the amount:')
print(color.GREEN) 
print(f'{minimum[n]}')
print(color.END)

print('The optimal construction is as follows:')
while(n > 0):
	optimal_solution.append(minimum_denomination[n])
	n -= minimum_denomination[n]
# Printing the optimal solution
print(color.GREEN)
print(*optimal_solution, sep = ", ")
print(color.END)

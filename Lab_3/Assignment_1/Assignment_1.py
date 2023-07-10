# for coloring the output
class color:
   DARKCYAN = '\033[36m'
   GREEN = '\033[92m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'

# taking input
n = int(input("Please enter the number of persons in the circle: "))
k = int(input("Please enter the skip number agreed upon: "))

if(n == 0):
    print("There is nobody in the circle from the start only!")
elif(k >= 0): 
    # the required collection of persons
    persons = []
    # the person from whom we count the k persons
    ref = 0
    for i in range(1, n+1):
        persons.append(i)
    while(len(persons) > 1):
        # index of the person to be killed
        psn_to_b_killed = (ref+k)%(len(persons))
        print(color.DARKCYAN + f"Person {persons[ref]} " + color.END + color.BOLD + "killed " + color.END + color.RED + f"Person {persons[psn_to_b_killed]}" + color.END)
        persons.remove(persons[psn_to_b_killed])
        # new reference person
        ref = psn_to_b_killed%(len(persons))
        print(f"Now the person(s) left in the circle are: " + color.GREEN + f"{persons}" + color.END)
else:
    # if k < 0, then it does not make sense to kill anyone
    print("Invalid skip number!")
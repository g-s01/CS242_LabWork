from copy import deepcopy

# for coloring the output
class color:
   DARKCYAN = '\033[36m'
   GREEN = '\033[92m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'

# Function to check inversion count of the input and output matrices
# If the parity of inversion count in the input and output is same, then the output state is reachable 
# from the input state
def inversion_count(matrix):
    cnt = 0
    for i in range(9):
        for j in range(i+1, 9):
            if(matrix[i] > matrix[j] and matrix[j] != '0' and matrix[i] != '0'): cnt = cnt+1
    return cnt

# Function to find depth of the node
# Logic: Go to the parent of the current node until you reach the root node, while incrementing the depth variable
def depth(current_state):
    cnt = 0
    while(parent.get(hash_function(current_state)) != current_state):
        current_state = parent.get(hash_function(current_state))
        cnt = cnt+1
    return cnt

# Hash-Function to hash matrices
# Logic: The matrix is converted into a string
def hash_function(matrix):
    s = ""
    for i in range(9):
        s += matrix[i]
    return s

# Function to find the fscore of a state
# fscore = depth_of_state + manhattan_distance
def find_fscore(current_state):
    count = 0
    coordinates_in_current_state = {}
    for i in range(3):
        for j in range(3):
            coordinates_in_current_state[current_state[3*i+j]] = [i, j]
    for i in range(9):
        j = str(i)
        count += abs(coordinates_in_current_state.get(j)[0]-coordinates_in_final_square.get(j)[0]) + abs(coordinates_in_current_state.get(j)[1]-coordinates_in_final_square.get(j)[1])
    return depth(current_state)+count-1

# Function to find the coordinates of 0 (the empty space)
def find(current_state):
    pair = []
    for i in range(3):
        for j in range(3):
            if(current_state[3*i+j] == '0'): 
                pair.append(i)
                pair.append(j)
                return pair

# Taking the inputs
initial_square = []
current_state = []
print(color.BOLD + "Enter the initial state of the square: " + color.END)
for i in range(3):
    item = []
    element = input()
    item.append(element.split())
    initial_square.append(item[0][0])
    initial_square.append(item[0][1])
    initial_square.append(item[0][2])
    current_state.append(item[0][0])
    current_state.append(item[0][1])
    current_state.append(item[0][2])

final_square = []
print(color.BOLD + "Enter the final state of the square: " + color.END)
for i in range(3):
    item = []
    element = input()
    item.append(element.split())
    final_square.append(item[0][0])
    final_square.append(item[0][1])
    final_square.append(item[0][2])

# evaluating the reachability of the states 
if(inversion_count(initial_square)%2 != inversion_count(final_square)%2):
    print(color.RED + "Output-State is not reachable from Input-State" + color.END)

else:
    # storing the position of numbers in the final configuration
    coordinates_in_final_square = {}
    for i in range(3):
        for j in range(3):
            coordinates_in_final_square[final_square[3*i+j]] = [i, j]
    # dictionary to store parents of each node, root node is the parent of itself
    parent = {}
    parent[hash_function(deepcopy(current_state))] = deepcopy(current_state)

    # list to store the already visited states
    visited_states = []
    visited_states.append(initial_square)
    # list to store the potential visited states
    potential_next_states = []

    # Actual solution
    # l tells whether the final and current states are equal or not
    l = True
    for i in range(3):
            for j in range(3):
                if(final_square[3*i+j] != current_state[3*i+j]): l = False
    if(l == True):
        print(color.BOLD + color.GREEN + "Input and Output states are one and the same!" + color.END)
    else:
        iterations = 1
        while (l == False and iterations <= 50000-1):  
            pair = find(current_state)
            x = pair[0]
            y = pair[1]

            # to see if we can move upwards in the matrix
            if(x - 1 >= 0):
                child1 = []
                for i in range(3):
                    for j in range(3):
                        child1.append(current_state[3*i+j]) 
                child1[3*(x-1)+y], child1[3*(x)+y] = child1[3*(x)+y], child1[3*(x-1)+y]
                if(visited_states.count(child1) == 0):
                    potential_next_states.append(child1)
                    parent[hash_function(child1)] = deepcopy(current_state)
            # to see if we can move downwards in the matrix
            if(x + 1 <= 2):
                child2 = []
                for i in range(3):
                    for j in range(3):
                        child2.append(current_state[3*i+j])
                child2[3*(x+1)+y], child2[3*(x)+y] = child2[3*(x)+y], child2[3*(x+1)+y]
                if(visited_states.count(child2) == 0):
                    potential_next_states.append(child2)
                    parent[hash_function(child2)] = deepcopy(current_state)
            # to see if we can move left in the matrix
            if(y - 1 >= 0):
                child3 = []
                for i in range(3):
                    for j in range(3):
                        child3.append(current_state[3*i+j])
                child3[3*x+y-1], child3[3*x+y] = child3[3*x+y], child3[3*x+y-1]
                if(visited_states.count(child3) == 0):
                    potential_next_states.append(child3)
                    parent[hash_function(child3)] = deepcopy(current_state)
            # to see if we can move right in the matrix
            if(y + 1 <= 2):
                child4 = []
                for i in range(3):
                    for j in range(3):
                        child4.append(current_state[3*i+j])
                child4[3*(x)+y+1], child4[3*(x)+y] = child4[3*(x)+y], child4[3*(x)+y+1]
                if(visited_states.count(child4) == 0):
                    potential_next_states.append(child4)
                    parent[hash_function(child4)] = deepcopy(current_state)

            # loop to see the minimum fscore in the potential_next_states
            t = 1000000
            ind = -1
            for i in range(len(potential_next_states)):
                if(visited_states.count(potential_next_states[i]) == 1): 
                    continue
                else:
                    x = find_fscore(potential_next_states[i])
                    if(x < t): 
                        ind = i
                        t = x

            current_state.clear()
            for i in range(3):
                for j in range(3):
                    current_state.append(potential_next_states[ind][3*i+j])
            visited_states.append(deepcopy(current_state))

            l = True
            for i in range(3):
                for j in range(3):
                    if(final_square[3*i+j] != current_state[3*i+j]): l = False
            potential_next_states.remove(potential_next_states[ind])

        # optimal path is constructed by backtracking the parent of the current state
        path = []
        while(parent.get(hash_function(current_state)) != current_state):
            path.append(current_state)
            current_state = parent.get(hash_function(current_state))
        path.append(initial_square)

        # path is printed iff the path-length is less than 10 or the number of iterations is greater than 50000
        # which would imply that the path length is greater than 10
        path.reverse()
        if(iterations <= 50000):
            print(color.BOLD + color.GREEN + "Output-State is reachable from the Input-State" + color.END)
            for i in range(len(path)):
                print(color.GREEN + f"Step {i}: {path[i]}" + color.END)
        else:
            print(color.BOLD + color.GREEN + "Output-State is reachable from the Input-State but the path has not been discovered within 50,000 iterations of the algorithm" + color.END)
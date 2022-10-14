Question 1:
In this question, we need to output the sequence of killing of persons standing in a circle facing the center.

Approach:
Maintain a variable to store the index of the person from whom we start to skip the persons for killing.
Using this variable, find the index of the person to be killed. In 0-indexed array, it would be:
psn_to_b_killed = (ref+k)%(len(persons)),
where person to be killed's index = psn_to_b_killed, reference person's index = ref, 
k is the skip number that was agreed upon initially, persons is the array in which the alive persons are being
stored.

Algorithm:
(1) Take the input for number of persons and the skip number agreed upon
(2) Output the trivial cases if any using if-else conditionals
(3) Start killing the persons while maintaining the variables as mentioned in the approach till the 
    length of the array containing the alive persons is 1. Output the sequence at each step.

Question 2:
In this question, we need to give a solution to the 8-puzzle problem.

Approach:
This problem has been solved using the heuristic-A* approach.
A* algorithm:
An informed search to estimate the most optimal path from a given point to another given point.

Working: 
At each iteration of its main loop, A* needs to determine which of its paths to extend.
It does so based on the cost of the path and an estimate of the cost required to extend
the path all the way to the goal. Specifically, A* selects the path that minimizes f(n)=g(n)+h(n)
where n is the next node on the path, g(n) is the cost of the path from the start node to n, 
and h(n) is a heuristic function that estimates the cost of the cheapest path from n to the goal. 
A* terminates when the path it chooses to extend is a path from start to goal or if there are no paths eligible to be extended.
The heuristic function is problem-specific.

In this question, g(n) is the depth of each node from the root node, f(n) is the cost function defined as:
f(n) = summation of (|x1_i - x2_i| + |y1_i - y2_i|) from i = 1 to 8
where:
    (x1_i, y1_i) = coordinates of entry with the value of i in the final matrix (final state)
    (x2_i, y2_i) = coordinates of entry with the value of i in the current matrix (current state)

I maintain a list of nodes which can be potentially visited and from that list, I pickup the node with least
f(n) or fscore to be the next node to be explored.
I also maintain a map for storing the parent of each matrix, which is defined as the matrix on which one sliding 
operation was done to get the current matrix. This matrix is used to reconstruct the path from the input
to the output.

Algorithm:
(1) Take the input and output matrices
(2) Check the inversion condition in both the matrices, if the parity of the number of inversions in both
    the matrices is same then the final state is reachable else not.
(3) If the state is reachable, start traversing and put the untraversed child nodes of the current node in 
    a list, from where the matrix with the least fscore is picked to be the next current node.
(4) Also maintain a map which maps the current state to it's parent state.
(5) After the final state has been processed, retrace the path from the final state to the initial state, store the path in a list and reverse print the list.
(6) If the algorithm, takes more than 50,000 iterations to find the optimal path, then don't iterate more, rather tell that the output state is reachable from the input state.

Input:
Please give the input IN BELOW MENTIONED FORM ONLY:
Starting Shuffled Puzzle:
a11 a12 a13
a21 a22 a23
a31 a32 a33
Goal State:
b11 b12 b13
b21 b22 b23 
b31 b32 b33
where all entries are numbers in the range [0, 8] where the number 0 denotes the position of the space in both the states

Note: The program might take several seconds to compute. Kindly wait for at max 15 minutes for the programme to produce an output
Note: While copying the arrays, I use deepcopy so that changes made in any array is independent of the other.
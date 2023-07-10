# Question 1:
In this question, we need to output the sequence of killing of persons standing in a circle facing the center.

## Approach:
Maintain a variable to store the index of the person from whom we start to skip the persons for killing.
Using this variable, find the index of the person to be killed. In 0-indexed array, it would be:

$psn\textunderscore to \textunderscore b \textunderscore killed = (ref+k) \space mod \space (len(persons))$
<br> 

where 
1. person to be killed's index = $psn\textunderscore to \textunderscore b \textunderscore killed$
2. reference person's index = $ref$
3. $k$ is the skip number that was agreed upon initially, and persons is the array in which the alive persons are being
stored.

## Algorithm:
1. Take the input for number of persons and the skip number agreed upon
2. Output the trivial cases if any using `if-else` conditionals
3. Start killing the persons while maintaining the variables as mentioned in the approach till the 
    length of the array containing the alive persons is $1$.
4. Output the sequence at each step.

# Question 2:
In this question, we need to give a solution to the [8-puzzle problem](http://gamescrafters.berkeley.edu/site-legacy-archive-sp20/games.php?puzzle=8puzzle).

## Approach:
This problem has been solved using the heuristic-[A* approach](https://en.wikipedia.org/wiki/A*_search_algorithm).<br>
#### A* algorithm: An informed search to estimate the most optimal path from a given point to another given point.

## Working: 
At each iteration of its main loop, A* needs to determine which of its paths to extend.
It does so based on the cost of the path and an estimate of the cost required to extend
the path all the way to the goal. Specifically, A* selects the path that minimizes $f(n)=g(n)+h(n)$
where $n$ is the next node on the path, $g(n)$ is the cost of the path from the start node to $n$, 
and $h(n)$ is a heuristic function that estimates the cost of the cheapest path from $n$ to the goal. 
A* terminates when the path it chooses to extend is a path from start to goal or if there are no paths eligible to be extended.
The heuristic function is problem-specific.

In this question:
1. $g(n)$ is the depth of each node from the root node
2. $f(n)$ is the cost function defined as:

$f(n) =  \sum\limits_{i=1}^{i=8} |x1_i - x2_i| + |y1_i - y2_i|$

where: 
1. $(x1_i, y1_i)$ = coordinates of entry with the value of $i$ in the final matrix   (final state) 
2. $(x2_i, y2_i)$ = coordinates of entry with the value of $i$ in the current matrix (current state)


I maintain a list of nodes that can be potentially visited and from that list, I pick up the node with the least
$f(n)$ or $fscore$ to be the next node to be explored.
I also maintain a map for storing the parent of each matrix, which is defined as the matrix on which one sliding 
operation was done to get the current matrix. This matrix is used to reconstruct the path from the input
to the output.

## Algorithm:
1. Take the input and output matrices
2. Check the inversion condition in both the matrices, if the parity of the number of inversions in both
    the matrices are same then the final state is reachable else not.
3. If the state is reachable, start traversing and put the untraversed child nodes of the current node in 
    a list, from where the matrix with the least $fscore$ is picked to be the next current node.
4. Also maintain a map that maps the current state to its parent state.
5. After the final state has been processed, retrace the path from the final state to the initial state, store the path in a list, and reverse print the list.
6. If the algorithm, takes more than $50,000$ iterations to find the optimal path, then don't iterate more, rather tell that the output state is reachable from the input state.

## Input:
Please give the input IN BELOW MENTIONED FORM ONLY:

### Starting Shuffled Puzzle:

a<sub>11</sub> a<sub>12</sub> a<sub>13</sub> <br>
a<sub>21</sub> a<sub>22</sub> a<sub>23</sub> <br>
a<sub>31</sub> a<sub>32</sub> a<sub>33</sub>

### Goal State:

b<sub>11</sub> b<sub>12</sub> b<sub>13</sub> <br>
b<sub>21</sub> b<sub>22</sub> b<sub>23</sub> <br>
b<sub>31</sub> b<sub>32</sub> b<sub>33</sub>

where all entries are numbers in the range $[0, 8]$ where the number $0$ denotes the position of the space in both states.

Note: The program might take several seconds to compute. Kindly wait for at max $15$ minutes for the program to produce an output. <br>
Note: While copying the arrays, `deepcopy` was used so that changes made in any array are independent of the other.

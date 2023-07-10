# Question:
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

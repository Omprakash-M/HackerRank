In a cricket tournament, the organizer arranges matches in a hierarchy where each level represents a match round. The matches form a binary tree, where the root is the first match of the tournament, and each child node represents subsequent matches. The maximum depth of the tournament structure represents the maximum number of rounds a team has to win to become the champion.

Given the structure of the tournament in the form of a binary tree, find the maximum number of rounds (or depth) of the tournament.

Input Format

First line contains the number of nodes (matches).
The next line contains the values of nodes (matches) in level-order (use "null" for no match at that position).
Constraints

NA

Output Format

A single integer representing the maximum depth of the tournament structure (binary tree).

Sample Input 0

7
3 9 20 null null 15 7
Sample Output 0

3
Explanation 0

The first value 3 is the root of the binary tree (the first match).
The second and third values 9 and 20 represent the left and right matches of 3.
The values null indicate that node 9 has no children.
The next two values 15 and 7 represent the left and right matches of node 20.
The structure of the binary tree looks like this:

  3

 / \

 9 20

   / \

  15  7
The maximum depth of this binary tree is 3 because the longest path from the root 3 to the farthest leaf nodes (15 or 7) contains 3 nodes.

Sample Input 1

7
1 2 3 null null 4 5
Sample Output 1

3

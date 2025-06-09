In a cricket tournament, every team has several players, and among them are left-handed players. Each player is represented by a node in a binary tree, where the left and right children represent players in different roles. The tournament organizers want to calculate the total contribution (score) made by all left-handed players who are not further managing other players, i.e., left-handed players who are "leaves" (players with no further responsibilities).

The binary tree structure can help represent the hierarchy of the players, and our goal is to find the sum of the scores of all left-handed players who are at the end of the hierarchy (leaf players).

Input Format

First line contains the number of nodes (players).
The next line contains the values of nodes (scores of players) in level-order (use "null" for no player at that posit
Constraints

NA

Output Format

A single integer representing the sum of the scores of all left-handed (left child) leaf players.

Sample Input 0

7
3 9 20 null null 15 7
Sample Output 0

24
Explanation 0

The first value 3 is the root of the binary tree (captain).
The second and third values 9 and 20 represent the left and right players of 3.
The values null indicate that player 9 has no children.
The next two values 15 and 7 represent the left and right players of player 20.
The structure of the binary tree looks like this:

  3

 / \

9  20

   / \

  15 7
The left leaf in this binary tree is 9, and the left leaf of node 20 is 15. Therefore, the sum of the left leaf nodes is 9 + 15 = 24.

Sample Input 1

7
5 3 8 null null 6 10
Sample Output 1

9

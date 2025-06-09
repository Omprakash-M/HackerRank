In a cricket tournament, teams are ranked based on their performance, and the organizer uses a binary tree to structure the teams' rankings. The rankings are represented in such a way that:

Each node in the binary tree represents a team's ranking.
The inorder traversal of the binary tree gives the rankings of the teams based on the number of matches they had won.
Given a list of rankings for teams, you need to perform an inorder traversal of the binary tree to obtain the correct sequence of team rankings.

Input Format

First line contains the number of nodes (teams).
Next line contains the node values (team rankings) in level order for constructing the binary tree.
Constraints

NA

Output Format

A single line with the result of the inorder traversal of the binary tree

Sample Input 0

4
1 null 2 3
Sample Output 0

1 3 2
Explanation 0

The first value 1 is the root of the binary tree.
The second value null means the root 1 has no left child.
The third value 2 is the right child of the root 1.
The fourth value 3 is the left child of node 2.
The structure of the binary tree will look like this:

image

The inorder traversal visits nodes in the order:

Left subtree.
Root.
Right subtree.
For the given binary tree:

First, it visits 1 (root).
Then, it visits the left subtree of node 2, which is 3.
Finally, it visits node 2.
Thus, the inorder traversal output is 1 3 2.

Sample Input 1

5
10 5 15 null null 12 18
Sample Output 1

5 10 12 15 18

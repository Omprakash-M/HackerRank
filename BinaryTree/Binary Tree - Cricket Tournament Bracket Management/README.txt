In the context of a cricket tournament, teams are organized in a knockout format where each match's winner advances to the next round. You need to design a system to manage the tournament bracket using a binary tree representation. In this tree, each node represents a match between two teams, with the left child representing the winner of the first semi-final match and the right child representing the winner of the second semi-final match.

The goal is to input the results of the matches and display the tournament's progression in a pre-order traversal. This traversal will list each match in the order it occurred: starting with the final match, followed by the semi-finals, and so on.

Input Format

A single line of space-separated integers representing the department IDs.
-1 indicates that a department does not have a left or right sub-department.
Constraints

NA

Output Format

The output will be a single line of space-separated integers representing the pre-order traversal of the binary tree.

Sample Input 0

1 2 3 -1 -1 4 5 -1 -1 -1
Sample Output 0

1 2 3 4 5
Explanation 0

1 is the root of the tree.

2 is the left child of 1.

3 is the right child of 1.

-1 indicates that 2 does not have any children.

4 is the left child of 3.

5 is the right child of 3.

-1 indicates that 4 does not have any children.

-1 indicates that 5 does not have any children.

  1

 / \

2  3

   / \

  4  5
Traversal Steps

Start at the root node 1:

Visit and print 1.

Move to the left child 2:

Visit and print 2.

Since 2 has no left or right children, go back up.

Move to the right child 3:

Visit and print 3.

Move to the left child 4 of 3:

Visit and print 4.

Since 4 has no children, go back up to 3.

Move to the right child 5 of 3:

Visit and print 5.

Since 5 has no children, traversal ends.

The output of the traversal represents the order in which the nodes were visited, confirming that the pre-order traversal for the given tree structure is 1 2 3 4 5.

Sample Input 1

10 20 30 -1 -1 40 50 -1 -1 -1 -1
Sample Output 1

10 20 30 40 50

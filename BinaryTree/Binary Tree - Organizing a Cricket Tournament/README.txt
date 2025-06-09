In a cricket tournament, each team is ranked based on their performance. The teams need to be organized in a binary tree structure to quickly manage and track matchups. The binary tree represents the tournament bracket, where each node corresponds to a team, and the tree helps efficiently find opponents and record match results.

As the organizer, you need to insert new teams into this binary tree structure based on their registration order. Your task is to create a system that inserts teams into the binary tree and then displays the teams in a level-order (top-to-bottom) manner, so you can view the bracket.

Input Format

First line contains the number of teams to be inserted.
Next line contains the team rankings (as integers) to be inserted into the binary tree in sequence. Italic Text
Constraints

NA

Output Format

After all teams are inserted, display the team rankings in level-order traversal.

Sample Input 0

6
8 3 10 1 6 14
Sample Output 0

8 3 10 1 6 14
Explanation 0

The binary tree starts empty.
The first team with ranking 8 becomes the root.
The second team with ranking 3 becomes the left child of 8.
The third team with ranking 10 becomes the right child of 8.
The fourth team with ranking 1 becomes the left child of 3.
The fifth team with ranking 6 becomes the right child of 3.
The sixth team with ranking 14 becomes the right child of 10.
image

Sample Input 1

5
7 4 9 2 5
Sample Output 1

7 4 9 2 5

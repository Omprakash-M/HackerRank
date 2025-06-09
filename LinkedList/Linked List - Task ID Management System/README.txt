You are developing a simple task management application where tasks are represented by unique IDs. Users can add new tasks at the beginning of the task list for quick access. You need to write a program to handle the insertion of task IDs at the beginning of a linked list. After all insertions are completed, the final list of task IDs should be printed to confirm the additions.

Write a program to insert new task IDs at the beginning of the linked list. After all insertions, print the entire linked list to show the updated list of task IDs.

Input Format

The first line contains an integer N, the number of task IDs to be initially added to the linked list.
The second line contains N space-separated integers representing the task IDs.
Constraints

NA

Output Format

After completing all insertions, print the current linked list with elements separated by a space.

Sample Input 0

5
201 202 203 204 205
Sample Output 0

205 204 203 202 201
Explanation 0

Initially the linked list is empty. The first task ID 201 is inserted at the beginning, and the list becomes 201. The second task ID 202 is inserted at the beginning, and the list becomes 202 201. The third task ID 203 is inserted at the beginning, and the list becomes 203 202 201. The fourth task ID is inserted at the beginning, and the list becomes 204 203 202 201. The fifth task ID is inserted at the beginning, and the list becomes 205 204 203 202 201.

Sample Input 1

3
10 20 30
Sample Output 1

30 20 10

You are building a task tracker for project management, where each task is represented by a unique ID and tasks are stored in the order they need to be completed. Sometimes, due to changes in project priorities, certain tasks need to be removed from the list based on their position. Your task is to write a program that deletes a task at a specified position from the list and prints the updated list of remaining tasks.

Write a program that deletes a task (represented by a unique ID) from a given position in the linked list. After the deletion, print the updated list of task IDs. If the list is empty, Print the message as “List is empty”. If the entered position value is out the range, print the message as “Position out of range”.

Input Format

The first line contains an integer N, the number of task IDs initially added to the linked list.
The second line contains N space-separated integers representing the task IDs.
The third line contains an integer P, the position of the task to be deleted (1-based index).
Constraints

The value of P will always be between 1 and N (both inclusive).

Output Format

Print the updated task list with the elements separated by a space.

Sample Input 0

5
101 102 103 104 105
3
Sample Output 0

101 102 104 105
Explanation 0

The task list is initialized with 5 task IDs: 101 102 103 104 105. The task at position 3 (103) is removed from the list. The updated list after deletion is 101 102 104 105.

Sample Input 1

0
1
Sample Output 1

List is empty
Explanation 1

The task list is initially empty. Attempting to delete at position 1 returns "List is empty."

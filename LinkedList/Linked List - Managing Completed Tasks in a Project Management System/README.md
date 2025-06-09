You are developing a project management application for a team of software developers. In this application, tasks are represented by unique IDs, and team members can add tasks to their project. As tasks are completed, they need to be removed from the task list to maintain an organized view of ongoing tasks. The team wants to delete the completed tasks from the end of the list, ensuring they focus only on active work.

Write a program to manage the deletion of completed tasks from the end of the task list. After all deletions, print the updated list of remaining task IDs to show which tasks are still pending. If the list is empty, Print the message as “List is empty”.

Input Format

The first line contains an integer N, the number of task IDs to be initially added to the task list.
The second line contains N space-separated integers representing the task IDs.
The third line contains an integer M, the number of completed tasks to be deleted from the end of the list.
Constraints

NA

Output Format

After completing all deletions, print the current task list with elements separated by a space.

Sample Input 0

6
201 202 203 204 205 206
4

Sample Output 0

201 202

Explanation 0

The initial task list contains 6 task IDs: 201 202 203 204 205 206. After the first deletion, the task ID 206 (the last task) is removed. After the second deletion, the task ID 205 is removed. After the third deletion, the task ID 204 is removed. After the fourth deletion, the task ID 203 is removed. Finally, the remaining task list contains 201 202, indicating these are the active tasks left to complete.

Sample Input 1

5
101 102 103 104 105
5

Sample Output 1

List is empty

Explanation 1

The initial task list contains 5 task IDs: 101, 102, 103, 104, 105.After the first deletion, the task ID 105 (the last task) is removed from the list.After the second deletion, the task ID 104 is removed.After the third deletion, the task ID 103 is removed.After the fourth deletion, the task ID 102 is removed.After the fifth deletion, the task ID 101 is removed, which is the only task left in the list.Finally, after all deletions, the list becomes empty, indicating that all tasks have been completed and there are no active tasks left to work on. Thus, the output will be "List is empty."

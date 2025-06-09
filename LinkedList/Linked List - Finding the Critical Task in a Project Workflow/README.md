Imagine you are managing a long-term project with a series of tasks arranged in a linear sequence. Each task is dependent on the completion of the previous one, and the tasks are stored in a singly linked list. At certain points in the project, you want to identify the critical task, which lies in the middle of the task flow, so you can allocate additional resources to it and ensure timely completion.

In case there are two middle tasks, you want to focus on the second middle task as it represents the next crucial step in the project.

You are given the head of a singly linked list, where each node represents a task in a project workflow. Your task is to find and return the middle task. If the list has two middle tasks, return the second middle task and all the tasks after it.

Input Format

The input consists of a linked list represented by its head node.
Each node contains an integer value representing the task ID or any relevant information.
Constraints

NA

Output Format

The output will be a list of integers starting from the middle node to the end of the linked list.
If there are two middle nodes, the output should start from the second middle node.
Sample Input 0

5
1 2 3 4 5

Sample Output 0

3 4 5

Explanation 0

The list contains tasks with IDs: 1 -> 2 -> 3 -> 4 -> 5.
The total number of tasks is 5, and the middle task is task 3.
Since the list has an odd number of tasks, the function returns task 3 and all tasks following it (3 -> 4 -> 5).
Thus, task 3 is the critical point in the workflow, and the system returns the tasks starting from the middle node.
Sample Input 1

6
10 20 30 40 50 60

Sample Output 1

40 50 60

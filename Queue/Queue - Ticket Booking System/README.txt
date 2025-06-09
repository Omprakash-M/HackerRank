You are part of a development team creating a ticket booking system for an online movie ticket platform. This platform needs to manage user requests efficiently, allowing customers to book tickets in a first-come, first-served manner.

To implement this, you decide to use a queue data structure, which is ideal for handling scenarios where elements are processed in the order they arrive. In this case, customers will be queued for ticket booking, and once their turn arrives, they will be served.

Your task is to implement a queue using an array to handle customer requests. The system should support operations such as adding a new customer to the queue, serving a customer (removing them from the queue), and displaying the current queue status.

Implement a queue using an array that can perform the following operations:

Enqueue: Add a customer to the end of the queue.
Dequeue: Serve and remove a customer from the front of the queue.
Display: Show the current queue status.
Input Format

The first line represents the capacity The second line of input specifies the number of operations to perform. Each subsequent line contains an operation: For enqueue: ENQUEUE For dequeue: DEQUEUE For display: DISPLAY

Constraints

NA

Output Format

For DEQUEUE: Print the name of the customer being served.[if the queue is empty means Print "Served Customer: Queue is empty. No customer to serve."]

For DISPLAY: Print current queue elements, [if the queue is empty means Print "Queue is empty."]

If Queue is full -> Print [Queue is full. Cannot add (Customer name)]

Sample Input 0

10
5
ENQUEUE Alice
ENQUEUE Bob
DISPLAY
DEQUEUE
DISPLAY
Sample Output 0

Current Queue: Alice Bob
Served Customer: Alice
Current Queue: Bob
Explanation 0

The first command ENQUEUE Alice adds Alice to the queue.

The second command ENQUEUE Bob adds Bob to the queue.

The DISPLAY command shows the current queue status: Alice Bob.

The DEQUEUE command serves Alice, removing her from the queue.

The final DISPLAY command shows that only Bob remains in the queue.

Sample Input 1

5
6
ENQUEUE Alice
ENQUEUE Bob
DISPLAY
DEQUEUE
DISPLAY
DEQUEUE
Sample Output 1

Current Queue: Alice Bob
Served Customer: Alice
Current Queue: Bob
Served Customer: Bob

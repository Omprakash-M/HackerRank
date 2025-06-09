Imagine you are building a system to manage the library book collection in a university. Each book in the library is represented by a unique Book ID, and these books are stored in a binary tree. As the number of books increases, it becomes essential to keep track of how many books are currently in the collection. To solve this, you need to develop a program that will count the total number of books (nodes) in the binary tree.

Write a program in Java that inserts a list of Book IDs into a binary tree and then counts the total number of nodes in the binary tree (i.e., the total number of books in the system). The program should take the number of Book IDs and the list of Book IDs as input, insert them into the tree, and return the total count of books stored in the tree.

Input Format

An integer n representing the number of books (nodes) in the binary tree.
n integers representing the unique Book IDs.
Constraints

NA

Output Format

An integer representing the total number of books (nodes) in the binary tree.

Sample Input 0

5
30 20 40 10 50
Sample Output 0

5
Explanation 0

First, the program inserts the Book IDs (30, 20, 40, 10, 50) into the binary tree.

The tree will be built as a binary tree (not a binary search tree):

30 is inserted as the root.
20 is inserted as the left child of 30.
40 is inserted as the right child of 30.
10 is inserted as the left child of 20.
50 is inserted as the right child of 20.
After the insertion, the program uses a recursive method to count all the nodes in the binary Tree.

The output, 5, represents the total number of books (nodes) in the binary tree.

Sample Input 1

3
15 10 20
Sample Output 1

3

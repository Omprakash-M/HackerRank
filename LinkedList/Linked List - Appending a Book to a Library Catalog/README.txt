You are designing a digital library system where books are represented by unique book IDs. The library catalog is stored as a doubly linked list, allowing users to navigate both forwards and backwards through the list of books. When a new book is added to the library, it needs to be appended to the end of the catalog. Your task is to write a program that inserts a new book at the end of the catalog and prints the updated list of book IDs.

Write a program to append a new book (represented by a unique book ID) to the end of the doubly linked list representing the library catalog. After the insertion, print the updated list of book IDs.

Input Format

The first line contains an integer N, the number of books initially in the catalog.
The second line contains N space-separated integers representing the book IDs.
Constraints

The input values are all positive integers.
There will be at least 1 book in the catalog initially.
Output Format

Print the updated list of book IDs in sequence from the start to the end of the catalog.

Sample Input 0

4
201 202 203 204
Sample Output 0

201 202 203 204
Explanation 0

Initially, the catalog is empty. First, the new book ID 201 is appended to the end of the catalog. The list becomes 201. Then the second book ID 202 is appended to the end of the catalog, making the list 201 202. Next, the third book ID 203 is appended to the end of the catalog, updating the list to 201 202 203. Finally, the fourth book ID 204 is appended to the end of the catalog, resulting in the final list of book IDs: 201 202 203 204.

Sample Input 1

3
101 102 103
Sample Output 1

101 102 103

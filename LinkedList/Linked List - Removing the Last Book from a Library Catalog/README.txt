You are building a digital library system where each book is represented by a unique book ID. The library catalog is stored as a doubly linked list, allowing users to navigate through the list of books. Occasionally, books are removed from the library, and when a book is removed from the end of the catalog, it should no longer appear in the list. Your task is to write a program that deletes the last book from the catalog and prints the updated list of book IDs.

Write a program to delete the last book from the doubly linked list representing the library catalog. After the deletion, print the updated list of book IDs. If the list is empty, Print the message as “List is empty”.

Input Format

The first line contains an integer N, the number of books initially in the catalog.
The second line contains N space-separated integers representing the book IDs.
Constraints

The input values are all positive integers.
There will be at least 1 book in the catalog initially.
Output Format

Print the updated list of book IDs in sequence from the start to the end of the catalog after the last book has been removed.

Sample Input 0

5
101 102 103 104 105
Sample Output 0

101 102 103 104
Explanation 0

The catalog is initialized with 5 book IDs: 101 102 103 104 105. The last book ID 105 is removed from the end of the catalog. The updated list after deletion is 101 102 103 104.

Sample Input 1

1
701
Sample Output 1

List is empty
Explanation 1

The catalog initially contains one book ID: 701. After removing the last book (701), the list becomes empty.So that print "List is empty"

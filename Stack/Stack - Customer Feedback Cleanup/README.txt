In an online retail platform, customers often leave reviews for products. However, many customers type their feedback with repeated adjacent characters that could make the feedback appear unprofessional. For example, a customer may type: "I loooove this product" or "The proooduct was amazzzingg!!".

To improve the readability and quality of the reviews, the platform's review management system needs to automatically clean up the reviews by removing adjacent duplicate characters.

Your task is to write a program that processes a string containing a review and removes all adjacent duplicate characters, leaving only unique characters in sequence.

For instance, given the review "The proooducttt was amazzzingg", the cleaned review should be "The product was amazing".

Input Format

The first line contains a single string S, representing the customer review.

Constraints

NA

Output Format

Print the string after removing all adjacent duplicate characters.

Sample Input 0

azxxzy
Sample Output 0

ay
Explanation 0

For the input, "azxxzy", removing adjacent duplicates "xx" results in "azzy". After removing "zz", the result is "ay".

Sample Input 1

aaccdd
Sample Output 1

Empty String
Explanation 1

For the input, "aaccdd", removing all adjacent duplicates results in an empty string.

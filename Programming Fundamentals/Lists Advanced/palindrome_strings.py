# On the first line, you will receive words separated by a single space. On the second line, you will receive a palindrome. 
# First, you should print a list containing all the found palindromes in the sequence. 
# Then, you should print the number of occurrences of the given palindrome in the format: "Found palindrome {number} times".


words = input().split(" ")
searched_palindrome = input()
palindromes = []
for el in words:
    if el == "".join(reversed(el)):
        palindromes.append(el)
print(palindromes)
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")

# Using comprehension, write a program that receives some text, separated by space, and take only those words whose length is even. Print each word on a new line.


text = input().split()
even_len = [s for s in text if len(s) % 2 == 0]
print(*even_len, sep="\n")

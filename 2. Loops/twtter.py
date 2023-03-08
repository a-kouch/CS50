"""
When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, 
much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts 
the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
whether inputted in uppercase or lowercase.
"""


#input()
input = input("Input: ")

#make list of vowels
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

output = []
#loop through input
for c in input:
    if c in vowels:
        continue
    else:
        output.append(c)

print("".join(output))

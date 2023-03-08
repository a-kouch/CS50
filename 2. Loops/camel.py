#input for variable in camel case
camel_case = input("Camel case: ")

#empty list to store each letter of string
conversion = []

#loop through string
for c in camel_case:
    #add undercase when uppercase letter appears
    if c.isupper():
        conversion.append("_")
    #add each letter of string to list
    conversion.append(c)

#join the list as a string, print as lowercase
converted = "".join(conversion)
print(converted.lower())

    

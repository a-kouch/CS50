#take str as input

#return string with converted smiley or sadge

def main():
    userInput = input("What do you want to say?")
    if ":)" in userInput:
        replaceSmiley = userInput.replace(":)", "🙂")
    if ":(" in replaceSmiley:
        replaceSad = replaceSmiley.replace(":(", "🙁")
    print(replaceSad)
main()
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()

acceptable_answers = ["42", "forty two", "forty-two"]

if answer in acceptable_answers:
    print("Yes")
else:
    print("No")

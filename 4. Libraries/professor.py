import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        question_score = generate_integer(level)
        if question_score == 1:
            score += 1
            # print(score)
        else:
            continue
            # print(score)

    print(score)
    
def get_level():
    levels = [1, 2, 3]
    while True:
        try:
            level = int(input("Level: "))
            if level in levels:
                return level
        except ValueError:
            level = int(input("Level: "))

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        z = x + y
    elif level == 2:
        x = random.randint(0, 6)
        y = random.randint(0, 6)
        z = x + y
    else:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        z = x + y
    question = (str(x) + " + " + str(y) + " = ")
    for i in range(3):
        answer = input(question)
        try:
            if int(answer) == z:
                return 1
            else:
                print("EEE")
        except:
            pass
 


if __name__ == "__main__":
    main()


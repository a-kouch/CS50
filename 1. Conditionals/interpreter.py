expression = input("Expression: ")

x, y, z = expression.split(" ")

answer = ""

if y == "+":
    answer = float(int(x) + int(z))
elif y == "-":
    answer = float(int(x) - int(z))
elif y == "*":
    answer = float(int(x) * int(z))
elif y == "/":
    answer = float(int(x) / int(z))    
print(answer)

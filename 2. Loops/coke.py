"""Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents 
and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, 
one at a time, each time informing the user of the amount due. 
Once the user has inputted at least 50 cents, output how many cents in change the user is owed. 
Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination."""


# price of coke
remainder = 50


while True:
    #take input and lower remainder    
    paid = input("Insert Coin: ")
    remainder -= int(paid)
    if remainder > 0:
        print("Amount Due: " + str(remainder))
    else:
        print("Change: " + str(remainder * -1))
        break

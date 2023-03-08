from pyfiglet import Figlet
from random import choice
import sys

first_argument = ["-f", "--font"]
figlet = Figlet()

if len(sys.argv) == 1:
    input = input("Input: ")
    figlet.setFont(font=choice(figlet.getFonts()))
    print("Output: \n" + figlet.renderText(input))
elif len(sys.argv) == 3:
    if sys.argv[1] in first_argument and sys.argv[2] in figlet.getFonts():
        input = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print("Output: \n" + figlet.renderText(input))
    else:
        sys.exit("Invalid Usage")
else: 
    sys.exit("Invalid Usage")   


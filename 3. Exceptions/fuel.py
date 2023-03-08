#input for x/y fraction

#output percentage of x/y rounded to nearest int

# if % < 1 print E (empty)

# if % > 99 print(F)

# if x/y not int, prompt again (while True)



def main():
    check_fraction()
    # check_fuel_level()

#function to get input, divide and round result
def get_fraction():
    fraction = input("Fraction:")
    x, y = fraction.split("/")
    z = round(int(x) / int(y) * 100)
    if z <= 1:
        print("E")
    elif z >= 99:
        print("F")
    else: 
        print(f"{z}%")

def check_fraction():
    while True:
        try: 
            get_fraction()
            break
        #catch exceptions for ValueError, ZeroDivisionError
        except ValueError: 
            print("Please input a fraction")
        except ZeroDivisionError:
            print("The fraction cannot be divided by zero")

main()





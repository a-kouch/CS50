
grocery_list = []

while True:
    try:
        item = input("Item: ").upper()
        grocery_list.append(item)
    except EOFError:
        grocery_list.sort()
        for i in range(len(grocery_list)):
            print(i + 1, grocery_list[i])

# grocery_list.sorted().upper()

#add to list
#sort
#capitalise
#print +number 
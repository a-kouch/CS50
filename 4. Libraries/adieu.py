
import inflect
p = inflect.engine()

names = []
while True:
    name = input("Name :")
    names.append(name)
    joined_names = p.join(names)
    print(joined_names)


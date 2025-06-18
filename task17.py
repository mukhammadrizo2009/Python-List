names = []

while True:
    name = input("Ismim kiriting: ")
    if name == "":
        break

    names.append(name)


print(len(names))
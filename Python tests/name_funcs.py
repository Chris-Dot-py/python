def insertName():
    name = input("What is your name?\n -> ")
    print("Hello, " + name + " nice to meet you!\n")
    return name

def checkName(name):
    names = ["Christian", "Kelly", "Joanna", "Giovanni"]
    if name in names:
        print(name + " is in the list!")
    else:
        print(name + " is not in the list :(")

checkName(insertName())

# string methods test
name = "Kelly"
print(name.upper())
name = name.lower()
print(name)

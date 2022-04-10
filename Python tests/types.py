x = "This is a string"
y = 45

def stringOrNot(myVar):
    if not(type(myVar) == type("string")) :
        print("That is not a string!")
    else:
        print("Yes! That is a string!")

stringOrNot(x) # it is a string!
stringOrNot(y) # it is not a string!

def floatOrNot(myVar):
    if type(40.2) != type(myVar):
        print("That is not a float!")
    else:
        print("Yes! That is a float!")

X = 69
Y = 69.69

floatOrNot(X) # not a float!
floatOrNot(Y) # its a float!

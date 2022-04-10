# calendar test
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September"
            ,"October", "Novemebr", "December"]

month = int(input("Which month of the year were you born?\n -> "))
if not (month >= 1 and month < 13):
    print("Error: invalid input\nExiting program . . .")
    exit()

day = int(input("What day of the month was it?\n -> "))
if not (day >= 1 and day < 31):
    print("Error: invalid input\n")
    print("Error: invalid input\nExiting program . . .")
    exit()

year = int(input("What year were you born?\n -> "))

birthday = months[month-1] + " " + str(day) + " " + str(year)
print("Your birth date is ", birthday)
"""
    This is a multi line comment
"""
# this is a single line comment

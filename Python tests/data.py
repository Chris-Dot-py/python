one = 1
two = 2
three = 3
numbers = [one, two,  three]
for x in numbers:
    print(x)

numbers_two = numbers[:]
for x in numbers_two:
    print(x)

print('\n')

min_number = 5
max_number = 98
count = 56
while (count < max_number):
    count = count + 1

if (count == max_number):
    print("count has reached ", max_number)

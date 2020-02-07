# Lists and Loops

the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quaters']

# this loop goes through a list

for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(fruit)

for i in change:
    print(i)

# building list

elements = []

for i in range(0,6):
    print(f"Adding {i} to the list")
    #know more about this function
    elements.append(i)

for i in elements:
    print(i)

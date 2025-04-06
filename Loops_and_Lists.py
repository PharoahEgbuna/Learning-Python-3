the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#the for-loop below iterates through a list. 
for number in the_count:
   print(f"This is count {number}")

#Behaves the same as the loop above.
for fruit in fruits:
   print(f"A fruit of type: {fruit}")

#Here we iterate through a list containing different data types 
for i in change:
   print(f"I got {i}")

#We can create an empty list using closed parentheses
elements = []

#Then we use the range function and append method to add add five numbers to the list  

for i in range(0, 6):
   print(f"Adding {i} to the list.")
   elements.append(i)

#nowwecanprintthemouttoo
for i in elements:
   print(f"The element was:{i}")
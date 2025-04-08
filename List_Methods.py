ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee","Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
  next_one = more_stuff.pop()
  print("Adding:", next_one)
  stuff.append(next_one)
  print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with our stuff.")

print(f"Our second item is {stuff[1]}.")
print(f"Our last item is {stuff[-1]}") 
print(f"Let's remove the last item: {stuff.pop()}")
print("Let's cramp everything together:", end= ' ')
print(''.join(stuff)) 
print("Let's put hashtags between our stuff:", end= ' ')
print('#'.join(stuff[1:5])) 
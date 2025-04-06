i = 0
numbers = []

###While loops will loop repeatedly until a condition is met. 
# It is important to make sure the condition will evenetually be met otherwise it will loop infinitely. 
while i < 6:
   print(f"Atthe topiis{i}")
   numbers.append(i)
   i = i + 1

print("Numbersnow: ", numbers)
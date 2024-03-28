#There are two ways to format strings, either using an f-string (f"string{variable}) or string.format(variable)

types_of_people = 10
x = f"There are {types_of_people} types of people."
print(x)

binary = "binary"
do_not = "don't"
#y is assigned to a string that calls the variables binary and do_not
y = f"Those who know {binary} and those who {do_not}."
print(y)

#Both lines print a string which calls to a variable, and that variable also calls to another variables
print(f"I said: {x}")
print(f"I also said: {y}")

agreement = True
joke_evaluation = "Don't you agree? {}"
print(joke_evaluation.format(agreement))

w = "This is the left side of a string..."
e = "this is the right side of the same string."
#Strings can be added together to be printed one after the other
print(w + e)
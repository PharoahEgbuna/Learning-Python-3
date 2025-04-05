# The escape character (\) can be used to alter the effect of the character that follows it. The escape character is ignored by the compiler
# \t is an escape sequence that causes the string to print indented or tabbed
# \\ is an escape sequence which allow a backslash to appear in the string
tabby_cat = "\tI'm tabbed in"
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat"

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass 
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
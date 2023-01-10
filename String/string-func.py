name = "Adi Venkat loves to code in Python  "
print(f"Spliting: {name.split()}") # Split() - To split value based on spaces.
print(type(name.split()))

print(f"Strip: {name.strip()}") # strip() - To remove right and left spaces.
print(f"R Strip: {name.rstrip()}") # rstrip() - To remove right spaces.
print(f"L Strip: {name.lstrip()}") # lstrip() - To remove right spaces.

print(f"Find: {name.find('loves')}") # find() - To find a particular string in variable.
print(f"Find: {name.find('loves', 12, 20)}") # find('value', from index, to index) - It will search the value from given index to index/

age = "17"
print(f"Is digit: {age.isdigit()}") # isdigit() - To know whether the string in digit or not.

username = "adivenkat65"
print(f"Is alnum: {username.isalnum()}") # isalnum() - To know whether the variable contains alpha numeric contents.

print(f"Is space: {username.isspace()}") # isspace() - To check whether there is space.

print(f"Lower: {name.lower()}") # lower() - Makes every character lowercase in a variable.

print(f"Upper: {name.upper()}") # upper() - Makes every character uppercase in a variable.

print(f"Capitalize: {name.capitalize()}") # capitalize() - Makes 1st character capital.

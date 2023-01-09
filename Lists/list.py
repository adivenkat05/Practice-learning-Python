# If a datatype's individual value can be modified or updated it is known as mutability.
# list stores value in continous memory blocks.

list = [1, 2, 3]
for i in list:
    print(list[i - 1])

print("\n\n")

list[1] = 1
for i in list:
    print(f"after updating: {list[i - 1]}")

# Tuple is immutable compared to list.

tup = (1, 2, 3, 4)

print(tup[1])

single_element = (1,) # Single element tuple (if we remove comma from here, it'll be recognized as integer).

print(type(single_element))

for i in tup:
    print(i)

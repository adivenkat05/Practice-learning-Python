lst = [1, 2, 3, 4, 5]

print(f"Length of lst: {len(lst)}") # len() - To find out length of a list.

print(f"Maximum number: {max(lst)}") # max() - To find out maximum number of a list.

print(f"Minimum number: {min(lst)}") # min() - To find out minimum number of list.

lst.append(6) # append() - To add values to last index of a list.
 
print(f"After appending: {lst}")

lst.insert(0, 0)

print(f"After inserting: {lst}") # insert(index, value) - To insert value in a particular index.

lst.extend([7, 8, 9, 10])

print(f"After extending: {lst}") # extend(value) - To append group of values to list.

lst.remove(0)

print(f"After removing: {lst}") # remove(value) - To remove the first occurence of a value from the list.

lst.pop(9)

print(f"After poping: {lst}") # pop(index) - To remove all the occurence of a value from the list.

lst.sort()

print(f"After sorting: {lst}") # sort() - To arrange values in ascending order.

lst.sort(reverse = True)

print(f"After sorting in reverse: {lst}") # sort(reverse == True) - To arrange values in descending order.


print(f"The data inside variable 'name' is converted into list: {list('Adithyan')}") #list() - To convert group of value into an list.



# READ
f = open("data.txt", 'r') # open('fileName', 'mode') - mode(r) refers to read data.
print(f"f.read(): {f.read()}\n\n") # var.read() - To fetch data from the file.

# WRITE (Overwrite)
f1 = open('data-2.txt', 'w') # open('fileName', 'mode') - mode(w) refers to write data.
f1.write("Written by Python.")

#WRITE (Append)
f1 = open('data-2.txt', 'a') # open('fileName', 'mode') - mode(a) refers to append data.
f1.write("\nAppended.")


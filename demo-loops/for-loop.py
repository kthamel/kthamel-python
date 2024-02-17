x = ["Apple", "Orage", "Banana"]

for i in x:  # This will print all the elements of x list.
    print(i)

###################

x = ["Apple", "Orage", "Banana"]
index = 0
for i in x: # This will print all the elements of x list with index value.
    y = x[index]
    print(index, y)
    index += 1

x = ["Apple", "Orage", "Banana"]

for index, value in enumerate(x): # Using the enumerate funcion, we can get the values from the list as Tuple.
    print(index, value)

###################

x = ["Apple", "Grapes", "Berries", "Orage", "Banana"]
y = range(2, len(x)) # len(x) means, length of the list x.

for i in y: # This will print the elements under the index y.
    print(x[i])


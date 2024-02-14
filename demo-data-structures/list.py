x = [1, 2, 3, 4, 5]

print(x)
print(type(x))

y =x[3] # Y is third element of the list x, let we print y.
print(y)

x[3] = 10 # Replace the third element of list x, from asigning new a value. 
print(x)

x.append(6) # From this we can append a new element to the list x, and will apper in the end of the list.
print(x)

x.insert(3, 100) # From this we can insert element into specific position.
print(x)

x.remove(3) # From this we can remove element. That means it will remove 3 from the list.
print(x)

x.pop(4) # From this we can remove element in specific position.
print(x)

z = [11, 12, 13, 14, "apple"]

zz = x + z # From this way we can add two lists.
print(zz)

print("apple" in zz) # From this way we can check, specific element existing inside a list.
is_apple_in_zz = "apple" in zz # This is much better for this task.
print(is_apple_in_zz)

is_not_apple_in_zz = "apple" not in zz # Can check element is non-existing inside a list.
print(is_not_apple_in_zz)


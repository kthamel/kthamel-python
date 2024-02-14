x = {"Hello", "World", "Hello", "Apple", "100"}

print(x) # Not printing the duplicated elements inside the set.

x.add("Orange") # From this, we can add new element to the sets.
print(x)

x.remove("Apple") # From this, we can remove an element from the sets.
print(x)

y = {"Physics", "Chemistry", "Maths"} # We can use union operator to add two sets. Also, we can use the pipe mark [|] as well.
z = x.union(y)
zz = x | y
print(z)
print(zz)

a = {"Apple", "100"}
zzz = x - a # From this, we can remove all the 'a' elements from set 'x'
print(zzz)


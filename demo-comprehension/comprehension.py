x = [10, 20, 30, 40, 50]

y = x # That means y = x = [10, 20, 30, 40, 50] If, make any changes to y, its reflecting to x as well. 
y.append(60) # From printing the values, can confirm this.

print(y)
print(x)

z = list(x)
z.append(70) # Create list from x and appending values, will be a solution.
print(z)

zz = []

for i in x:      # Also, can do the same thing using a "for loop" like this.
    zz.append(i)

zz.append(80)
print(zz)

## Can do the same thing from one line code ##

zzz = [i for i in x] #This is values returning. That means, "for i in x" is returning the values to i (first letter i)

print(zzz)
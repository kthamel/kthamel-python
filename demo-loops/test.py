x = [10, 20, 30, 40, 50]

total = 0

for i in x:
    total += i

print("Total", total)
print("Average", total/len(x))

max = x[0]
min = x[0]

for i in x:
    if max < i:
        max = i

print("Max", max)

for i in x:
    if min > i:
        min = i

print("Min", min)
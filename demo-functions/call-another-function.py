def even_or_odd (number):
    return "Even" if number % 2 == 0 else "Odd" # This is simple function to define integer is even or odd.

#################

x = [10, 13, 16, 19, 22]
y = []

for i in x:
    y.append(i)

y = [ even_or_odd(i) for i in x] # Here, passing the "for i in x" value into function even_or_odd()
print(y)
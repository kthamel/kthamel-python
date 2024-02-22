def get_odd_numbers(last_integer):
    for i in range(0, last_integer): # Want to get the odd numbers from 0 to 10. 
        if i % 2 == 1:
            return i

get_return_values = get_odd_numbers(5) # Here calling the function, set last_integer as 10.
print(get_return_values)
## From above way, its not returning all the values, cause its returning only one value ##

def get_odd_numbers(last_integer):
    odd_numbers = [] # Here defined a empty list.
    for i in range(0, last_integer): 
        if i % 2 == 1:
            odd_numbers.append(i) # Appending the odd numbers into above defined list.

    return odd_numbers

get_output = get_odd_numbers(10) # Calling the function with input value.
print(get_output)

## This way can fixed the above addressed issue ##

def get_numbers(last_integer):
    odd_numbers = [] # Here defined a empty list for odd values.
    even_numbers = [] # Here defined a empty list for even values.
    for i in range(0, last_integer): 
        if i % 2 == 1:
            odd_numbers.append(i) # Appending the odd numbers into above defined list.
        else:
            even_numbers.append(i)
    return odd_numbers, even_numbers # Appending the even numbers into above defined new list.

get_output = get_numbers(10) # Calling the function with input value.
print(get_output)

## This will print the last output after the calculation, until that its keeping in memory. ##
## It's not a good for large data set, to handle this issue can use generators ##

def get_numbers(last_integer):
    for i in range(0, last_integer):
        if i % 2 == 1:
            print("Odd Number", i)
            yield i # Using yield, we can reduce the memory consumption. Because, its only storing the required value #
                    # at once calling the function. Other than storing the whole data, till the end of manipulation.  #

print("Starting")
x = get_numbers(10)
print("Finish")

for i in x:
    print("Looping", i)

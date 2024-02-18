## Iterate a dictionary ##
set_01 = {        
    "name_01": 10,
    "name_02": 20,
    "name_03": 30
}

for name in set_01:
    age = set_01[name] 
    print(name, age)  # an call the elements of dictionary from this way

# Using the "items()" functionality of a dictionary we can do the same from single line code. It will return the Tuple

for name, age in set_01.items():
    print(name, age)

## Iterate a set ##
    
set_02 = {
    "Apple",
    "Orage",
    "Grapes"
}

for fruit in set_02:
    print(fruit)

## Iterate a tuple ##

set_03 = ("Adam", 180, "Ceylon", 30)

for data in set_03:
    print(data)
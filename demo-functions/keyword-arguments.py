def test_function(**in_values): # Not specify the required arguments for this function. And put ** like this.
    print(in_values)

test_function(name="Adam", city="Lis", age=20) # But want to pass this named parameters. 

print("#################### Task 2 ####################")

## If there is a mandatory input parameter, can check using if condition ##
def test_function(** in_values): 
    if 'name' not in in_values:
        print("Name not found")
    print(in_values)

test_function(name="Adam", city="Lis", age=20)
test_function(city="Lis", age=20)
test_function(name="AdamA", city="Lis", age=20) 

print("#################### Task 3 ####################")

def converting(name, age): # This will convert the dictionary into named arguments.
    print(name, age)

in_values = {
    "name": "Adam",
    "age" : 20
}

converting(** in_values)


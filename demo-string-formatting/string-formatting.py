## Depricated method - String concadination ##
name = "Adam"
age  = 20
msg = "Hello, " + name + " you are " + str(age) + " years old."

print(msg)
## Method 1 - percentage formating ##
## From this way can print the set of strings as one. When the variable count getting more longer, its annoying. ##
msg = "Hello, %s you are %d years old." % (name, age)   # %s <- it means, expecting string in that place.
print(msg)                                              # %d <- it means, expecting decimal in that place.

## Method 2 - format functions - Example 1 ##
name = "Adam"
age  = 20
msg = "Hello, {} you are {} years old.".format(name,age)    # here using the empty {} blocks other than the %. And, use the 
                                                            # format() function to instruct the order of data, that we inserting. 
print(msg)

## Method 2 - format functions - Example 2 ##
name = "Adam"
age  = 20
msg_1 = "Hello, {0} you are {1} years old.".format(name,age) # Also, inside the {} can define it.
print(msg_1)
msg_2 = "Hello, {1} you are {0} years old. {0}.".format(name,age) # And, also able to put like this.
print(msg_2)

## Method 3 - f strings##
name = "Adam"
age  = 20
msg_3 = f"Hello, {name} you are {age} years old."   # In this method just put the one f begin of the string.
print(msg_3)                                        # Also, able to define the varible inside the string like this.


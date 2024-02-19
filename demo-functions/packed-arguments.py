def grd_calc(marks): # Defined one parameter in here.
    total = 0
    for i in marks:
        total += i

    print(total)

score =[10, 20, 30]
    
grd_calc(score) # Passing one value from here.

#################
def grd_calc(*marks): # From * its called packed, Passing values set identified as one value.
    total = 0
    for i in marks:
        total += i

    print(total)

#score =[10, 20, 30]
    
grd_calc(10, 20, 30) # Passing multiple values other than the "score".


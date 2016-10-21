
def month_interpreter_func(val):
    m = ["Jan","Feb","Mar", "Apr","May","Jun","July", "Aug","Sept", "Oct","Nov","Dec"]
    print val
    if val in range(1,13):
        month = m[val-1]
    else: month= "invalid month"
    return month

#function call
#x= month_interpreter(-1)
#print x
#or print month_interpreter(0)

x = [-7, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 55]
m = ["Jan","Feb","Mar", "Apr","May","Jun","July", "Aug","Sept", "Oct","Nov","Dec"]
inx  = 0
minx = 0
while inx < len(x):
    if x[inx] in range(1,13):
       print m[minx]
       minx = minx+1
    else: print "no invalid"
    inx=inx+1
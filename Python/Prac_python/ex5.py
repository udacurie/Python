my_name = 'Zed A. Shaw'
my_age = 35 #not a lie
my_height = 74 #inches
fac_cm = 2.54 #inches to cm factor
#h_cm = my_height*fac_cm
my_weight = 180 #lbs
fac_kg = 0.454 # 1lbs = 0.454kg
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches or %r cm tall." % (my_height, my_height*fac_cm)
print "He's %d pounds heavy or %r kgs heavy." % (my_weight, my_weight*fac_kg)
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "He's got {} eyes and {} hair." .format (my_eyes, my_hair) #new format

print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
import collections

print 'Regular dictionary:'
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print k, v

print '\nOrderedDict:'
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print k, v

	
d1 = {}
d1['a2'] = 'A'
d1['b2'] = 'B'
d1['c2'] = 'C'
d1['d2'] = 'D'
d1['e2'] = 'E'
print '\nMethods 2 for crewating OrderedDict:'
d2 = collections.OrderedDict()
d2.update(d1)
#d2 = d1

for k, v in d1.items():
	print k, v

for k, v in d2.items():
	print k, v
#ssw
	#d2.update(k,v)
	#d2[k] = v
	
 	
	

	
	
# for k, v in d1.items():
	# print k, v
	# d2['k'] = 'v'
#print d2

#for k, v in d2.items():
    #print k, v
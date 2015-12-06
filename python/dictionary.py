# Dictionary , associative arrays or maps
__author__ = 'ssinghal'

tel = {'harry': 4098, 'snape': 4139}

print tel['harry']


for key in tel.keys():
    print "Key : " + key + ", Value : " + str(tel[key])
    print "Key : " + key + ", Value : " , tel[key] ,", note the commas "

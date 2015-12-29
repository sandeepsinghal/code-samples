__author__ = 'ssinghal'

word_counts = {"sandeep" : 7, "sam" : 10, "sid" : 9, "ruby":8}

print word_counts["ruby"]

# Check if a key exists in the dictionary
if "sid" in word_counts:
    print "present"

# Two ways to initialize a dictionary
michaeljordan = { "name" : "Micheal", "surname" : "Jordan", "nick" : "AirJordan", "status" : "Legend", "age" : 50}
michaeljordan_two = dict(name="Micheal",surname='Jordan',nick="AirJordan",status="Legend",age=50)

print michaeljordan

print michaeljordan_two


tel = {'harry': 4098, 'snape': 4139}

print tel['harry']


for key in tel.keys():
    print "Key : " + key + ", Value : " + str(tel[key])
    print "Key : " + key + ", Value : " , tel[key] ,", note the commas "

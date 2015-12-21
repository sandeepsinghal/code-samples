# Demo for list and arrays

# List of strings
names = ["Sandeep", "Ruby", "Sam", "Sid"]

for name in names:
    print name

# Size of the list
print len(names)

# Accessing an element
print "First element is : " + str(names[0])


# Find the words in the list which begin with S and store the lowercase of them
words_filtered = [name.lower() for name in names if name.startswith("S")]
print words_filtered


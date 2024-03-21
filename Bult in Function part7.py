#------Built in Function-----
#enumerate()
#help()
#reversed()
#--------------------------------------


#enumerate(iterable, stsrt=0)
myskill= ["python","HTML","CSS"]
myskillswithcounter = enumerate(myskill,1)
for counter , skill in myskillswithcounter:
    print(f"{counter} - {skill}")

#help()
print(help(print))

#reversed(iterable)
mystring="mozn suliman"
print(reversed(mystring))
for l in reversed(mystring):
    print(l)

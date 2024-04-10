'''
#creating tuples (packing)
address = (7465, "Rosewood dr", "Addison", "AL", 35540)

print(address)
print(address[0], address[1], address[2], address[3], address[4])

#applying for loop on tuple
for i in address:
    print(i,end = " ")

#unpacking
housenumber,street,city,state,zipcode = address
print(housenumber,street,city,state,zipcode)

#a tuple can be created without parentheses
mytuple = 7382, "dublin ireland", 1839
print(mytuple)
'''

#nested tuples
ntuples = ("computers",[492024,"calendar"],("python",40346))
print(ntuples)

print(ntuples[0])
print(ntuples[1])
print(ntuples[2])
print(ntuples[0][4])
print(ntuples[1][1])

mytuple = "p","r","o","g","r","a","m","m","i","n","g"
print(mytuple[:])
print(mytuple[2:7])
print(mytuple[:6])
print(mytuple[8:])

#update tuple
#update not possible
#mytuple[7] = "u"

mytuple = 2,6,3,4,6,4
print(mytuple)

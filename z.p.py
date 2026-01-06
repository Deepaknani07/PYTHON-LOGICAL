from itertools import zip_longest  #this is with using zip_longest using the zip longest function we can add all the values

names = ["kohli","des"]


age = [37]
add = ["delhi","kolar"]
res = list(zip_longest(names,age,add,fillvalue='#'))

print(res)

# this is with using zip function 
# it follows the length of the order of values
names = ["kohli","des"]
age = [37,36]
add = ["delhi","kolar"]
res = list(zip(names,age,add,))

print(res)
print("enter the string:")
str = input()
i =0 
newstr = ''

while(i<=len(str)-1):
    data = str[i]
    if(data == ' '):
        i = i+1
    else:
        newstr = newstr + data
        i= i+1
print(newstr)

#using built in
print("enter the string:")
s =input()
newstr = s.replace(" "," ")
print(newstr)


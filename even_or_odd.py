def even(n:int)->bool:
    return n%2 == 0
if __name__ == "__main__":
    num =int(input("enter the number:"))
    if even(num):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
#this is with using modulus operator

#with simple if else

num = int(input("enter the number:"))        
if num % 2 ==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
    
#with using function

def even(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"
num = int(input("enter the number:"))
print(even(num))
    



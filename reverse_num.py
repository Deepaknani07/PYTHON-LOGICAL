def rev_number(n:int)->int:
    rev = 0
    while n!=0:
        d = n % 10
        rev = d + (rev * 10)
        n = n //10
    return rev

if __name__ == '__main__':
    n = int(input("enter the number:"))
    print(rev_number(n))
    
    
n = int(input("enter the number:"))    
rev = n[::-1]
print("reversed number is :",rev)
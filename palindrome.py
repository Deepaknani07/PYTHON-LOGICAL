def check_palindrome(n:int)->int:
    temp = n
    rev = 0 
    while n !=0:
        d = n % 10
        rev = (rev*10)+d
        n = n//10
    return temp == rev

if __name__ == '__main__':
    n = int(input("enter the number:"))
    if check_palindrome(n):
        print(f"{n} is palindrome")
    else:
        print(f"{n} is not a plaindrome")
        
        
n = input("enter the number:")
if n == n[::-1]:
    print(f"{n} is a palindrome" )
else:
    print(f"{n} is not a palindrome")
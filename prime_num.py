def prime(n:int)->int:
    if n ==1 or n == 0:
        return False
    for i in range(2,(n//2)+1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input("enter the number :"))
    print(prime(n))




def prime(n:int)->int:
    if n ==1 or n == 0:
        return "not a prime"
    for i in range(2,(n//2)+1):
        if n % i == 0:
            return "not a prime"
    return "is a prime"

if __name__ == '__main__':
    n = int(input("enter the number :"))
    print(prime(n))
    


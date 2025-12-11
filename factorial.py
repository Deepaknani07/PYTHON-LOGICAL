def get_factorial(n:int)->int:
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

if __name__ == '__main__':
    n=int(input("enter the number:"))
    print(get_factorial(n))
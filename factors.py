def display_factors(n:int)->int:
    for i in range(1,(n//2)+1):
        if n%i == 0:
            print(i,end=" ")
    print(n)
    
if __name__ == '__main__':
    n = int(input("enter the number:"))
    print(display_factors(n))
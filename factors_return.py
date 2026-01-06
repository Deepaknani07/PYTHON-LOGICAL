def factors_return(n:int)->int:
    count = 0
    for i in range(1,(n//2)+1):
        if n%i == 0:
            count = count+1
    return count

if __name__ == '__main__':
    n = int(input("enter the number:"))
    print(f"the number of factors {n} {factors_return(n)}")
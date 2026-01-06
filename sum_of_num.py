def sumofnum(n:int)->int:
    sum=0
    for i in range(1,n+1):
        sum = sum+i
    return sum
if __name__ == '__main__':
    n = int(input("enter the number:"))
    print(sumofnum(n))
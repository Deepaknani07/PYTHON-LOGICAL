def three(a:int,b:int,c:int):
    return sorted([a,b,c])

if __name__ == '__main__':
    n1 = int(input("enter the number 1:"))
    n2 = int(input("enter the number 2:"))
    n3 = int(input("enter the number 3:"))

    sorted = three(n1,n2,n3)
    print("sorted numbers : ",sorted)
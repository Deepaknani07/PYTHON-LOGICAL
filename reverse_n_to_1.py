def display(n:int)->None:
    i = n
    while i > 0:
        print(i, end=" ")
        i =i-1
if __name__ == '__main__':
    n = int(input("enter the number:"))
    display(n)  
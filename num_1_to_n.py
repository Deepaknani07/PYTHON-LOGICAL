def display(n:int)->None:
    i = 1
    while i<= n:
        print(i, end= " ")
        i =i+1

if __name__ == '__main__':
    n = int(input("enter the number:"))
    display(n)
    

#without builtin
def get_small_number(a:int,b:int,c:int)->int:
    small = a
    if b < small:
        small =b
    if c < small:
        small = c
    return small
if __name__ == '__main__':
    n1 = int(input("enter the number1:"))
    n2 = int(input("enter the number 2:"))
    n3 = int(input("enter th number 3:"))
    print(f"the smallest amoung {n1},{n2} and {n3} are {get_small_number(n1,n2,n3)}")
    
#with built in
def get_small_num(a:int,b:int,c:int)->int:
    return min(a, b, c)
if __name__ == '__main__':
    n1 = int(input("enter the number1 :"))
    n2 = int(input("enter the number2 :"))
    n3 = int(input("enter the number3 :"))
    print(f'the smallest number is{n1},{n2} and {n3} is {get_small_num(n1,n2,n3)}')
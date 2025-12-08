#without using the inbuilt function
def get_big_num(a:int,b:int,c:int)->int:
    if b<a>c:
        return a
    if a<b>c:
        return b
    if b<c>a:
        return c
    
if __name__ == "__main__":
    n1 = int(input("entr the number 1:"))
    n2 = int(input("enter the number2:"))
    n3 = int(input("enter he number 3 :"))
    print(f"the biggest among {n1} {n2} and {n3} is {get_big_num(n1,n2,n3)}")

#with inbuilt function

def get_big_num(a:int,b:int,c:int)->int:
    return max(a,b,c)
if __name__ == "__main__":
    n1 = int(input("enter the number1:"))
    n2 = int(input("enter the number2:"))
    n3 = int(input("enter the number 3:"))
    print(f"the biggest num among 3 is : {n1},{n2} and {n3} is {get_big_num(n1,n2,n3)} ")
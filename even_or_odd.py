def even(n:int)->bool:
    return n%2 == 0
if __name__ == "__main__":
    num =int(input("enter the number:"))
    if even(num):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
        
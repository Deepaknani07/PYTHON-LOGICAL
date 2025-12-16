def is_armstrong(n:int)->bool:
    temp =n
    digits = len(str(n))
    total = 0

    while n > 0:
        d = n % 10
        total += d **digits
        n //= 10

    return total == temp

if __name__ == '__main__':
    num = int(input("enter the number:"))
    if is_armstrong(num):
        print(f"{num} is a armstrong number")
    else:
        print(f"{num} is not a armstrong number")
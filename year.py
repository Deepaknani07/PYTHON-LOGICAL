def is_leap(y: int):
    return (y%4==0 and y%100 !=0) or (y%400 ==0)
if __name__ == '__main__':
    y = int(input("enter the year:"))
    if is_leap(y):
        print(f"{y} is leap ")
    else:
        print(f"{y} is not not leap")
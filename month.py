def is_valid(mon:int)->bool:
    return 0<mon<13

if __name__ == '__main__':
    m = int(input("entert the month :"))
    if is_valid(m):
        print(f"{m} is valid")
    else:
        print(f"{m} is not valid")
        
def get_month(mon: int):
    match mon:
        case 1:
            return "jan"
        case 2:
            return "feb"
        case 3:
            return "mar"
        case 4:
            return "apr"
        case 5:
            return "may"
        case 6:
            return "jun"
        case 7:
            return "jul"
        case 8:
            return "aug"
        case 9:
            return "sep"
        case 10:
            return "oct"
        case 11:
            return "nov"
        case 12:
            return "dec"
        case _:
            return "Invalid month number"

if __name__ == '__main__':
    m = int(input("enter the month number: "))
    print(get_month(m))

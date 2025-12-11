def get_grade(marks:int)->int:
    if 0 < marks and marks>100:
        return "invalid"
    if marks > 89:
        return 'A'
    if marks > 69:
        return 'B'
    if marks > 59:
        return 'c'
    if marks > 49:
        return 'd'
    if marks >34:
        return 'e'
    return 'f'

if __name__ == '__main__':
    marks = int(input("enter the marks:"))
    print(get_grade(marks))
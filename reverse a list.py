def reverse(li: list[int]) -> list[int]:
    r = []
    for i in range(len(li)-1, -1, -1):
        r.append(li[i])
    return r

if __name__ == '__main__':
    li = list(map(int, input("enter the numbers: ").split()))
    print(reverse(li))

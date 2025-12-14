def remove_duplicates(li:list[int])->list[int]:
    res = list()
    for ele in li:
        if ele not in res:
            res.append(ele)
    return res

if __name__ == '__main__':
    l = eval(input("enter the list:"))
    print(remove_duplicates(l))

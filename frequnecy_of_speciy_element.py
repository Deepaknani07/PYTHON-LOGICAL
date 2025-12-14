def get_frequency(li:list[int],target:int)->int:
    count = 0
    for ele in li:
        if ele == target:
            count = count+1
    return count

if __name__ == '__main__':
    l = eval(input("enter the list:"))
    e = eval(input("enter the element:"))
    print(f"the frequency of {e} in {l} is{get_frequency(l,e)}")
            
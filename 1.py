def funcTest1 (lst):
    if type(lst) is not list:
        return print("item is not a list")
    if len(lst) == 0:
        return print("list is empty")
    if not all(type(item) is (int) for item in lst):
        return print("not all elements of type 'int'")
    outputLst = [lst[0]]
    for i in range(len(lst)):
        isItemInLst = lst[i] in outputLst
        if not(isItemInLst):
            outputLst.append(lst[i])
    outputLst = sorted(outputLst)
    return outputLst        
                 

main_lst = [5, 3, 4, 7, 7, 6, 3, 6, 9, 10, 6]

print(funcTest1(main_lst))


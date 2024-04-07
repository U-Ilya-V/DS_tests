def funcTest2 (v1, v2):
    if not((type(v1) is list) and (type(v2) is list)):
        return print("one of the item is not a list")
    if len(v1)  == 0 or len(v2) == 0: 
        return print("one of the vectors is empty") 
    if len(v1) != len(v2):    
        return print("vectors have different length") 
    if all(item == 0 for item in v1) or all(item == 0 for item in v2):
        return print("one of vector is the zero vector")
    if not(all(isinstance(item,(int, float, complex)) for item in v1)) or not(all(isinstance(item,(int, float, complex)) for item in v2)):
        return print("not all elements of number")
    scalarProduct: float = 0
    lenVector1: float = 0
    lenVector2: float = 0
    for i in range(len(v1)):
        scalarProduct = scalarProduct + (v1[i]*v2[i])
        lenVector1 = lenVector1 + (v1[i] ** 2)
        lenVector2 = lenVector2 + (v2[i] ** 2)
    cosDist = 1 - (scalarProduct/((lenVector1 ** 0.5 )*(lenVector2** 0.5 )))
    return cosDist

a = [1, 2.3, 3.6, 4.6j+3]
b = [1.5, 2, 3j+10.6, 6]

print(funcTest2(a,b))


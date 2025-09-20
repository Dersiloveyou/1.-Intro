def difference_lists(a, b):
    set_b = set(b)
    result = []
    for x in a:
        if x not in set_b:
            result.append(x)
    return result

a1 = [1, 2]
b1 = [1]
print(a1, b1, "---", difference_lists(a1, b1)) 
a2 = [1, 2, 2, 3]
b2 = [2]
print(a2, b2, "---", difference_lists(a2, b2))  
a3 = [1, 2, 3]
b3 = [4, 5]
print(a3, b3, "---", difference_lists(a3, b3))  

a4 = [1, 2, 3]
b4 = []
print(a4, b4, "---", difference_lists(a4, b4))

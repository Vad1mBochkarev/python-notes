def main(lst):
    if len(lst) < 2:
        return lst
    
    result = [lst[0]]
    
    for i in range(1, len(lst)):
        if lst[i] != lst[i-1]: 
            result.append(lst[i])

    x = (len(lst) - len(result))

    for i in range(x):
        result.append('_')
    
    return result
xyi = [0, 0, 1, 2, 2, 2, 2, 3, 4, 5, 5, 6, 6, 6, 6, 7, 7, 8]
print(main(xyi))


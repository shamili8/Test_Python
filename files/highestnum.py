#find a highest number in list

def highest_num(n):
    list1 = [9, 3, 5, 1, 6, 7,9,9]
    list2 = list(set(list1))
    list2.sort()
    return list2[-n]
print(highest_num(2))



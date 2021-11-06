def merge_array(lst1,lst2):
    ind1 = 0
    ind2 = 0
    lst3 = [] * (len(lst1) + len(lst2))
    for i in range(min(len(lst1) , len(lst2))):

        if lst1[ind1] < lst2[ind2]:
            lst3.append(lst1[ind1])
            ind1 += 1

        else:
            lst3.append(lst2[ind2])
            ind2 += 1
    return lst3


if __name__ == '__main__':
    print(merge_array([1,3,5],[2,4,6]))
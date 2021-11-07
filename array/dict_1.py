def sum_of_dict(dict):
    list = []
    for i in dict:
        list.append(dict[i])
    add = sum(list)
    return add

if __name__ == '__main__':
    dict = {'a' : 1, 'b' : 2, 'c' : 3}
    print(sum_of_dict(dict))
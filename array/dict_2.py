def merge_dict(dict1, dict2):
    return (dict2.update(dict1))
if __name__ == '__main__':
    dict1 = {'a' : 10, 'b' : 20}
    dict2 = {'c' : 30, 'd' : 40}
    print(merge_dict(dict1, dict2))
    print(dict2)
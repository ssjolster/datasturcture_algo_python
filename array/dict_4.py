if __name__ == '__main__':
    my_dict = {}
    for i in [6, 7, 6, 8, 9, 18]:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    print(my_dict)
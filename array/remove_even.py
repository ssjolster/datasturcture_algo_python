def remove_even(lst):
    odd = []
    for number in lst:
        if number % 2 != 0:
           odd.append(number)
    return odd

if __name__ == '__main__':
    print(remove_even([1,2,3,4,5]))

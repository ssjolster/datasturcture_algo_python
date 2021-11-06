def array_shift(lst, k):
    rotate = []
    k = 0 if len(lst) == 0 else k % len(lst)

    for number in range(len(lst) - 1, len(lst)):
        rotate.append(lst[number])

    for number in range(0, len(lst)):
        rotate.append(lst[number])
    return rotate


if __name__ == '__main__':
    print(array_shift([1, 2, 3, 4, 5], 2))

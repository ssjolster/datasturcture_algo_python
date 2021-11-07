if __name__ == '__main__':
    number_of_shoe = int(input())
    shoe_size = list(map(int, input().split(",")))
    number_of_customer = int(input())
    cost = 0
    for i in range(number_of_customer):
        size, price = list(map(int, input().split(" ")))
        if shoe_size[size]:
            cost = cost + price
            shoe_size[size] = shoe_size[size] - 1
    print(cost)

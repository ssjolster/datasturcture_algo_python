if __name__ == '__main__':
    number_of_shoe = int(input())
    shoe_size = list(map(int, input().split(",")))
    shoe_size_count = {}
    for shoe_size in shoe_size:
        if shoe_size in shoe_size_count:
            shoe_size_count[shoe_size] += 1
        else:
            shoe_size_count[shoe_size] = 1

    number_of_customer = int(input())
    cost = 0
    for i in range(number_of_customer):
        size, price = list(map(int, input().split(" ")))
        if size in shoe_size_count and shoe_size_count[size] >= 1:
            cost = cost + price
            shoe_size_count[size] = shoe_size_count[size] - 1
    print(cost)
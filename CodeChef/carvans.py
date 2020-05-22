n = int(input())
for j in range(n):
    no_cars = int(input())
    car_list = list(map(int, input().split()))
    if no_cars == 1:
        max_speed = 1
    stop = no_cars - 1
    max_speed = 0
    temp = car_list[0]
    for i in range(no_cars):
        if car_list[i] <= temp:
            max_speed += 1
            temp = car_list[i]
    print(max_speed)


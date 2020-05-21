n = int(input())
max_speed = 0
for j in range(n):
    no_cars = int(input())
    car_list = input().split(' ')
    if no_cars == 1:
        max_speed = 1
    stop = no_cars - 1
    for i in range(stop):
        print('---->',car_list[stop-i], car_list[stop-i-1], i+1)
        last_item = no_cars
        if car_list[stop-i-1] > car_list[stop-i]:
            print(car_list[stop-i-1], car_list[stop-i])
            max_speed += 1
    print(max_speed)


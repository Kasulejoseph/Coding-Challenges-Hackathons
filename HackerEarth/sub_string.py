from time import time, sleep
start_time = time()
n, k , m = input()
s = str(input())

s_array = list(s)
only_transformed = []
transformed_dict = dict()

def generate_sub_strings():
    start_range = stop_range = n
    string_combination = []
    while start_range > 0:
        start_range -= k
        sub_string = map(int, [s_array[a] for a in range(start_range, stop_range)])
        stop_range -= k
        string_combination.append(sub_string)
    return string_combination
    
def update_ones_while_sum_lessthan_m(list_of_items, i):
    list_of_items = list_of_items[0]
    for key, item in enumerate(list_of_items):
        if(list_of_items[item] == 1 and sum(list_of_items) > m):
            list_of_items[item] = 0
            transformed_dict[i] = list_of_items
            only_transformed.append(list_of_items)

def transfrom_array(reversed_sub, only_transformed, i):
    list_of_items= [value for i, value in reversed_sub.items()]
    if sum(list_of_items[0]) > m:
        update_ones_while_sum_lessthan_m(list_of_items, i)
    else:
        transformed_dict[i] = list_of_items[0]


# print(generate_sub_strings()[::-1])

reversed_sub = generate_sub_strings()[::-1]
for i in range(len(reversed_sub)):
    dic_reversed_sub = {i: reversed_sub[i]}
    transfrom_array(dic_reversed_sub, only_transformed, i)

transformed_list = [value for x, values in transformed_dict.items() for value in values]
count = len(only_transformed)
transformed = ''.join(str(x) for x in transformed_list)
end_time = time()

print(count)
print(transformed)
print(end_time-start_time)




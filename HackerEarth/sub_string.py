n, k , m = input()
s = str(input())

s_array = list(s)
sub_string = map(int, s_array[:k])
reminder_String = map(int, s_array[k:])
only_transformed = []
transformed_list = []

def generate_sub_strings():
    start_range = stop_range = n
    string_combination = []
    while start_range > 0:
        start_range -= k
        print(start_range)
        sub_string = map(int, [s_array[a] for a in range(start_range, stop_range)])
        stop_range -= k
        string_combination.append(sub_string)
    return string_combination

def transfrom_array(sum_of_sub_string, reversed_sub, only_transformed):
    for i, value in reversed_sub.items():
        print('i, x', i, value)
        for x, y in enumerate(value):
            print('x, y', x,y )
            if(value[y] == 1):
                while sum_of_sub_string > m:
                    print(value)
                    value[y] = 0
                    transformed_list.insert(i, value)
                    only_transformed.append(value)
                    break
            # print('reversed_sub', reversed_sub)




# print(generate_sub_strings()[::-1])
transformed = []
reversed_sub = generate_sub_strings()[::-1]
for i in range(len(reversed_sub)):
    sum_of_sub_string = sum(reversed_sub[i])
    dic_reversed_sub = {i: reversed_sub[i]}
    transfrom_array(sum_of_sub_string, dic_reversed_sub, only_transformed)

print('count', only_transformed)
print('transformed_list', transformed_list)


# sum_of_sub_string = sum(sub_string)
# count = 1
# reversed_sub = sub_string[::-1]

# transformed = reversed_sub[::-1] + reminder_String
# print(count)
# print(''.join(str(x) for x in transformed))




# if ():
#     print('yes')

# print(sub_String)


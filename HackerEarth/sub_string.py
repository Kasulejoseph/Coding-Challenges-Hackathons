n, k , m = input()
s = str(input())

s_array = list(s)
sub_string = map(int, s_array[:k])
reminder_String = map(int, s_array[k:])
only_transformed = []
transformed_dict = dict()

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
    yy = [value for i, value in reversed_sub.items()]
    print('yy',yy , i)
    if sum(yy[0]) > m:
        for x, y in enumerate(yy[0]):
            if(yy[0][y] == 1):
                while sum(yy[0]) > m:
                    # print('iiiiii', i)
                    yy[0][y] = 0
                    transformed_dict[i] = yy[0]
                    only_transformed.append(yy[0])
                    print('transformed_dict[i]', transformed_dict[i])
                    if(i != i):
                        print('iiiiii', i)
                    break
    else:
        transformed_dict[i] = yy[0]



# print(generate_sub_strings()[::-1])
transformed = []
reversed_sub = generate_sub_strings()[::-1]
for i in range(len(reversed_sub)):
    sum_of_sub_string = sum(reversed_sub[i])
    dic_reversed_sub = {i: reversed_sub[i]}
    transfrom_array(sum_of_sub_string, dic_reversed_sub, only_transformed)

yy = [value for x, values in transformed_dict.items() for value in values]
print('count', only_transformed)
print('transformed_list', ''.join(str(x) for x in yy))



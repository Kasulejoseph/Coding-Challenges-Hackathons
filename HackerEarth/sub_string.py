n, k , m = input()
s = str(input())

s_array = list(s)
sub_string = map(int, s_array[:k])
reminder_String = map(int, s_array[k:])

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

print(generate_sub_strings()[::-1],)

sum_of_sub_string = sum(sub_string)
count = 1
reversed_sub = sub_string[::-1]

for i, x in enumerate(reversed_sub):
    if(reversed_sub[i] == 1):
        while sum_of_sub_string > m:
            count +=1
            reversed_sub[i] = 0
            sum_of_sub_string = sum(reversed_sub)
            break
transformed = reversed_sub[::-1] + reminder_String
print(count)
print(''.join(str(x) for x in transformed))




# if ():
#     print('yes')

# print(sub_String)


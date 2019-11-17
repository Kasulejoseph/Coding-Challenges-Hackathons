try:
    name = input()
    if len(name) > 20:
        print('length should be less than 20')
    name_list = name.split('z')
    isZoos = 'yes' if(len(name_list[-1]) == 2 * len(name_list[:-1])) else 'No'

    print(isZoos)
except:
    print('something went wrong')



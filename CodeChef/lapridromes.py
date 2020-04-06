# cook your dish here
T = int(input())
for _ in range(T):
    string = input()
    if len(string) % 2 == 0:
        s1 = string[:(len(string) // 2)]
        s2 = string[len(string) // 2:]
        if sorted(s1) == sorted(s2):
            print('YES')
        else:
            print('NO')

    if len(string) % 2 == 1:
        mid_item = (len(string) + 1) // 2
        s1 = string[:mid_item - 1]
        s2 = string[mid_item:]
        if sorted(s1) == sorted(s2):
            print('YES')
        else:
            print('NO')


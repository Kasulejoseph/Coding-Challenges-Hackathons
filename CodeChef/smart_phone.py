# cook your dish here
T = int(input())
maximum = 0
p_list = []
for i in range(T):
    p_list.append(int(input()))
p_list.sort(reverse=True)

for x in range(T):
    maximum = max(maximum, p_list[x] * (x + 1))
print(maximum)

# Use dynamic programing for this problem.
# Runs in 0(n^2)


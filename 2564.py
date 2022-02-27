N = int(input())
lst = list(map(int, input().split()))
len_1 = 1   # 증가하는
len_2 = 1   # 감소하는
max_len = 1
for i in range(1, N):
    if lst[i] > lst[i-1]:
        len_1 += 1
        len_2 = 1
        if len_1 > max_len:
            max_len = len_1
    elif lst[i] < lst[i-1]:
        len_1 = 1
        len_2 += 1
        if len_2 > max_len:
            max_len = len_2
    else:
        len_1 += 1
        len_2 += 1
        if len_1 > max_len:
            max_len = len_1
        if len_2 > max_len:
            max_len = len_2

print(max_len)
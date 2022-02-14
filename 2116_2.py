N = int(input())
ans = 0
tot = 0

lst = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, 7):
    next_under_num = i
    for idx in range(N):
        under_num_idx = lst[idx].index(next_under_num)
        lst_05 = [lst[idx][1], lst[idx][2], lst[idx][3], lst[idx][4]]
        lst_13 = [lst[idx][0], lst[idx][2], lst[idx][4], lst[idx][5]]
        lst_24 = [lst[idx][0], lst[idx][1], lst[idx][3], lst[idx][5]]

        if under_num_idx == 0:
            upper_num_idx = 5
            tot += max(lst_05)
        if under_num_idx == 5:
            upper_num_idx = 0
            tot += max(lst_05)
        if under_num_idx == 1:
            upper_num_idx = 3
            tot += max(lst_13)
        if under_num_idx == 3:
            upper_num_idx = 1
            tot += max(lst_13)
        if under_num_idx == 2:
            upper_num_idx = 4
            tot += max(lst_24)
        if under_num_idx == 4:
            upper_num_idx = 2
            tot += max(lst_24)

        next_under_num = lst[idx][upper_num_idx]
    if tot > ans:
        ans = tot
    tot = 0

print(ans)
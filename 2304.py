N = int(input())

input_lst = [list(map(int, input().split())) for _ in range(N)]
max_x = max(input_lst) # x 끝점
max_height_lst = max(input_lst, key=lambda x: x[1])
max_idx, max_height = max_height_lst[0], max_height_lst[1] # 최고점 좌표/ 높이

lst = [0]*(max_x[0]+1)

for sets in input_lst:
    lst[sets[0]] = sets[1]

tmp_max = 0
for i in range(max_idx):
    if lst[i] > tmp_max:
        tmp_max = lst[i]
    lst[i] = tmp_max

tmp_max = 0
for j in range(len(lst)-1, max_idx, -1):
    if lst[j] > tmp_max:
        tmp_max = lst[j]
    lst[j] = tmp_max

print(sum(lst))

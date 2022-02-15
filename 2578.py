# from pprint import pprint

N = 5
lst = [list(map(int, input().split())) for _ in range(N)]

call = []
for _ in range(N):
    call += list(map(int, input().split()))
# pprint(lst)
# print(call)

cnt = 0
for num in call:
    for i in range(N):
        for j in range(N):
            if num == lst[i][j]:
                lst[i][j] = 0
                cnt += 1
                break
    # 리스트 체크
    # print(f'#{cnt}')
    # pprint(lst)
    bingo = 0
    sum_rd, sum_ld = 0, 0
    for k in range(N):
        sum_x, sum_y = 0, 0
        for p in range(N):
            sum_x += lst[k][p]
            sum_y += lst[p][k]
            # print(sum_x, sum_y)
        if sum_x == 0:
            bingo += 1
        if sum_y == 0:
            bingo += 1
    # print(bingo)
    for idx in range(N):
        sum_rd += lst[idx][idx]
        sum_ld += lst[idx][-(idx+1)]
        # print(sum_rd, sum_ld)
    if sum_rd == 0:
        bingo += 1
    if sum_ld == 0:
        bingo += 1
    # print(bingo)
    if bingo >= 3:
        break
print(cnt)

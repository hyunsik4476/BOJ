def dicefind(idx, num, tot):
    global ans
    if tot > ans:
        ans = tot
    if idx == N:
        return


    check = lst[idx].index(num) # 밑면에 깔릴 수의 인덱스

    lst_05 = [lst[idx][1], lst[idx][2], lst[idx][3], lst[idx][4]]
    lst_13 = [lst[idx][0], lst[idx][2], lst[idx][4], lst[idx][5]]
    lst_24 = [lst[idx][0], lst[idx][1], lst[idx][3], lst[idx][5]]

    if check == 0:
        dicefind(idx+1, lst[idx][5], tot+max(lst_05))
    if check == 5:
        dicefind(idx+1, lst[idx][0], tot + max(lst_05))

    if check == 1:
        dicefind(idx+1, lst[idx][3], tot+max(lst_13))
    if check == 3:
        dicefind(idx+1, lst[idx][1], tot + max(lst_13))

    if check == 2:
        dicefind(idx+1, lst[idx][4], tot+max(lst_24))
    if check == 4:
        dicefind(idx+1, lst[idx][2], tot + max(lst_24))

N = int(input())

ans = 0
lst = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, 7):
    dicefind(0, i, 0)
print(ans)



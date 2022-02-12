lst = [[0]*100 for _ in range(100)]
sq_1 = list(map(int, input().split()))
sq_2 = list(map(int, input().split()))
sq_3 = list(map(int, input().split()))
sq_4 = list(map(int, input().split())) # x1 x2 y1 y2
ans = 0

for y in range(sq_1[1], sq_1[3]):
    for x in range(sq_1[0], sq_1[2]):
        if lst[y][x] == 0:
            lst[y][x] = 1
            ans += 1

for y in range(sq_2[1], sq_2[3]):
    for x in range(sq_2[0], sq_2[2]):
        if lst[y][x] == 0:
            lst[y][x] = 1
            ans += 1

for y in range(sq_3[1], sq_3[3]):
    for x in range(sq_3[0], sq_3[2]):
        if lst[y][x] == 0:
            lst[y][x] = 1
            ans += 1

for y in range(sq_4[1], sq_4[3]):
    for x in range(sq_4[0], sq_4[2]):
        if lst[y][x] == 0:
            lst[y][x] = 1
            ans += 1

print(ans)
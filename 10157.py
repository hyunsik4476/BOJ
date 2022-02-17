x, y = map(int, input().split())
K = int(input())
if K > x*y:
    print(0)
else:
    #2(x+y)-4 -> x-2, y-2
    idx = 1
    tot = 1
    while tot <= K:
        tot += 2*(x+y)-4
        x -= 2
        y -= 2
        idx += 1
    idx -= 1
    tot = tot - (2*(x+y)+4)
    x += 2
    y += 2

    # (idx, idx) 에서 시작, 위로 +y-1, 우로 +x-1, 아래로 -y+1, 좌로 -x+2
    start = [idx, idx]
    if tot == K:
        print(idx, idx)
    for y1 in range(1, y):
        start[1] += 1
        tot += 1
        if tot == K:
            print(*start)
            break

    for x1 in range(1, x):
        start[0] += 1
        tot += 1
        if tot == K:
            print(*start)
            break

    for y2 in range(1, y):
        start[1] -= 1
        tot += 1
        if tot == K:
            print(*start)
            break

    for x2 in range(1, x-1):
        start[0] -= 1
        tot += 1
        if tot == K:
            print(*start)
            break

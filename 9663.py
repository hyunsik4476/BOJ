def nq(stx, sty, dia_r = [], dia_l = []):
    global cnt
    if (stx - sty) in dia_r:
        return
    if (stx + sty) in dia_l:
        return
    if sty >= N-1:
        cnt += 1
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            nq(i, sty+1, dia_r + [stx - sty], dia_l + [stx + sty])
            visited[i] = 0


N = int(input())

visited = [0]*N
cnt = 0
for x in range(N):
    visited[x] = 1
    nq(x, 0)
    visited[x] = 0
print(cnt)
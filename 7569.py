from collections import deque


def bfs():
    visited = [[[0] * M for _ in range(N)] for _ in range(H)]
    day = 0
    size = 0
    while q:
        x, y, h = q.popleft()
        size += 1
        for dx, dy, dh in [[0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0], [0, 0, 1], [0, 0, -1]]:
            nx, ny, nh = x+dx, y+dy, h+dh
            if M > nx >= 0 and N > ny >= 0 and H > nh >= 0 and visited[nh][ny][nx] == 0 and arr[nh][ny][nx] == 0:
                q.append((nx, ny, nh))
                visited[nh][ny][nx] = visited[h][y][x] + 1
                day = visited[nh][ny][nx]
    if size == M*N*H - cnt:
        return day
    else:
        return -1


M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# arr[h][y][x]
q = deque()
cnt = 0
for k in range(H):
    for j in range(N):
        cnt += arr[k][j].count(-1)
        for i in range(M):
            if arr[k][j][i] == 1:
                q.append((i, j, k)) # x, y, h
ans = bfs()
print(ans)
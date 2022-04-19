from collections import deque


def bfs():
    visited = [[0]*M for _ in range(N)]
    day = 0
    size = 0
    while q:
        x, y = q.popleft()
        size += 1
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx, ny = x+dx, y+dy
            if M > nx >= 0 and N > ny >= 0 and visited[ny][nx] == 0 and arr[ny][nx] == 0:
                q.append((nx, ny))
                visited[ny][nx] = visited[y][x] + 1
                day = visited[ny][nx]
    if size == M*N - cnt:
        return day
    else:
        return -1


M, N = map(int, input().split())    # 가로, 세로
arr = [list(map(int, input().split())) for _ in range(N)]
# 1 : 익은 토마토 0 : 안익은토마도, -1 : 빈칸
# 시작 0일, 모두 익을때까지 걸리는 날짜 출력
q = deque()
for j in range(N):
    for i in range(M):
        if arr[j][i] == 1:
            q.append((i, j))
cnt = 0
for k in range(N):
    cnt += arr[k].count(-1)
ans = bfs()
print(ans)
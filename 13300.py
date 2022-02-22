N, K = map(int, input().split()) # 사람 수, 방 인원
dct = dict()
for _ in range(N):
    s, y = map(int, input().split())
    dct[(s,y)] = dct.get((s,y), 0) + 1

ans = 0

for num in dct.values():
    if num%K:
        ans += num//K + 1
    else:
        ans += num//K

print(ans)

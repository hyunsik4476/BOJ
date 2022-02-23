N = 9
lst = [int(input()) for _ in range(N)]
ans = []
done = 0

for i in range(1<<9):
    cnt = 0
    tot = 0
    for j in range(9):
        if i & (1<<j):
            cnt += 1
            tot += lst[j]
    if cnt == 7 and tot == 100:
        done = 1
        for k in range(9):
            if i & (1<<k):
                ans.append(lst[k])
    if done:
        break

ans.sort()
for num in ans:
    print(num)
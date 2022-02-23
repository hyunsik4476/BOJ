N = int(input())
stu = []
lst = list(map(int, input().split()))
for i in range(N):
    stu.append(i+1)
    stu = stu[:i-lst[i]] + [stu[i]] + stu[i-lst[i]:i] + stu[i+1:]

print(*stu)
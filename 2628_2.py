x, y = map(int, input().split())
N = int(input())
lst_x = [0, x]
lst_y = [0, y]

for _ in range(N):
    a, b = map(int, input().split())
    if a == 0:
        lst_y.append(b)
    else:
        lst_x.append(b)

lst_x.sort()
lst_y.sort()

dx = []
dy = []
for i in range(1, len(lst_x)):
    dx.append(lst_x[i] - lst_x[i-1])
for j in range(1, len(lst_y)):
    dy.append(lst_y[j] - lst_y[j - 1])

max_area = max(dx)*max(dy)
print(max_area)
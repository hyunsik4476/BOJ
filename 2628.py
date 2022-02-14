x, y = map(int, input().split())
n = int(input())
input_list = [list(map(int, input().split())) for _ in range(n)]
lst_x = [0]+[lst[1] for lst in input_list if lst[0] == 0 and lst[1] < y]+[y]
lst_y = [0]+[lst[1] for lst in input_list if lst[0] == 1 and lst[1] < x]+[x]

for i in range(len(lst_x)-1):
    min_idx = i
    for j in range(i+1, len(lst_x)):
        if lst_x[j] < lst_x[min_idx]:
            min_idx = j
    lst_x[i], lst_x[min_idx] = lst_x[min_idx], lst_x[i]
lst_y.sort()

new_x = []
new_y = []
for k in range(len(lst_x)-1): # lst[1]-lst[0]
    new_x.append(lst_x[k+1] - lst_x[k])
for l in range(len(lst_y)-1): # lst[1]-lst[0]
    new_y.append(lst_y[l+1] - lst_y[l])

max_xy = 0
for x_1 in new_x:
    for y_1 in new_y:
        if x_1*y_1 > max_xy:
            max_xy = x_1*y_1
print(max_xy)
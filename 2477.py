N = int(input())
input_lst = [list(map(int, input().split())) for _ in range(6)]
input_lst.append(input_lst[0])
print(input_lst)

# 1, 2 가로 3, 4 세로 4->2->3->1->4
sub_area = 0
for i in range(len(input_lst)-1):
    if input_lst[i][0] == 4 and input_lst[i+1][0] == 1:
        sub_area = input_lst[i][1]*input_lst[i+1][1]
    elif input_lst[i][0] == 1 and input_lst[i + 1][0] == 3:
        sub_area = input_lst[i][1] * input_lst[i + 1][1]
    elif input_lst[i][0] == 3 and input_lst[i + 1][0] == 2:
        sub_area = input_lst[i][1] * input_lst[i + 1][1]
    elif input_lst[i][0] == 2 and input_lst[i + 1][0] == 4:
        sub_area = input_lst[i][1] * input_lst[i + 1][1]

lst_x = [lst[1] for lst in input_lst if lst[0] == 1 or lst[0] == 2]
lst_y = [lst[1] for lst in input_lst if lst[0] == 3 or lst[0] == 4]
full_area = max(lst_x)*max(lst_y)

print((full_area-sub_area)*N)

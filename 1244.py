def man(num_input, num):
    for idx in range(num_input):
        if (idx + 1) % num == 0:
            s_lst[idx] = 0 if s_lst[idx] else 1


def woman(num_input_2, num, cnt):
    cnt += 1
    if num - cnt < 0 or num + cnt == num_input_2:
        s_lst[num] = 0 if s_lst[num] else 1
        return

    if s_lst[num - cnt] != s_lst[num + cnt]:
        s_lst[num] = 0 if s_lst[num] else 1
        return

    if s_lst[num - cnt] == s_lst[num + cnt]:
        s_lst[num - cnt] = 0 if s_lst[num - cnt] else 1
        s_lst[num + cnt] = 0 if s_lst[num + cnt] else 1
        woman(num_input_2, num, cnt)


N = int(input())
s_lst = list(map(int, input().split()))
M = int(input())  # 사람의 수
lst = [0] * M
for i in range(M):
    lst[i] = map(int, input().split())

for j in range(M):
    a, b = lst[j]
    if a == 1:
        man(N, b)
    else:
        woman(N, b - 1, 0)

answer = ''
for k in range(N):
    answer = answer + str(s_lst[k]) + ' '
    if (k + 1) % 20 == 0:
        answer = answer + '\n'

print(answer)

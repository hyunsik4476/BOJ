# 100 60 40 20...

def fn(N, num, cnt): # 입력, 뺄 수
    global ans, num_minus, i
    if cnt > ans:
        ans = cnt
        num_minus = i
    if N < 0:
        return

    new_N = N - num
    if new_N < 0:
        return
    fn(num, new_N, cnt+1)

def fn2(N2, num2, cnt2):
    if N2 < 0:
        return
    new_N2 = N2 - num2
    if new_N2 < 0:
        return
    lst.append(new_N2)
    fn2(num2, new_N2, cnt2+1)

N = int(input())
ans = 0
num_minus = 0
i = 0
for _ in range(N+1):
    fn(N, i, 0)
    i += 1
lst = [N, num_minus]

print(ans+2)

fn2(N, num_minus, 0)
print(*lst)
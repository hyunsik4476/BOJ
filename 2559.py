N, K = map(int, input().split()) # 리스트 요소 수, 연속된 날짜의 수

lst = list(map(int, input().split()))+[0]

tmp_sum = sum(lst[:K])

max_sum = tmp_sum
for i in range(N-K+1):
    if tmp_sum > max_sum:
        max_sum = tmp_sum
    tmp_sum = tmp_sum - lst[i] + lst[i+K]
print(max_sum)
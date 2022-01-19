'''
자기 자신과 각 자릿수의 합으로 셀프 넘버 만들고
셀프 넘버가 아닌 수 출력하기

set 두 개를 만들고 집합 빼기를 하려다
방향을 바꿈
'''

def self_num(n):
    ans = n
    strs = str(n)
    for num in strs:
        ans += int(num)
    return ans

self_num_set = set()
# full_set = set(range(1,11))
for idx in range(1, 10001):
    if self_num(idx) < 10001: 
        self_num_set.add(self_num(idx))

    if idx not in self_num_set:
        print(idx)


# ans_set = full_set - self_num_set

# for idx in range(1, 11):
'''
자기 자신과 각 자릿수의 합으로 셀프 넘버 만들고
10001 셀프 넘버가 아닌 수 출력하기

set 두 개를 만들고 집합 빼기를 하려다
복잡한 것 같아 방향을 바꿈
'''
'''
테스트를 위해 
self_num 함수 다른 시도
line 30의 if 문은 어떻게 하는 게 좋을지 모르겠음
'''

# def self_num(n):
#     ans = n
#     strs = str(n)
#     for num in strs:
#         ans += int(num)
#     return ans

def self_num(n):
    for num in str(n):
        n += int(num)
    return n

self_num_set = set()
# full_set = set(range(1,11))

for idx in range(1, 101):
    #if self_num(idx) < 11: 
    self_num_set.add(self_num(idx))

    if idx not in self_num_set:
        print(idx)

# ans_set = full_set - self_num_set
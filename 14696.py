N = int(input())
for tc in range(N):
    dct_a = dict()
    dct_b = dict()
    a = list(map(int, input().split()))[1:]
    b = list(map(int, input().split()))[1:]
    for num in a:
        dct_a[num] = dct_a.get(num, 0) + 1
    for num in b:
        dct_b[num] = dct_b.get(num, 0) + 1

    for num in [4,3,2,1]:
        if dct_a.get(num, 0) > dct_b.get(num,0):
            print('A')
            break
        if dct_a.get(num, 0) < dct_b.get(num,0):
            print('B')
            break
    else:
        print('D')
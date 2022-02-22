w, h = map(int, input().split())
x, y = map(int, input().split())
time_limit = int(input())

t_x = ((time_limit-(w-x))%(2*w))
t_y = ((time_limit-(h-y))%(2*h))
if t_x <= w:
    ans_x = w - t_x
if t_x > w:
    ans_x = t_x - w

if t_y <= h:
    ans_y = h - t_y
if t_y > h:
    ans_y = t_y - h

print(ans_x, ans_y)
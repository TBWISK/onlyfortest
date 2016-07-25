# coding:utf-8
total = 0
a = 1
N = 10
for i in range(1, N):
    if i % 2 == 0:
        # print i
        total -= i
    else:
        total += i
    # print i
print total

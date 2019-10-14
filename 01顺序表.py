# 17 + 2 + 6
#
# 26 + 3 + 6
#
# 26 2
#
# 13 0
# 6 1
# 3 0
# 1 1
#   1
#
# 10001
# 00010
#
# 11010
# 00011
#


# [1]  O(1)
# [1,2,3,4,5,6] O(6)
#
# [1,2,3,4,5……n]   O(n)
#
# O(n**2)
# O(n**3)
# O(logN)
# O(nlogn)
#
# 2**n
# for

# a+b+c =1000  且a**2 + b**2 = c**2  求出所有的a,b,c 组合（a,b,c为自然数)
import time

# start = time.time()
# for a in range(1001):
#     for b in range(1001):
#         for c in range(1001):
#             if a**2 +b**2 == c**2 and a+b+c == 1000:
#                 print(f'a={a},b={b},c={c}')
#
# end = time.time()
# print(end-start)

#
#
# start = time.time()
# for a in range(1001):
#     for b in range(1001-a):
#         c = 1000-a-b
#         if a**2+b**2==c**2:
#             print(f'a={a},b={b},c={c}')
#
# end = time.time()
# print(end-start)
#





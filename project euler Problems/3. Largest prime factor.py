# This is my code took too long to verify.
# N = 600851475143
# count = 0
# mx = 0
# z = round(N/3)
# for i in range(3, z):
#     for a in range(2, i):
#         if i % a == 0:
#             count = count + 1
#             if count > 2:
#                 break
#     if N % i == 0:
#         mx = i
#     count = 0
# print(mx)

n = 600851475143
p = 2

while n > 1:
    if n % p == 0:
        while n % p == 0:
            n /= p
        largest = p
    p += 1

print(largest)  # 6857K




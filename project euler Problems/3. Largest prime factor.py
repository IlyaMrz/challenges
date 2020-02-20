N = 600851475143
count = 0
mx = 0
for i in range(3, N):
    for a in range(2, i):
        if i % a == 0:
            count = count + 1
    if count < 2 and N % i == 0:
        mx = i
    count = 0
print(mx)





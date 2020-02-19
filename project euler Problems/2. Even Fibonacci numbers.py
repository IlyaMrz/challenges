F = [1 , 2]
x = 0
z = 2
while x < 4000000:
    x = F[-1] + F[-2]
    if x % 2 == 0:
        z = z + x
    F.append(x)
print(z)
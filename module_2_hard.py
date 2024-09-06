import random
a = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
r = random.choice(a)
b = []
for i in range(1, 21):
    for j in range(1, 21):
        if r % (i + j) == 0 and i < j and (i + j) != 0:
            b.append(str(i))
            b.append(str(j))
print( r, "=", "".join(b))
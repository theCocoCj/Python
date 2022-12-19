import random

f = open("casuali.txt", "w")

l_Ali = [random.randint(1,6) for _ in range(10)]
l_Bob = [random.randint(1,6) for _ in range(10)]

for a,b in zip(l_Ali, l_Bob):
    f.write(f"{a},{b}")

f.close()


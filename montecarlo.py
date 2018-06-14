import random
import math

iteration = 10000
total = 0

for i in range(1,iteration) :
    x = random.random()
    y = random.random()

    dist = math.sqrt(x * x + y * y)

    if dist <= 1 :
        total = total + 1

#aire cercle = pi * r * r (ici r = 1)
#aire quart cercle = pi / 4
pi = float(total) / float(iteration) * 4.0

print(pi)


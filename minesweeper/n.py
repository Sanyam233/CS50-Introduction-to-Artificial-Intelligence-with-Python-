import random
import itertools
# a = {(2,3), (5,4), (6,7)}

# print(random.choice(tuple(a)))

a = []

# a = [1,2,3,4,5,6]

# for i, j in itertools.combinations(a, 2):
#     print(i, j)

for i in range(5):
    b = []
    for j in range(5):
        b.append(j)
    
    a.append(b)

cell = (3,3)

cells = []

for i in range(cell[0] - 1, cell[0] + 2):
    for j in range(cell[1] - 1, cell[1] + 2):
        if(i, j) == cell:
            continue
        else:
            if((i > 0 and i < 5) and (j > 0 and j < 5)):
                cells.append((i, j))

print(a)
print(cells)
matrix = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 0]
]

temp = matrix

MarkovMatrix = [[0.0 for _ in range(len(temp[0]))] for _ in range(len(temp))]

print(matrix)

print(temp)

print(MarkovMatrix)
print(len(MarkovMatrix))

print(matrix + temp)

for i in range(len(temp)):
    cnt = 0
    for j in range(len(temp[0])):
        if temp[i][j] != 0:
            cnt += 1
    for k in range(len(temp)):
        if temp[i][k] != 0:
            MarkovMatrix[k][i] = 1 / cnt

print(MarkovMatrix)

length = len(temp)
PR = [1 / length for _ in range(length)]
print(PR)

# ##############################################################
#                     单元测试论文引用的连接矩阵
# ##############################################################

from Matrix import build_paper_matrix

matrix = build_paper_matrix()

for i in range(0, len(matrix)):
    for j in range(0, len(matrix)):
        print(matrix[i][j], end=' ')
    print()

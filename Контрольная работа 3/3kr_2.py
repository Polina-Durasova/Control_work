"""2. Дан массив N × M. Требуется повернуть его по часовой стрелке на 90 градусов.
Входные данные
На первой строке даны натуральные числа N и M (1 ≤ N, M ≤ 50). На следующих N строках записано по M
неотрицательных чисел, не превышающих 109 – сам массив.
Выходные данные
Выведите повернутый массив в формате входных данных.
"""

n, m=map(int,input().split())
matrix=[]
for i in range(n):
    row=input().split()
    for i in range(len(row)):
        row[i]=int(row[i])
    matrix.append(row)

matrix_two=[]
for i in range(m):
    n_mat_one=n-1
    row=[]
    for j in range(n):
        row.append(matrix[n_mat_one][i])
        n_mat_one-=1
    matrix_two.append(row)
for i in range(m):
    for j in range(n):
        print(matrix_two[i][j],sep="", end=" ")
    print()





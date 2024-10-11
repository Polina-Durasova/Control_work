"""1. Даны числа n и m. Создайте массив A[n][m] и заполните его змейкой (см. пример).
Входные данные
Программа получает на вход два числа n и m.
Выходные данные
Программа должна вывести полученный массив
"""

n, m=map(int,input().split())
matrix=[]
counter=0
for i in range(n):
    row=[]
    if i%2==0:
        for j in range(m):
            row.append(counter)
            counter+=1
    else:
        counter2=counter+m-1
        for j in range(m):
            row.append(counter2)
            counter2-=1
            counter+=1
    matrix.append(row)

for i in range(n):
    for j in range(m):
        print(matrix[i][j],sep="", end=" ")
    print()
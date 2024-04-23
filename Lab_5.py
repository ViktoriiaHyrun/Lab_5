import random
n = 5
m = 5
mas1 = []
i=j=int()
for i in range(n):
    mas1.append([0] * m)
for i in range(n):
    for j in range(m):
        mas1[i][j] = random.randint(-50, 50)
print("Matrix A(5,5):")
for row in mas1:
    print(row)
sum_above_diagonal = 0
for i in range(n):
    for j in range(m):
        if i < j:  
            sum_above_diagonal += mas1[i][j]
print("The sum of elements above the main diagonal:", sum_above_diagonal)

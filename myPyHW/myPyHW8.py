#求一个3*3矩阵中对角线上元素之和
lst = [
    [3, 5, 6],
    [4, 7, 8],
    [2, 4, 9]
]
sum=0
for i in range(3):
    sum += lst[i][i]
print(sum)
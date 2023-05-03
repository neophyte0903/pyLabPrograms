#rows=int(input("enter number of rows"))
size1=int(input("size"))
size2=int(input("size of 2nd matrix"))
#cols=int(input("enter number of columns"))

Matrix1=[]
Matrix2=[]


for i in range (size1):
    row=[]
    for j in range(size1):
        row.append(int(input("enter values first matrix")))
    Matrix1.append(row)
#first matrix
print(Matrix1)

for p in range (size2):
    row2=[]
    for q in range(size2):
        row2.append(int(input("enter values second matrix ")))
    Matrix2.append(row2)
#second matrix2
print(Matrix2)


# multiplication

resultMatrix=[]

for i in range(size1):
    resultRow=[]
    for j in range(size1):
        resultRow.append(0)
    resultMatrix.append(resultRow)



for i in range(len(Matrix1)):
    for j in range(len(Matrix2[0])):
        for k in range(len(Matrix2)):
            resultMatrix[i][j]+=Matrix1[i][k]*Matrix2[k][j]

print(resultMatrix)
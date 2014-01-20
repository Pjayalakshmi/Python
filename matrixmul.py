a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[3,6,7],[1,2,3],[7,3,2]]
c=0
for i in range(3):
for j in range(3):
 for k in range(3):
 c+=a[i][j]*b[j][i]
 print(" ",c,end=' ')
print()

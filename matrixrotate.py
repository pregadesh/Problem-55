#Rotate 90 degrees clockwise (matrix)
def esh (mat):
  n = len(mat)
  res = [[i]* n for i in range(n)]
  for i in range(n):
    for j in range(n):
      res[j][n-i-1] = mat[i][j]
  for i in range(n):
    for  j in range(n):
      mat[i][j] = res[i][j]
  return res
mat = [[1,2,3],[4,5,6],[7,8,9]]
esh(mat)
for num in mat :
  print(" ".join(map(str,num))

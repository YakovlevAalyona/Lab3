m=input("row")
n=input("col")
X=[]
for i in range (m):
    m1=[]
    for j in range (n):
        m1.append(input("num"))
    X.append(m1)
Y=[]
for i in range (m):
    n1=[]
    for j in range (n):
        n1.append(input("num"))
    Y.append(n1)


result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
  
   for j in range(len(Y[0])):
       
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
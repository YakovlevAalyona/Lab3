from random import randint

a = [[col for col in range(7)] for row in range(7)]
for i in a:
    print(i)
for row_index, row in enumerate(a):
    for col_index in range(row_index, len(row)):
        tmp = a[col_index][row_index]  
        a[col_index][row_index] = row[col_index]
        a[row_index][col_index] = tmp

print(numpy.array(a))
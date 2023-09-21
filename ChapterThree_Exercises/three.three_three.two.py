a = b = 7
print('a =', a, '\nb =', b)
c ,d =1,2
print('c =', c, '\nd =', d)


for row in range(10):
    for column in range(10):
        print(row if row % 2 == 1 else column, end='')
        print()

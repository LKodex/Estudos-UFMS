'''
1. Imprima a seguinte figura:
*
**
***
****
*****
******
*******
'''

SIZE = 7

for i in range(1, SIZE + 1):
    for j in range(i):
        print('*', end='')
    print()

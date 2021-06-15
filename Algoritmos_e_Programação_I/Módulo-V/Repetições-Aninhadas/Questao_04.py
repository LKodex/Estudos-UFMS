'''
4. Para um dado inteiro positivo n, imprima n linhas como no exemplo a seguir, que considera n = 7.
1 = 1
1 +2 = 3
1 +2 +3 = 6
1 +2 +3 +4 = 10
1 +2 +3 +4 +5 = 15
1 +2 +3 +4 +5 +6 = 21
1 +2 +3 +4 +5 +6 +7 = 28
'''

n = 7

aux = 0
for i in range(1, n + 1):
    aux += i
    print(1, end=' ')
    for j in range(2, i + 1):
        print(f'+{j}', end=' ')
    print(f'= {aux}')

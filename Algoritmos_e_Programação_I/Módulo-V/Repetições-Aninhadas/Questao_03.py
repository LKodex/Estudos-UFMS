''' 
3. Para um dado inteiro positivo n, imprima n linhas como no exemplo a seguir, que considera n = 7.
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
1 2 3 4 5 6 7
'''

n = 7

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

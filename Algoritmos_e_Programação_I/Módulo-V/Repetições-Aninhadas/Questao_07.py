'''
7. Para um dado inteiro positivo n, imprima n linhas como no exemplo a seguir, que considera n = 5.
                +
            +       +
        +       +        +
    +       +       +        +
+       +       +        +       +

'''

n = 5

for i in range(1, n + 1):
    for j in range(n, i, -1):
        print('   ', end='')
    for j in range(1, i + 1):
        print('+', end='     ')
    print()

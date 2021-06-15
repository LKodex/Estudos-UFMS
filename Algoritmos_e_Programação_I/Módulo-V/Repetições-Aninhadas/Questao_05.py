'''
5. Para um dado inteiro positivo n, imprima n linhas como no exemplo a seguir, que considera n = 10.
1
    2
        3
            4
                5
                    6
                        7
                            8
                                9
                                    10
'''

n = 10

for i in range(1, n + 1):
    for j in range(1, i):
        print('    ', end='')
    print(i)

'''
6. Para um dado inteiro positivo n, imprima n linhas como no exemplo a seguir, que considera n = 10.
                                    10
                                9
                            8
                        7
                    6
                5
            4
        3
    2
1
'''

n = 10

for i in range(n, 0, -1):
    for j in range(1, i):
        print('    ', end='')
    print(i)

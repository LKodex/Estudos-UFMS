'''
2. Para um dado inteiro positivo n, imprima um figura como no exercício anterior, sendo que a primeira linha da figura tem 1 *, a segunda linha tem 2 *, a terceira linha tem 3 * e assim até a linha n, que deverá conter n * .
'''

def readInt():
    while True:
        try:
            return int(input())
        except:
            print('ERRO! Digite um número inteiro!')

n = readInt()

for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    print()

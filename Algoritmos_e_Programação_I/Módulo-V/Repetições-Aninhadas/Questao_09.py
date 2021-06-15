'''
9. Para cada inteiro no intervalo [m, n], sendo m e n inteiros e m < n, apresente a lista dos seus divisores.
'''

def readInt():
    while True:
        try:
            return int(input())
        except:
            print('ERRO! Digite um número inteiro!')

m = readInt()
n = readInt()

while m >= n:
    print(f'Digite um número maior que {m}:', end=' ')
    n = readInt()

for i in range(m, n + 1):
    listaAUX = list()
    for j in range(1, i + 1):
        if i % j == 0:
            listaAUX.append(j)
    print(f'Os divisores de {i} são: {listaAUX}')

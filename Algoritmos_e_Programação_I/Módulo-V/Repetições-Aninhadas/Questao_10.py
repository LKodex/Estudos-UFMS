'''
10. Liste os números primos existentes no intervalo [m, n], sendo m e n inteiros positivos e m < n.
'''

def readInt():
    while True:
        try:
            return int(input())
        except:
            print('ERRO! Digite um número inteiro!')

m = readInt()
while m < 0:
    print('Digite um número inteiro maior que 0:', end=' ')
    m = readInt()

n = readInt()
while n <= m:
    print(f'Digite um número inteiro maior que {m}:', end=' ')
    n = readInt()

numerosPrimos = list()
for i in range(m, n + 1):
    listaAUX = list()
    for j in range(1, i + 1):
        if i % j == 0:
            listaAUX.append(j)
    if len(listaAUX) == 2:
        numerosPrimos.append(i)

print(f'Os números primos do intervalo [{m}, {n}] são: {numerosPrimos}')

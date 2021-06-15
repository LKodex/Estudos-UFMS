'''
12. Leia um valor inteiro n e, em seguida n valores inteiros positivos. Para cada inteiro lido k, apresente o seu fatorial. A impressão do resultado deve acontecer apenas ao final da leitura dos dados informados pelo usuário.
'''

def readInt():
    while True:
        try:
            return int(input())
        except:
            print('ERRO! Digite um número inteiro!')

def fatorial(num):
    if num <= 1:
        return 1
    return num * fatorial(num - 1)

n = readInt()
while n <= 0:
    print('Digite um número maior que 0:', end=' ')
    n = readInt()

listaNumeros = list()
listaFatoriais = list()
for i in range(1, n + 1):
    k = readInt()
    listaNumeros.append(k)
    listaFatoriais.append(fatorial(k))

for i in range(len(listaNumeros)):
    print(f'O fatorial de {listaNumeros[i]} é = {listaFatoriais[i]}')

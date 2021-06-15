'''
11. Leia um valor inteiro n e, em seguida n valores inteiros positivos. Para cada inteiro lido k, apresente apenas os que são múltiplos de 3. A impressão do resultado deve acontecer apenas ao final da leitura dos dados informados pelo usuário.
'''

def readInt():
    while True:
        try:
            return int(input())
        except:
            print('ERRO! Digite um número inteiro!')

n = readInt()
while n <= 0:
    print('Digite um número inteiro maior que 0:', end=' ')
    n = readInt()

multiplosDe3 = list()

for i in range(1, n + 1):
    k = readInt()
    if k % 3 == 0:
        multiplosDe3.append(k)

if len(multiplosDe3) == 1:
    print(f'O único valor multiplo de 3 digitado é: {multiplosDe3}.')
elif len(multiplosDe3) > 0:
    print(f'Os valores digitados múltiplos de 3 são: {multiplosDe3}.')
else:
    print('Não existe nenhum múltiplo de 3 nos números digitados.')
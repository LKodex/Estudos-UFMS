'''
8. Para cada inteiro no intervalo [101, 276] apresente a lista dos seus divisores.
'''

intervaloInicio = 101
intervaloFim = 276

for i in range(intervaloInicio, intervaloFim + 1):
    listaAUX = list()
    for j in range(1, i + 1):
        if i % j == 0:
            listaAUX.append(j)
    print(f'Os divisores de {i} são: {listaAUX}')

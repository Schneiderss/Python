n = str(input('Digite um número de 0 a 9999: '))
k = '00'+n
print('Unidades: {}'.format(k[-1]))
print('Dezenas: {}'.format(k[-2]))
print('Centena: {}'.format(k[-3]))
print('Milhar: {}'.format(k[-4]))
n = input('Digite algo: ')
print('O tipo primitivo desse valor é: ' , type(n))
print('É um número: {}'.format(n.isnumeric()))
print('É letra: {}'.format(n.isalpha()))
print('Está em maiúsculo: {}'.format(n.isupper()))
print('Está em minúsculo: {}'.format(n.islower()))
print('Está um trem: {}'.format(n.istitle()))

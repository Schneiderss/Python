print('Quantos litros de tinta para pintar a sua parede!')
l = float(input('Qual a largura da sua parede em metros? '))
a = float(input('Qual é a altura da sua parede em metros? '))
r = l*a/2
print('Litros de tinta que você irá necessitar: {}'.format(r),'litros')
print('A área da sua parede é: {} m²'.format(l*a))
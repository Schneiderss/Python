from math import floor
v = float(input('Quantos km/h você estava? '))
l = floor(v)
if l >= 80:
    print('Você foi multado! O valor será de R${}'.format((l-80)*7))
    print('Você estava acima da velocidade permitida, que é 80km/h')
else:
    print('Parabéns! Você tem uma direção defensiva')
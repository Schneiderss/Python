from random import randint
from time import sleep
n = randint(0,5)
k = int(input('Escolha um número de 0 a 5 e veja se você acertou o número que o computador escolher: '))
print('Processando...')
sleep(2)
if k == n:
    print('Parabéns, você é uma maquina!')
else:
    print('Péssimo!')
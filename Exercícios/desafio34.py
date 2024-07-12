sal = float(input('Digite o seu salário: '))
if sal>1250.00:
    print('Seu aumento é: {:.2f}'.format(sal*1.1))
else:
    print('Seu aumento é de: {:.2f}'.format(sal*1.15))
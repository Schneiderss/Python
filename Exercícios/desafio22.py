nome = str(input('Digite o seu nome: ')).strip()
n = nome.strip()
print('Seu nome em maiúsculo:',n.upper())
print('Seu nome em minúsculo:',n.lower())
k = n.split()
l = ''.join(k)
print('Quantas letras há no seu nome:',len(l))
print('Número de letras do primeiro nome:',len(k[0]))
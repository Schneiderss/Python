n = str(input('Digite o nome da sua cidade: '))
k = n.lower()
j = k.strip()
l = j.split() 
print('Sua cidade começa com Santo?','santo' in l[0])
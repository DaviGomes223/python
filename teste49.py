cont = 0
resposta = 0
tabuada = int(input('Digite um número para ver sua tabuada: '))
for i in range(1, 11):
    cont += 1
    resposta = tabuada * cont
    print('{} x {:2} = {}'.format(tabuada, cont, resposta))
    
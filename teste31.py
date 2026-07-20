KM = int(input('Digite a distancia da sua viagem: '))
D = float
if KM <= 200:
    D = KM * 0.50
else:
    D = KM * 0.45
print('Voce esta prestes a fazer uma viagem de {}Km '.format(KM))
print('E o preço da sua passagem sera de R${} '.format(D))
#importando a classe veiculo para o  meu main

from veiculo import Veiculo

caminhao_rosa = Veiculo('rosa','6','Ford','80')

print(caminhao_rosa)
print(type(caminhao_rosa))

print ('CAMINHÂO ROSA')
print('cor:',caminhao_rosa.cor)
print('Marca:',caminhao_rosa.marca)
print('Quantidade de Rodas:',caminhao_rosa.rodas)
print('Quantidade de Litros por Tanque:',caminhao_rosa.tanque)

print("")
carro_azul = Veiculo('Azul',4,'BMW',45)
print('CARRO AZUL')
print('cor:',carro_azul.cor)
print('Marca:',carro_azul.marca)
print('Qunatidade de Rodas:',carro_azul.rodas)
print('Quantidade de Litros por Tanque:', carro_azul.tanque)
carro_azul.load (10)
print('Quantidade de Litros por Tanque:', carro_azul.tanque)

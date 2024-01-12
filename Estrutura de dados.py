minha_lista = ['Gui', 'Joao']  # LISTA (List)
minha_tupla = ('Gui', 'Joao')  # TUPLA (Tuple)
meu_dicionario = {'nome': 'Guilherme', 'Idade': 27} # DICONARIO (dict)
meu_conjunto = {'Gui', 'Joao'}  #CONJUNTO (set) nao pode ter dois itens iguais

#Como Iniciar vazios
#lista = []
#tupla = ()
#dicionario = []
#conjunto = set()

#Podemos agrupar lista com Tuplas e conjuntos
#loucura = [(1,2), (3,4), (5,6), ({'Joao', 'maria'},{'Gabriel'})]
#print(loucura)


''' no Conjunto ele e mais rapido e faz a busca mais rapida ,Lista nao e feita para fazer busca
     ja o conjunto e uma tabela HASH  
if 'Gui' in meu_conjunto:
    print ('Foi encontrado dentro do conjunto')
'''

''' Podemos acrescentar os dados no conjunto como segue abaixo como ele tamem tem uma busca rapida 
podemos usar o remove 

meu_conjunto.add('Maria')
meu_conjunto.add('Gui')
mu_conjunto.remove('Gui')
print(meu_conjunto)
'''


''' Podemos acrescentar mais dados na nossa lista podemos tambem remover ocmo clear
meu_dicionario['endereco'] = 'Av.Loao Cabral de melo Neto'
meu_dicionario['Telefone'] = '(81)99999-0999'
meu_dicionario['Ponto de Referençia'] = 'Ladeira de da escola simon Bolivar'
print(meu_dicionario)
'''

#podemos alterar tambem os valroes nas posicoes com o comando abaixo pode colocar numeros tambem
#meu_dicionario ['idade'] = 'Joao'
#print (meu_dicionario)

#Imprime valores dentro do Dicionario
#for valores in meu_dicionario.values():
#    print (valores)

''' verifica o valor dentro do dicionario  e imprime o valor Guilherme 
if 'Guilherme' in meu_dicionario.values():
    print('Guilherme esta no dicionario')
'''
# saber o tamanho com o len
#print (len (meu_dicionario))

'''perguntar se Gui esta dentro da minha tupla
if 'Gui' in minha_tupla:
    print('Gui esta dentro da minha lista')
'''
#imprimir tupla
# print (minha_tupla[1])

'''passar o for para imprimir somento o nome  como dado em parametro
 posso passar tambem [] para pegar somente as letras de uma tupla
 posso passar tambem os valores de dois ou mais nomes com o parametr [],[] e assim sucessivamente

for nome in minha_tupla:
    print(nome[1],[1])
'''
#Podemos subsitituir a tupla toda tambem porem nao podemos substituir somente um valor temos que passar ela toda
#minha_tupla= ('Joao','Fabricio')
#print(minha_tupla)

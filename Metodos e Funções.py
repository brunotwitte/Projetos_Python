# Aula de metodos e funções

#funcao soma  eu posso ficar usand a funcao soma
'''def soma (numero1,numero2):
   resp =  numero1 + numero2
   return resp
retorno =  soma(12.35,75.4)
print(retorno)
'''
'''
Funcao de imprimir varias vezes com a funcao def 
def imprimi_oi():
    print("OI")
imprimi_oi()
imprimi_oi()
imprimi_oi()
imprimi_oi()
'''
'''Funcao de impressao infinita 
def imprimi_oi():
    print("OI")
while True:
    imprimi_oi()
'''
''' Usanod a funcao para  condicional if de leitura de letras e condional de numeros
def tem_sete_letras(argumentos):
    if len(argumentos) == 7:
        return True
    else:
        return  False
print (tem_sete_letras('OIPesso'))
'''
'''
Funcao para impressao e checagem se tem 7 letras
def tem_sete_letras(argumentos):
    if len(argumentos) == 7:
      return True
    else:
        return False

if tem_sete_letras('1234567'):
     print("realmente tem sete Letras")







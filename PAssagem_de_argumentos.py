import sys

argumentos = sys.argv   #arg1 metod // arg2  - n1  // arg3 - n2
# Podemos ussar para passar argumentos  executando o aquivo pelo comando com a funcao soma e funcao subtracao
# isso serve para passar exemplo  soma   123 espaco tecla espaco 123 vai trazr o valor de 246 e podemos colocar outras
#funcoes e podemos acrescentar multiplicacao e sbtracao isso serve para escrever menos.


def soma(n1, n2):
  return n1 + n2

def sub(n1, n2):
    return n1 - n2

if argumentos [1]== "soma":
   resp = soma(float(argumentos[2]),float (argumentos[3]))
elif argumentos[1] == "sub":
    resp = sub(float(argumentos[2]),float (argumentos[3]))
print (resp)

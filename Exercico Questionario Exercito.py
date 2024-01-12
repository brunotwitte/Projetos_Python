'''
exercico aula 3
Faca um programa que pergunte a idade, o peso e a altura de uma pessoa e decida se ela est apta a ser
do exercito ,para entrar no exercito e preciso ter mais de 18 anos, pesar mais de 60 kilos
e medir maior ou igual a  1.70
'''

idade = int (input ("Digite sua idade:"))
altura = float  (input('Digite sua altura:'))
peso = float (input('Digite seu Peso:'))


if idade >= 18 and peso >=60 and  altura >= 1.70:
    print ('Voce esta nos Padroes das forcas Armadas ')
else:
    print ('Voce nao pode servir as Forcas Armadas  ')




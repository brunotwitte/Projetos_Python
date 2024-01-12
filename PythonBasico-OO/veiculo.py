from itertools import takewhile


class Veiculo():


 # ele passa ele mesmo como o this no java init ele quem constroi ele mesmo
 # temos tres argumentos dentro deles
    def __init__(self, cor, rodas, marca, tanque):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque

    def load(self, litros):
        self.tanque += litros


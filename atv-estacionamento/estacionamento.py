class Veiculo():
    def __init__(self, placa):
        self.placa = placa
        self.estacionado = False

    def estacionar(self):
        self.estacionado = True
        return f'{self.tipo} {self.placa}'
        
    def sair_da_vaga(self):
        self.estacionado = False
        return f'{self.tipo} {self.placa}'
        

class Carro(Veiculo):
     def __init__(self, placa):
        super().__init__(placa)
        self.tipo = 'carro'    

class Moto(Veiculo):
    def __init__(self, placa):
        super().__init__(placa)
        self.tipo = 'moto'


class Vaga():
    def __init__(self, tipo):
        self.id = [1,2,3,4,5,6,7,8,9,10]
        self.placas = []
        self.tipo = tipo
        self.livre = 10
        
    def ocupar(self, tipo, placa): 
        self.tipo = tipo
        if len(self.placas) < 10:
            self.placas.append(placa)
            self.livre -= 1
            print(f'{self.tipo} estacionado com sucesso!')
        else:
            for i in self.placas:
                if i == 'vago':
                    i_ocupa = self.placas.index(i)
                    self.placas.remove('vago')
                    self.placas.insert(i_ocupa, placa)
                    self.livre -= 1
                    

    def desocupar(self, tipo, placa):
        self.tipo = tipo
        if placa in self.placas:
           i_descocupa = self.placas.index(placa)
           self.placas[i_descocupa] = 'vago'
           self.livre += 1
           print(f'{self.tipo} desocupado com sucesso!')
          
class Estacionamento(Vaga):
    def __init__(self):
        super().__init__(self)
        self.vagas_de_carro = 5
        self.vagas_de_moto = 5
        self.carro_para_vaga = 5
        self.moto_para_vaga = 5
        self.total_vagas_livres_carro = 5
        self.total_vagas_livres_moto = 5

    def estacionar_carro(self, Carro):
        if self.total_vagas_livres_carro == 0:
            print('Não há mais vagas para carro')

        elif Carro.tipo == 'carro' and self.total_vagas_livres_carro > 0: 
            self.ocupar(Carro.tipo, Carro.placa)
            self.total_vagas_livres_carro -= 1
            self.carro_para_vaga -= 1

        elif Carro.tipo == 'moto' and self.total_vagas_livres_moto == 0:
            self.ocupar(Carro.tipo, Carro.placa)
            self.total_vagas_livres_carro -= 1
            self.carro_para_vaga -= 1
        else:
            print('Ainda há vagas exclusivas para motos disponíveis.')
                  
    def estacionar_moto(self, Moto):
        if(Moto.tipo == 'carro'):
            print('Não permitido, vagas exclusivas para motos.')
        elif(self.total_vagas_livres_moto == 0):
             print('Não há mais vagas exclusivas para motos.')
        elif(self.total_vagas_livres_moto <= 5):
            self.ocupar(Moto.tipo, Moto.placa)
            self.total_vagas_livres_moto -= 1
            self.moto_para_vaga -= 1

    def remover_carro(self, Carro):
        self.desocupar(Carro.tipo, Carro.placa)
        self.total_vagas_livres_carro += 1
        self.carro_para_vaga += 1

    def remover_moto(self, Moto):
        if Moto.tipo == 'carro':
            print('Não tem o tipo "carro" estacionado aqui, só motos.')
        else:
            self.desocupar(Moto.tipo, Moto.placa)
            self.total_vagas_livres_moto += 1
            self.moto_para_vaga += 1

    def estado_do_estacionamento(self):
        dict_exibir_estacionados = dict(zip(self.id, self.placas))
        print('\n\n  *** Estadado do Estacionamento ***')
        print('\nId da vaga + placas cadastradas:\n  ',
                            dict_exibir_estacionados)

        print(f'\nTotal de Vagas Excusivas para Carros: {self.vagas_de_carro}')
        print(f'Total de Vagas Exclusivas para Motos: {self.vagas_de_moto}')
        print(f'\nTotal de Vagas Livres: {self.livre}')
        print(f'Total de Vagas Livres para Carros: {self.total_vagas_livres_carro}')
        print(f'Total de Vagas Livres para Motos: {self.total_vagas_livres_moto}')
        print(f'\nTotal de Carro para vagas: {self.carro_para_vaga}')
        print(f'Total de Moto para vagas: {self.moto_para_vaga}\n')
        
estacionamento = Estacionamento()

carro1 = Carro('KJK')
carro2 = Carro('LLL')
carro3 = Carro('BBB')
carro4 = Carro('OOO')
carro5 = Carro('QQQ')
carro6 = Carro('NNN')

moto1 = Moto('AAA')
moto2 = Moto('HHJ')
moto3 = Moto('WWZ')
moto4 = Moto('RRX')
moto5 = Moto('KKK')
moto6 = Moto('ÇÇÇ')

estacionamento.estacionar_carro(carro1)
estacionamento.estacionar_carro(carro2)
#estacionamento.estacionar_carro(carro3)
#estacionamento.estacionar_carro(carro4)
#estacionamento.estacionar_carro(carro5)

estacionamento.estacionar_moto(moto1)
estacionamento.estacionar_moto(moto2)
#estacionamento.estacionar_moto(moto3)
#estacionamento.estacionar_moto(moto4)
#estacionamento.estacionar_moto(moto5) 

estacionamento.estado_do_estacionamento()

estacionamento.remover_carro(carro1)

#estacionar.remover_carro(carro2)
#estacionamento.remover_moto(moto5)

#estacionamento.estacionar_carro(carro6)

estacionamento.estado_do_estacionamento()
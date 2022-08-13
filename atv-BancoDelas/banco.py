class Banco:
    def __init__(self):
        self.titular = []
        self.telefone = []
        self.renda_mensal = []
        self.sexo = []
        
    def criar_conta(self, nome, telefone, renda_mensal,sexo):
        self.titular.append(nome)
        self.telefone.append(telefone)
        self.renda_mensal.append(renda_mensal)
        self.sexo.append(sexo)

    def adicionar_mais_titular(self, nome, telefone, renda_mensal,sexo):
        self.titular.append(nome)
        self.telefone.append(telefone)
        self.renda_mensal.append(renda_mensal)
        self.sexo.append(sexo)

    def imprimir_comprovante(self):
        print('\nConta corrente criada com sucesso!')
        print(f'Titular(es): {self.titular}')   
        print('**Nossas clientes MULHERES terão direito a um cheque especial no valor igual a sua renda mensal.\nPara adquirir solicite em .adquirir_cheque_especial**\n')


class ContaCorrente(Banco):
    def __init__(self):
        super().__init__()
        self.saldo = 0
        
    def adquirir_cheque_especial(self, Banco):
        if 'masculino' in Banco.sexo:
            print('O cheque especial é exclusivamente para as mulheres.')
        else:
            valor = sum(Banco.renda_mensal) / len(Banco.renda_mensal)
            self.saldo += valor
            print(f'Você tem direito ao cheque especial com valor igual a sua renda R$ {valor}')
            
    def verifica_saldo(self):
        print(self.saldo)
                
    def depositar(self, valor):
        self.saldo += valor
        print(f'Adicionado o valor {valor} na sua conta com sucesso!')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque no valor de R$ {valor} realizado com sucesso! ')
        else:
            print("Esse valor ultrapassa o limite")

    def imprimir_comprovante(self, Banco):
         print('\nEXTRATO DA CONTA')
         print(f'Titular(es): {Banco.titular}')
         print(f'Saldo: {self.saldo}\n')


b1 = Banco()
b1.criar_conta("Bianka", 986014831, 800, 'feminino')
b1.adicionar_mais_titular("Mario", 986014831, 400, 'masculino')
b1.imprimir_comprovante()
c1 = ContaCorrente()
c1.adquirir_cheque_especial(b1)
#c1.depositar(40)
#c1.sacar(600)
c1.imprimir_comprovante(b1)

print('-------------------------------------\n')

b2 = Banco()
b2.criar_conta("paty", 986014831, 1200, 'masculino')
c2 = ContaCorrente()
c2.adquirir_cheque_especial(b2)
c2.depositar(100)
c2.sacar(50)
c2.imprimir_comprovante(b2)










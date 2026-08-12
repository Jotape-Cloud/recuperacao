from excecoes import ValorInvalidoError, VeiculoIndisponivelError

class Veiculo:
    def __init__(self, placa, modelo, valor_diaria):
        self.placa = placa
        self.modelo = modelo
        self.valor_diaria = valor_diaria
        self.disponivel = True

    def alugar(self):
        if not self.disponivel:
            raise VeiculoIndisponivelError(self.placa)

        self.disponivel = False
        print(f"Veículo {self.placa} alugado com sucesso.")

    def devolver(self):
        self.disponivel = True
        print(f"Veículo {self.placa} devolvido.")

    def calcular_valor(self, dias):
        if dias <= 0:
            raise ValorInvalidoError(dias)

        return self.valor_diaria * dias
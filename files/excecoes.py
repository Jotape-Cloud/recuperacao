class VeiculoIndisponivelError(Exception):
    def __init__(self, placa):
        self.placa = placa
        super().__init__(f"O veículo de placa {self.placa} não está disponível para locação.")


class VeiculoNaoEncontradoError(Exception):
    def __init__(self, placa):
        self.placa = placa
        super().__init__(f"Veículo de placa {self.placa} não encontrado.")


class ClienteNaoEncontradoError(Exception):
    def __init__(self, cpf):
        self.cpf = cpf
        super().__init__(f"Cliente com CPF {self.cpf} não encontrado.")


class ValorInvalidoError(Exception):
    def __init__(self, dias):
        self.dias = dias
        super().__init__(f"Quantidade de dias inválida: {self.dias}.")
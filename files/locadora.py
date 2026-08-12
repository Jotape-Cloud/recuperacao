from excecoes import ClienteNaoEncontradoError, VeiculoNaoEncontradoError

class Locadora:
    def __init__(self):
        self.veiculos = []
        self.clientes = []

    def cadastrar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def buscar_veiculo(self, placa):
        for veiculo in self.veiculos:
            if veiculo.placa == placa:
                return veiculo

        raise VeiculoNaoEncontradoError(placa)

    def buscar_cliente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente

        raise ClienteNaoEncontradoError(cpf)

    def alugar_veiculo(self, placa, cpf, dias):
        veiculo = self.buscar_veiculo(placa)
        cliente = self.buscar_cliente(cpf)
        valor = veiculo.calcular_valor(dias)
        veiculo.alugar()
        cliente.adicionar_locacao(veiculo, dias)
        return valor

    def devolver_veiculo(self, placa):
        veiculo = self.buscar_veiculo(placa)
        veiculo.devolver()
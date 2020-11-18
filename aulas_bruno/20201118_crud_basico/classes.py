class Pessoa:
    """Pessoa

    > Argumentos:
        - nome (str): Nome 
        - idade (int): Idade
        - cpf (str): CPF sem pontos nem traços
    """
    # Método construtor
    def __init__(self, nome:str, idade:int, cpf:str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf


class Veiculo:
    """Veiculo

    Esta classe serve de classe "mae" para outras classes com Carro, 
    Caminhao e Motocicleta

    > Argumentos:
        - num_rodas (int): Número de rodas;
        - cor (str): Cor do veículo;
        - marca (str): Marca, montadora, do veículo;
        - combustivel (str): Combustível (Gasolina, Álcool, ...);
        - cv (int): Pontência do motor em C.V. (Cavalo-Vapor);
        - proprietario (str): Nome do(a) proprietario(a) do veículo.
    """
    # Método construtor
    def __init__(self, num_rodas:int, cor:str, marca:str, combustivel:str, 
    cv:int, proprietario:str):
        self.num_rodas = num_rodas
        self.cor = cor
        self.marca = marca
        self.combustivel = combustivel
        self.cv = cv
        self.proprietario = proprietario
        self.passageiros = []
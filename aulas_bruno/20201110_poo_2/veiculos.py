"""
Programação Orientada a Objetos (POO)
- Herança e Polimorfismo
- Classes Veículos

Blusoft/Senac - Formação em Python Entra21 2020

Autor: Marcus Moresco Boeno
Último update: 2020-11-10

"""

# Importando classe Pessoa
from pessoa import Pessoa


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
    

    # Veículo acelerando
    def acelerar(self):
        """Som de aceleração

        > Argumentos:
            - Sem argumentos.
        
        > Output:
            - Sem output.
        """
        print("Vroooom!")
    

    # Veículo sendo abastecido
    def abastecer(self):
        """Abastecimento do veículo

        > Argumentos:
            - Sem argumentos.
        
        > Output:
            - Sem output.
        """
        print("Abastecendo o tanque! ...")
        print("Tanque completo!")
    

    # Vender veículo
    def vender(self):
        """Procedimento para venda do veículo

        > Argumentos:
            - Sem argumentos.
        
        > Output:
            - Sem output.
        """
        print(f"Vendendo {type(self).__name__} ...")
        self.proprietario = input("Nome do comprador: ")
        print("Venda realizada com sucesso!")
    

    # Método para apresentar nomes dos passageiros do veículo
    def apresentar_passageiros(self):
        """Apresentar nomes dos passageiros

        > Argumentos:
            - Sem argumentos.
        
        > Output:
            - Sem output
        """
        print([passageiro.get_name() for passageiro in self.passageiros])
    

    # Método para retornar lista de passageiros
    def listar_passageiros(self) -> list:
        """Listar passageiros no veículo

        > Argumentos:
            - Sem argumentos.
        
        > Output:
            - (list): Lista de passageiros (objetos da classe Pessoa)
        """
        return self.passageiros
    
    
    # Método para adicionar passageiros ao veículo
    def adicionar_passageiro(self, passageiro:Pessoa):
        """Adicionar passageiro

        Método para adicionar passageiro/motorista

        > Argumentos:
            - passageiro (Pessoa): Objeto da classe Pessoa representando
                um novo passageiro.
        
        > Output:
            - Sem output.
        """
        if len(self.passageiros) == self.num_lugares:
            print("Lotado!")
        else:
            self.passageiros.append(passageiro)
    

    # Método para retirar passageiros do veículo
    def retirar_passageiro(self, passageiro:str=None):
        """Retirar passageiro

        > Argumentos:
            - passageiro (str): Nome da pessoa a ser retirada.
        
        > Output:
            - Sem output.
        """
        # Remove ultimo passageiro se nenhum for indicado
        if passageiro is None:
            self.passageiros.pop()
        
        # Remove passageiro indicado
        else:
            for index, pessoa in enumerate(self.passageiros):
                if pessoa.get_name() == passageiro:
                    self.passageiros.pop(index)


class Carro(Veiculo):
    """Carro

    Classe representando um carro. Possui herança da classe
    Veiculo

    > Argumentos:
        - modelo (str): Modelo do carro;
        - num_portas (int): Número de portas;
        - num_lugares (int): Número de lugares;
        - cor (str): Cor do veículo;
        - marca (str): Marca, montadora, do veículo;
        - combustivel (str): Combustível (Gasolina, Álcool, ...);
        - cv (int): Pontência do motor em C.V. (Cavalo-Vapor);
        - proprietario (str): Nome do(a) proprietario(a) do veículo.
    """
    # Método construtor
    def __init__(self, modelo:str, num_portas:int, num_lugares:int, cor:str, 
    marca:str, combustivel:str, cv:int, proprietario:str):
        self.modelo = modelo
        self.num_portas = num_portas
        self.num_lugares = num_lugares
        super().__init__(4, cor, marca, combustivel, cv, proprietario)


class Caminhao(Veiculo):
    """Caminhao

    Classe representando um caminhao. Possui herança da classe
    Veiculo

    > Argumentos:
        - modelo (str): Modelo do caminhão;
        - num_lugares (int): Número de lugares;
        - num_eixos (int): Número de eixos;
        - num_rodas (int): Número de rodas;
        - capacidade_carga (int): Capacidade de carga do caminhão;
        - bau (bool): Booleano indicando se é caminhao bau ou não;
        - cor (str): Cor do veículo;
        - marca (str): Marca, montadora, do veículo;
        - combustivel (str): Combustível (Gasolina, Álcool, ...);
        - cv (int): Pontência do motor em C.V. (Cavalo-Vapor);
        - proprietario (str): Nome do(a) proprietario(a) do veículo.
    """
    # Método construtor
    def __init__(self, modelo:str, num_lugares:int, num_eixos:int, 
    num_rodas:int, capacidade_carga:int, bau:bool, cor:str, marca:str, 
    combustivel:str, cv:int, proprietario:str):
        self.modelo = modelo
        self.num_lugares = num_lugares
        self.num_eixos = num_eixos
        self.capacidade_carga = capacidade_carga
        self.bau = bau
        super().__init__(num_rodas, cor, marca, combustivel, cv, proprietario)


class Motocicleta(Veiculo):
    """Motocicleta

    Classe representando uma motocicleta. Possui herança da classe
    Veiculo

    > Argumentos:
        - modelo (str): Modelo da motocicleta;
        - automatica (bool): Booleano indicando se é automática ou não;
        - num_lugares (int): Número de lugares;
        - cor (str): Cor do veículo;
        - marca (str): Marca, montadora, do veículo;
        - combustivel (str): Combustível (Gasolina, Álcool, ...);
        - cv (int): Pontência do motor em C.V. (Cavalo-Vapor);
        - proprietario (str): Nome do(a) proprietario(a) do veículo.
    """
    # Método construtor
    def __init__(self, modelo:str, automatica:bool, num_lugares:int, cor:str, 
    marca:str, combustivel:str, cv:int, proprietario:str):
        self.modelo = modelo
        self.automatica = automatica
        self.num_lugares = num_lugares
        super().__init__(2, cor, marca, combustivel, cv, proprietario)


if __name__ == "__main__":

    # Instancia da classe Carro
    corsa = Carro(
        modelo="corsa", num_portas=3, num_lugares=5, cor="prata", 
        marca="Chevrolet", combustivel="Álcool", cv=76, 
        proprietario="João da Silva"
        )

    # Instancia da classe Caminhao
    scania = Caminhao(
        modelo="TR-1520XR", num_lugares=3, num_eixos=2, num_rodas=8, 
        capacidade_carga=2000, bau=False, cor="branco", marca="Scania", 
        combustivel="Diesel", cv=500, proprietario="João da Silva"
        )

    # Instancia da classe Motocicleta
    pcx = Motocicleta(
        modelo="PCX", automatica=True, num_lugares=2, cor="prata", 
        marca="Honda", combustivel="Gasolina", cv=14, 
        proprietario="João da Silva"
        )

    # Listagem dos veiculos na garagem
    garagem = [corsa, scania, pcx]

    for automovel in garagem:
        print(f"{type(automovel).__name__}: {automovel}")
    
    pcx.adicionar_passageiro(Pessoa("Cleber", 40, "456564546"))
    pcx.apresentar_passageiros()
    pcx.adicionar_passageiro(Pessoa("Cida", 40, "735753573"))
    pcx.apresentar_passageiros()
    print(pcx.listar_passageiros())
    pcx.adicionar_passageiro(Pessoa("Cida", 40, "735753573"))
    pcx.retirar_passageiro("Cleber")
    pcx.apresentar_passageiros()
    print(pcx.listar_passageiros())
    
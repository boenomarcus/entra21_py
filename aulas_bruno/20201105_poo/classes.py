"""
Criando e instanciando classes

Blusoft/Senac - Formação em Python Entra21 2020

Autor: Marcus Moresco Boeno
Último update: 2020-11-06

"""


class Caderno():

    # Método construtor
    def __init__(self, cor:str, num_paginas:int, marca:str):
        self.cor = cor
        self.num_paginas = num_paginas
        self.marca = marca
        self.conteudo = {}
    
    # Sobreescreve built-in print
    def __str__(self):
        return "Caderno {} da marca {} contendo {} páginas!".format(
                self.cor, self.marca, self.num_paginas
                )
    
    # Escrever texto em determinada pagina
    def escrever(self, txt, pagina):

        # Checa se a pagina indicada existe
        if pagina > self.num_paginas or pagina <= 0:
            print(
                "Página {} inexistente [Páginas válidas 1~{}]".format(
                    pagina, self.num_paginas
                    )
                )
        
        # Se a pagina existir, adicione o texto indicada
        else:
            if pagina in self.conteudo.keys():
                self.conteudo[pagina].append(txt)
            else:
                self.conteudo[pagina] = [txt]


class Mochila():
    
    # Método construtor
    def __init__(self, cor:str, marca:str, cap_ltrs:int):
        self.cor = cor
        self.marca = marca
        self.cap_ltrs = cap_ltrs
    
    # Sobreescreve built-in print
    def __str__(self):
        return "Mochila {} da marca {} com {} de capacidade!".format(
                self.cor, self.marca, self.cap_ltrs
                )


class Computador():
    
    # Método construtor
    def __init__(
        self, marca:str, cpu:str, ram:str, 
        hdd:str="**Empty**", ssd:str="**Empty**"
        ):
        self.marca = marca
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd
        self.ssd = ssd
            
    # Sobreescreve built-in print
    def __str__(self):
        string = "Configurações do Computador:"
        string += f"\n   > Marca: {self.marca}"
        string += f"\n   > CPU: {self.cpu}"
        string += f"\n   > RAM: {self.ram}"
        string += f"\n   > HDD: {self.hdd}"
        string += f"\n   > SSD: {self.ssd}"
        return string
    
    # Adicionando/Substituindo SSD
    def swap_ssd(self, ssd:str):
        if self.ssd == "**Empty**":
            print("Instalando SSD ...")
            self.ssd = ssd
            print("SSD instalado com sucesso ...")
        else:
            print("Substituindo SSD ...")
            self.ssd = ssd
            print("SSD substituído com sucesso ...")


class Monitor():
    
    # Método construtor
    def __init__(self, cor:str, marca:str, tamanho:str, freq:str):
        self.cor = cor
        self.marca = marca
        self.tamanho = tamanho
        self.freq = freq
    
    # Sobreescreve built-in print
    def __str__(self):
        return 'Monitor {} da marca {} com {}" e frequência de {}Hz.'.format(
                self.cor, self.marca, self.tamanho, self.freq
                )


class Mouse():
    
    # Método construtor
    def __init__(self, cor:str, marca:str, dpi:str):
        self.cor = cor
        self.marca = marca
        self.dpi = dpi
    
    # Sobreescreve built-in print
    def __str__(self):
        return "Mouse {} da marca {} com resolução de {} dpi.".format(
                self.cor, self.marca, self.dpi
                )


if __name__ == "__main__":

    # Criando instâncias
    caderno = Caderno("azul", 90, "Credeal")
    mochila = Mochila("cinza", "Dell", 25)
    computador = Computador(
        "Acer", "Intel Core i5 5430-U", 
        "8GB", hdd="1TB (5400 rpm)"
        )
    monitor = Monitor("Grafite", "Alienware", "27", "120")
    mouse = Mouse("Preto", "Razer", "600/1200")

    # Apresenta info dos objetos
    print("\n")
    print(caderno)
    print(mochila)
    print(computador)
    print(monitor)
    print(mouse)
    print("\n")

    # Escrevendo em paginas do caderno
    caderno.escrever("Funcionou!", 3)
    caderno.escrever("Aqui não vai funcionar!", 126)
    caderno.escrever("Funcionou aqui também!", 15)
    caderno.escrever("Mais texto na mesma pagina!", 15)
    
    # Apresentando conteudo do caderno
    print(caderno.conteudo)

    # Adicionando SSD no computador
    computador.swap_ssd("HP 500GB M.2 NVMe")
    print(computador)
    computador.swap_ssd("SAMSUNG EVO 512GB M.2 NVMe")
    print(computador)

"""
Object-Oriented Programming (OOP)
    - Graphics Processing Unit (GPU) Class and Methods

Blusoft/Senac - Formação em Python Entra21 2020

Author: Marcus Moresco Boeno
Last Update: 2020-11-16

"""


class GPU:
    """Graphics Processing Unit (GPU) Class

    > Class Parameters:
        - No paramaters.
    """
    # Constructor
    def __init__(self, manufacturer:str, model:str, memory:int):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__memory = memory
    
    @property
    def manufacturer(self) -> str:
        """GPU Manufacturer Getter

        > Arguments:
            - No arguments.
        
        > Output:
            - (str): GPU Manufacturer brand name.
        """
        return self.__manufacturer_getter
    
    @property
    def model(self) -> str:
        """GPU Model Getter

        > Arguments:
            - No arguments.
        
        > Output:
            - (str): GPU Model.
        """
        return self.__model_getter
    
    @property
    def memory(self) -> int:
        """GPU Memory Getter

        > Arguments:
            - No arguments.
        
        > Output:
            - (str): GPU Memory (GB).
        """
        return self.__memory_getter
    
    @manufacturer.setter
    def manufacturer(self, manu:str):
        """GPU Manufacturer Setter

        > Arguments:
            - manu (str): Manufacturer brand name.
        
        > Output:
            - No output.
        """
        self.__manufacturer_getter = manu
    
    @model.setter
    def model(self, cpu_model:str):
        """GPU Model Setter

        > Arguments:
            - gpu_model (str): GPU Model.
        
        > Output:
            - No output.
        """
        self.__model_getter = gpu_model
    
    @memory.setter
    def memory(self, gpu_memory:int):
        """GPU Memory Setter

        > Arguments:
            - gpu_memory (str): GPU Memory.
        
        > Output:
            - No output.
        """
        self.__memory_getter = gpu_memory
    
    # Represent GPU info as a string
    def __str__(self):
        """String representation of the GPU instance

        > Arguments:
            - No arguments.
        
        > Output:
            - (str): GPU as a string
        """
        return f"{self.__manufacturer} {self.__model} {self.__memory}GB"
"""
Object-Oriented Programming (OOP)
    - Central Processing Unit (CPU) Class and Methods

Blusoft/Senac - Formação em Python Entra21 2020

Author: Marcus Moresco Boeno
Last Update: 2020-11-16

"""

class CPU:
    """Central Processing Unit (CPU) Class
    
    > Class Parameters:
        - manufacturer (str): Manufacturer brand name;
        - model (str): MotherBoard model.
    """
    # Constructor
    def __init__(self, manufacturer:str, model:str, num_cores:int, clock_rate:float):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__num_cores = num_cores
        self.__clock_rate = clock_rate
    
    @property
    def manufacturer(self) -> str:
        """CPU Manufacturer Getter

        > Arguments:
            - No arguments.
        
        > Output:
            - (str): CPU Manufacturer brand name.
        """
        return self.__manufacturer_getter
    
    @property
    def model(self) -> str:
        """CPU Model Getter

        > Arguments:
            - No arguments.
        
        > Output:
            - (str): CPU Model.
        """
        return self.__model_getter
    
    @property
    def manufacturer(self) -> str:
        """CPU Manufacturer Getter

        > Arguments:
            - No arguments.
        
        > Output:
            - (str): CPU Manufacturer brand name.
        """
        return self.__manufacturer_getter
    
    @property
    def num_cores(self) -> int:
        """Number of CPU Cores Getter

        > Arguments:
            - No arguments.
        
        > Output:
            - (int): Number of CPU Cores.
        """
        return self.__num_cores_getter
    
    @property
    def clock_rate(self) -> float:
        """CPU Clock Rate Getter

        > Arguments:
            - No arguments.
        
        > Output:
            - (float): CPU Clock Rate (GHz).
        """
        return self.__clock_rate_getter
    
    @manufacturer.setter
    def manufacturer(self, manu:str):
        """CPU Manufacturer Setter

        > Arguments:
            - manu (str): Manufacturer brand name.
        
        > Output:
            - No output.
        """
        self.__manufacturer_getter = manu
    
    @model.setter
    def model(self, cpu_model:str):
        """CPU Manufacturer Setter

        > Arguments:
            - cpu_model (str): CPU Model.
        
        > Output:
            - No output.
        """
        self.__model_getter = cpu_model
    
    @num_cores.setter
    def num_cores(self, cores:int):
        """CPU Manufacturer Setter

        > Arguments:
            - cores (int): Number of CPU Cores.
        
        > Output:
            - No output.
        """
        self.__num_cores_getter = cores
    
    @clock_rate.setter
    def clock_rate(self, cpu_clock_rate:float):
        """CPU Clock Rate Setter

        > Arguments:
            - cpu_clock_rate (float): CPU Clock Rate (GHz).
        
        > Output:
            - No output.
        """
        self.__clock_rate_getter = cpu_clock_rate
    
    # Represent CPU info as a string
    def __str__(self):
        """String representation of the CPU instance

        > Arguments:
            - No arguments.
        
        > Output:
            - (str): CPU as a string
        """
        res = f"{self.__manufacturer} {self.__model}"
        res += f" [{self.__num_cores} cores] {self.__clock_rate} GHz"
        return res
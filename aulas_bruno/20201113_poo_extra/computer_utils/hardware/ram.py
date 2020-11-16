"""
Object-Oriented Programming (OOP)
    - Random Acces Memory (RAM) Class and Methods

Blusoft/Senac - Formação em Python Entra21 2020

Author: Marcus Moresco Boeno
Last Update: 2020-11-16

"""

class RAM:
    """Random Access Memory (RAM) Class

    > Class Parameters:
        - manufacturer (str): Manufacturer brand name;
        - capacity (int): Capacity (storage) of the RAM Module;
        - generation (str): Generation (DDR3, DDR4) of the RAM Module;
        - clock_rate (int): RAM Module Clock rate (MHz)
    """
    # Constructor
    def __init__(
        self, manufacturer:str, capacity:int, generation:str, clock_rate:int
        ):
        self.__manufacturer = manufacturer
        self.__capacity = capacity
        self.__generation = generation
        self.__clock_rate = clock_rate
    
    @property
    def manufacturer(self) -> str:
        """RAM Manufacturer Getter

        > Arguments:
            - No arguments.

        > Output:
            - (str): Manufacturer brand name. 
        """
        return self.__manufacturer_getter
    
    @property
    def capacity(self) -> int:
        """RAM Capacity Getter

        > Arguments:
            - No arguments.

        > Output:
            - (int): Capacity (storage) of the RAM Module.
        """
        return self.__capacity_getter

    @property
    def generation(self) -> str:
        """RAM Generation Getter

        > Arguments:
            - No arguments.

        > Output:
            - (str): Generation (DDR3, DDR4) of the RAM Module. 
        """
        return self.__generation_getter
    
    @property
    def clock_rate(self) -> int:
        """RAM Clock Rate Getter

        > Arguments:
            - No arguments.

        > Output:
            - (int): RAM Module Clock rate (MHz).
        """
        return self.__clock_rate_getter
    
    @manufacturer.setter
    def manufacturer(self, manu:str):
        """RAM Manufacturer Setter

        > Arguments:
            - manu (str): Manufacturer brand name.
        
        > Output:
            - No output.
        """
        self.__manufacturer_getter = manu
    
    @capacity.setter
    def capacity(self, cap:int):
        """RAM Capacity Setter

        > Arguments:
            - cap (int): Capacity (storage) of the RAM Module.
        
        > Output:
            - No output.
        """
        self.__capacity_getter = cap
    
    @generation.setter
    def generation(self, gen:str):
        """RAM Generation Setter

        > Arguments:
            - gen (str): Generation (DDR3, DDR4) of the RAM Module.
        
        > Output:
            - No output.
        """
        self.__generation_getter = gen
    
    @clock_rate.setter
    def clock_rate(self, rate:int):
        """RAM Clock Rate Setter

        > Arguments:
            - rate (int): RAM Module Clock rate (MHz).
        
        > Output:
            - No output.
        """
        self.__clock_rate_getter = cap
    
    # Represent RAM stick info as a string
    def __str__(self):
        res = f"{self.__manufacturer}"
        res += f" {self.__capacity}GB"
        res += f" {self.__generation}"
        res += f" {self.__clock_rate} MHz RAM Module"
        return res

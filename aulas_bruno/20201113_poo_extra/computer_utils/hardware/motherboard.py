"""
Object-Oriented Programming (OOP)
    - Mother Board Class and Methods

Blusoft/Senac - Formação em Python Entra21 2020

Author: Marcus Moresco Boeno
Last Update: 2020-11-16

"""

class MotherBoard:
    """Motherboard Class
    
    > Class Parameters:
        - No paramaters.
    """
    # Constructor
    def __init__(self, manufacturer:str, model:str):
        self.__manufacturer = manufacturer
        self.__model = model
    
    @property
    def manufacturer(self) -> str:
        """MotherBoard Manufacturer Getter

        > Arguments:
            - No arguments.
        
        > Output:
            - (str): Manufacturer brand name.
        """
        return self.__manufacturer_getter
    
    @property
    def model(self) -> str:
        """MotherBoard Model Getter

        > Arguments:
            - No arguments.
        
        > Output:
            - (str): MotherBoard Model.
        """
        return self.__model_getter
    
    @manufacturer.setter
    def manufacturer(self, manu:str):
        """MotherBoard Manufacturer Setter

        > Arguments:
            - manu (str): Manufacturer brand name.
        
        > Output:
            - No output.
        """
        self.__manufacturer_getter = manu
    
    @model.setter
    def model(self, mb_model:str):
        """MotherBoard Model Setter

        > Arguments:
            - manu (str): MotherBoard Model.
        
        > Output:
            - No output.
        """
        self.__model_getter = mb_model
    
    # Represent MotherBoard info as a string
    def __str__(self):
        return f"{self.__model} [{self.__manufacturer}] MotherBoard"

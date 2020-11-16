"""
Object-Oriented Programming (OOP)
    - Operational System Class and Methods

Blusoft/Senac - Formação em Python Entra21 2020

Author: Marcus Moresco Boeno
Last Update: 2020-11-16

"""

class OS_Build:
    """Operational System (OS) Class

    > Class Parameters:
        - No paramaters.
    """
    # Constructor
    def __init__(self, company:str, name:str, version:str):
        self.__company = company
        self.__name = name
        self.__version = version
    
    @property
    def company(self) -> str:
        """OS Company Getter

        > Arguments:
            - No arguments.
        
        > Output:
            - (str): Private instance attribute for os producer.
        """
        return self.__os_company
    
    @property
    def name(self) -> str:
        """OS Name Getter

        > Arguments:
            - No arguments.
        
        > Output:
            - (str): Private instance attribute for os name.
        """
        return self.__os_name
    
    @property
    def version(self) -> str:
        """OS Version Getter

        > Arguments:
            - No arguments.
        
        > Output:
            - (str): Private instance attribute for os version.
        """
        return self.__os_version
    
    @company.setter
    def company(self, c:str) -> str:
        """OS Company Setter

        > Arguments:
            - c (str): OS Company.
        
        > Output:
            - No output.
        """
        self.__os_company = c
    
    @name.setter
    def name(self, n:str) -> str:
        """OS Name Setter

        > Arguments:
            - n (str): OS Name.
        
        > Output:
            - No output.
        """
        self.__os_name = n

    @version.setter
    def version(self, v:str) -> str:
        """OS Version Setter

        > Arguments:
            - v (str): OS Version.
        
        > Output:
            - No output.
        """
        self.__os_version = v
    
    # Represent OS Info as a string
    def __str__(self) -> str:
        """String representation of the OS_Build instance

        > Arguments:
            - No arguments.
        
        > Output:
            - (str): OS info as a string
        """
        return f"{self.__company}, {self.__name} ({self.__version})"

if __name__ == "__main__":

    # Create Instance of an OS and print info on it
    my_os = OS_Build("Microsoft", "Windows 10", "Pro (Build:1909HS)")
    print(my_os)
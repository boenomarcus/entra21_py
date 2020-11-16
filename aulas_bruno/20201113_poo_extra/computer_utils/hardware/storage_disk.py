"""
Object-Oriented Programming (OOP)
    - Storage Disks Classes and Methods

Blusoft/Senac - Formação em Python Entra21 2020

Author: Marcus Moresco Boeno
Last Update: 2020-11-16

"""

class StorageDisk:
    """Base Class for Storage Disks

    > Class Parameters:
        - storage (int): Storage capacity in Gigabytes;
        - manufacturer (str): Manufacturer brand name;
        - size (str): Device size;
        - read (int): Reading rate (MB/s);
        - write (int): Writing rate (MB/s);
        - port (str): Communication Interface.
    """
    # Constructor
    def __init__(
        self, storage:int, manufacturer:str, size:str, 
        read:int, write:int, port:str
        ):
        self.storage = storage
        self.manufacturer = manufacturer
        self.size = size
        self.read = read
        self.write = write
        self.port = port

    @property
    def storage(self) -> int:
        """Storage Capacity Getter

        > Arguments:
            - No arguments.
        
        > Output:
            - (int): Storage capacity in Gigabytes.
        """
        return self.__storage_getter
    
    @property
    def manufacturer(self) -> str:
        """Storage Disk Manufacturer Getter

        > Arguments:
            - No arguments.
        
        > Output:
            - (str): Manufacturer brand name.
        """
        return self.__manufacturer_getter
    
    @property
    def size(self) -> str:
        """Storage Disk Size Getter

        > Arguments:
            - No arguments.
        
        > Output:
            - (str): Device size.
        """
        return self.__size_getter
    
    @property
    def read(self) -> int:
        """Storage Disk Read Rate Getter

        > Arguments:
            - No arguments.
        
        > Output:
            - (int): Reading rate (MB/s).
        """
        return self.__read_rate_getter
    
    @property
    def write(self) -> int:
        """Storage Disk Write Rate Getter

        > Arguments:
            - No arguments.
        
        > Output:
            - (int): Writing rate (MB/s).
        """
        return self.__write_rate_getter
    
    @property
    def port(self) -> str:
        """Communication Interface Getter

        Communication Interface (SATA, SATA M.2, M.2 PCIe NVMe)

        > Arguments:
            - No arguments.
        
        > Output:
            - (str): Communication interface.
        """
        return self.__port_getter
    
    @storage.setter
    def storage(self, sto:int):
        """Storage Capacity Setter

        > Arguments:
            - sto (int): Storage capacity in Gigabytes.
        
        > Output:
            - No output.
        """
        self.__storage_getter = sto
    
    @manufacturer.setter
    def manufacturer(self, manu:str):
        """Storage Disk Manufacturer Setter

        > Arguments:
            - manu (str): Manufacturer brand name.
        
        > Output:
            - No output.
        """
        self.__manufacturer_getter = manu
    
    @size.setter
    def size(self, siz:str):
        """Storage Disk Size Setter

        > Arguments:
            - siz (str): Device size.
        
        > Output:
            - No output.
        """
        self.__size_getter = siz
    
    @read.setter
    def read(self, read_rate:int):
        """Storage Disk Read Rate Setter

        > Arguments:
            - read_rate (int): Reading rate (MB/s).
        
        > Output:
            - No output.
        """
        self.__read_rate_getter = read_rate
    
    @write.setter
    def write(self, write_rate:int):
        """Storage Disk Write Rate Setter

        > Arguments:
            - write_rate (int): Writing rate (MB/s).
        
        > Output:
            - No output.
        """
        self.__write_rate_getter = write_rate
    
    @port.setter
    def port(self, port_interface:str):
        """Communication Interface Setter

        Communication Interface (SATA, SATA M.2, M.2 PCIe NVMe)

        > Arguments:
            - port_interface (str): Communication interface.
        
        > Output:
            - No output.
        """
        self.__port_getter = port_interface


class HDD(StorageDisk):
    """Hard Disk Drive (HDD) Class

    > Class Parameters:
        - rpm (int): Rotation of the Hard Disk (rpm).
        - StorageDisk Class Parameters apply to this class!
    """
    # Constructor
    def __init__(
        self, storage:int, manufacturer:str, size:str, 
        read:int, write:int, rpm:int, port:str
        ):
        self.rpm = rpm
        super().__init__(storage, manufacturer, size, read, write, port)
    
    @property
    def rpm(self) -> int:
        """Hard Disk Rotation Getter

        > Arguments:
            - No arguments.
        
        > Output:
            - (int): Rotation of the Hard Disk (rpm).
        """
        return self.__rpm_getter
    
    @rpm.setter
    def rpm(self, rpm_hdd:int):
        """Hard Disk Rotation Setter

        > Arguments:
            - rpm_hdd (int): Rotation of the Hard Disk (rpm).
        
        > Output:
            - No output.
        """
        self.__rpm_getter = rpm_hdd
       
    # Represent HDD info as a string
    def __str__(self):
        """String representation of the HDD instance

        > Arguments:
            - No arguments.
        
        > Output:
            - (str): HDD as a string
        """
        res = "> Hard Disk Drive (HDD):\n"
        res += f"   - Manufacturer: {self.manufacturer}\n"
        res += f"   - Storage: {self.storage} GB\n"
        res += f"   - Size: {self.size}\n"
        res += f"   - Port: {self.port}\n"
        res += f"   - Read Rate: {self.read} MB/s\n"
        res += f"   - Write Rate: {self.write} MB/s\n"
        res += f"   - Rotation: {self.rpm} rpm"
        return res


class SSD(StorageDisk):
    """Solid State Drive (SSD) Class

    > Class Parameters:
        - StorageDisk Class Parameters apply to this class!
    """
    # Constructor
    def __init__(
        self, storage:int, manufacturer:str, size:str, 
        read:int, write:int, port:str
        ):
        super().__init__(storage, manufacturer, size, read, write, port)
    
    # Represent SSD info as a string
    def __str__(self):
        """String representation of the HDD instance

        > Arguments:
            - No arguments.
        
        > Output:
            - (str): SSD as a string
        """
        res = "> Solid State Drive (HDD):\n"
        res += f"   - Manufacturer: {self.manufacturer}\n"
        res += f"   - Storage: {self.storage} GB\n"
        res += f"   - Size: {self.size}\n"
        res += f"   - Port: {self.port}\n"
        res += f"   - Read Rate: {self.read} MB/s\n"
        res += f"   - Write Rate: {self.write} MB/s"
        return res
    
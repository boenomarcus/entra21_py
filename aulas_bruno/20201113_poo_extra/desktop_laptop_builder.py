"""
Object-Oriented Programming (POO)
    - Desktop/Laptop Classes

Blusoft/Senac - Formação em Python Entra21 2020

Author: Marcus Moresco Boeno
Last Update: 2020-11-16

"""

# Import Computer Software Classes
import computer_utils.software as software

# Import Computer Hardware Classes
import computer_utils.hardware as hardware

class Computer():
    """Computer Class

    > Class Parameters:
        - motherboard (MotherBoard): Mother Board Object;
        - cpu (CPU): Processing Unit of the system;
        - integrated_gpu (GPU): Default graphics card (embedded);
        - dedicated_gpu (GPU): Extra graphics card;
        - ram (RAM): RAM Module;
        - os_drive (StorageDisk): Main drive where the OS is installed;
        - secondary_drive (StorageDisk): Secondary storage drive;
        - os_sys (OS_Build): Operating System Object.

    """
    # Constructor
    def __init__(
        self, motherboard, cpu, integrated_gpu, 
        dedicated_gpu, ram, os_drive, 
        secondary_drive, os_sys
        ):
        self.__motherboard = motherboard
        self.__cpu = cpu
        self.__integrated_gpu = integrated_gpu
        self.__dedicated_gpu = dedicated_gpu
        self.__ram = ram
        self.__drive_01 = os_drive
        self.__drive_02 = secondary_drive
        self.__os_sys = os_sys
        

class Desktop(Computer):
    """Desktop Class (Builds upon Computer Class)

    > Class Parameters:
        - cabinet (str): Desktop Cabinet Model;
        - Computer Class Parameters apply to this class!
    """
    # Constructor
    def __init__(
        self, motherboard, cpu, integrated_gpu, dedicated_gpu, ram, 
        os_drive, secondary_drive, os_sys, cabinet
        ):
        self.__cabinet = cabinet
        super().__init__(
            motherboard, cpu, integrated_gpu, dedicated_gpu, ram, 
            os_drive, secondary_drive, os_sys
        )


class Laptop(Computer):
    """Laptop Class (Builds upon Computer Class)

    > Class Parameters:
        - screen (int): Screen size (inches);
        - manufacturer (str): Manufacturer brand name;
        - Computer Class Parameters apply to this class!
    """
    # Constructor
    def __init__(
        self, motherboard, cpu, integrated_gpu, dedicated_gpu, ram, 
        os_drive, secondary_drive, os_sys, screen, manufacturer
        ):
        self.__screen = screen
        self.__manufacturer = manufacturer
        super().__init__(
            motherboard, cpu, integrated_gpu, dedicated_gpu, ram, 
            os_drive, secondary_drive, os_sys
        )


if __name__ == "__main__":

    # Create Instance of an OS and print info on it
    my_os = software.OS_Build("Microsoft", "Windows 10 Pro", "1909HS")
    print(my_os)

    # Create Instance of a MotherBoard and print info on it
    my_mb = hardware.MotherBoard("ASUS", "XTRz-30")
    print(my_mb)

    # Create Instance of a MotherBoard and print info on it
    my_ram = hardware.RAM("Kingston", 8, "DDR4", 2666)
    print(my_ram)

    # Create Instance of an HDD and print info on it
    my_hdd = hardware.HDD(500, "TOSHIBA", "2.5in", 140, 70, 5400, "SATA")
    print(my_hdd)

    # Create Instance of an HDD and print info on it
    my_ssd = hardware.SSD(
        512, "Hewllet-Packard (HP)", "80x120mm", 2100, 1650, "M.2 PCIe NVMe"
        )
    print(my_ssd)

    # Create Instance of a CPU and print info on it
    my_cpu = hardware.CPU("Intel", "i5-5430", 2, 2.85)
    print(my_cpu)

    # Create Instance of a CPU and print info on it
    my_gpu = hardware.GPU("NVIDIA", "GeForce 1050-Ti", 4)
    print(my_gpu)

    my_desktop = Desktop(
        motherboard=my_mb, 
        cpu=my_cpu, 
        integrated_gpu=my_gpu, 
        dedicated_gpu=my_gpu, 
        ram=my_ram, 
        os_drive=my_ssd,
        secondary_drive=my_hdd, 
        os_sys=my_os,
        cabinet="GAMERMAXX Plus"
        )
    print(my_desktop.__dict__)

    my_laptop = Laptop(
        motherboard=my_mb, 
        cpu=my_cpu, 
        integrated_gpu=my_gpu, 
        dedicated_gpu=my_gpu, 
        ram=my_ram, 
        os_drive=my_ssd,
        secondary_drive=my_hdd, 
        os_sys=my_os,
        screen="14in",
        manufacturer="Dell Inc."
        )
    print(my_laptop.__dict__)

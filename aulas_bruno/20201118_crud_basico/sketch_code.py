import sqlite3

DB_PATH = "clients.db"


class Client:
    """Class to create client objects
    """
    def __init__(self, name, cpf, email):
        self.name = name
        self.cpf = cpf
        self.email = email


class Vehicle:
    """Class to crete vehicle objects
    """
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color


class DataReader:
    """Class to Read data from a SQLite instance table
    """
    def __init__(self, db_path, table):
        self.db_path = db_path
        self.table = table
    
    def retrieve_all(self):
        """Retrieve all data within a given table
        """
        # Create connection with db and a cursor to handle data
        with sqlite3.connect(self.db_path) as conn:

            # Create a SQLite cursor
            c = conn.cursor()

            # Build SQL select command and execute it
            c.execute(f"SELECT * FROM {self.table}".replace("'", ""))
            
            # Fetch table data
            content = c.fetchall()
        
        # Return content as a list of tuples
        return content

class DataWriter:
    """Class to perform CRUD operations
    """
    # Constructor
    def __init__(self, obj):
        self.obj = obj
        self.table = type(obj).__name__.lower() + "s"
    
    def insert(self, db_path):
        """Method to insert data into SQLite instance
        """
        # Create connection with db and a cursor to handle data
        with sqlite3.connect(db_path) as conn:

            # Get instance attributes as a dictionary
            data = self.obj.__dict__

            # Create a SQLite cursor
            c = conn.cursor()
            
            # Build the SQL insert command
            query = "INSERT INTO {} {}".format(
                self.table, tuple(data.keys())
                )
            query += f" VALUES {('?',)*len(data)}"
            
            # Execute command and commit data
            c.execute(query.replace("'", ""), tuple(data.values()))
            conn.commit()

    def update_info(self, db_path):
        pass

    def delete_data(self, db_path):
        pass

if __name__ == "__main__":
    
    # Create Client instances
    c01 = Client("Peter", "189.892.312-99", "peter@yahoo.com")
    c02 = Client("John", "098.734.231-00", "john@amazon.com.uk")

    # Create Vechicle instances
    v01 = Vehicle("Cadillac", "Navigator", "2014", "Silver")
    v02 = Vehicle("Land Rover", "Discovery", "2016", "White")

    # Insert client data into clients table
    DataWriter(c01).insert(DB_PATH)
    DataWriter(c02).insert(DB_PATH)

    # Insert vehicle data into vechicles table
    DataWriter(v01).insert(DB_PATH)
    DataWriter(v02).insert(DB_PATH)

    # Fetch client and vehicle data and print it
    print(DataReader(DB_PATH, "clients").retrieve_all())
    print(DataReader(DB_PATH, "vehicles").retrieve_all())
    
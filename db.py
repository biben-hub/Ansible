import psycopg2

class DatabaseConnection:
    
    def __init__(self):
        try:
            self.conex = psycopg2.connect(host = "localhost", user = "rooot", password = "mypass", database = "myfirst_db")

            self.mycursor = self.conex.cursor()
            print("Connection succeeded !")
        except Exception as errors:
            print("Error : ", errors)


    def drop_table(self):
        self.mycursor.execute("DROP TABLE IF EXISTS matable;")

    def create_table(self):
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS matable (id INT);")

    def close_connection(self):
        self.conex.commit()
        self.conex.close()
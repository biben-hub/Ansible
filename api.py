import psycopg2

conex = psycopg2.connect(host = "localhost", user = "rooot", password = "mypass", database = "myfirst_db")

mycursor = conex.cursor()

mycursor.execute("DROP TABLE IF EXISTS matable;")
print("data table droped !")

mycursor.execute("CREATE TABLE IF NOT EXISTS matable (id SERIAL PRIMARY KEY);")
print("database created !")

conex.commit()

conex.close()
import psycopg2




try:
    conex = psycopg2.connect(host = "localhost", user = "rooot", password = "mypass", database = "myfirst_db")

    mycursor = conex.cursor()
    print("Connection succeeded !")
except Exception as errors:
    print("Error : ", errors)



mycursor.execute("DROP TABLE IF EXISTS matable;")
print("data table droped !")


mycursor.execute("CREATE TABLE IF NOT EXISTS matable (id INT);")
print("database created !")

conex.commit()

conex.close()
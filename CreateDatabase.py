import sqlite3
import timeit

start = timeit.default_timer()

connection = sqlite3.connect("UmbrellaDataTable.db")
cursor = connection.cursor()

sql = """
        CREATE TABLE UmbrellaDataTable (
            time INTEGER,
            hostName TEXT,
            airQuality FLOAT,
            humidity FLOAT,
            temperature FLOAT,
            pressure FLOAT,
            VOCEstimate FLOAT,
            gasSensorResistance FLOAT,
            carbonDioxideEstimate FLOAT
        
        ) """

cursor.execute(sql)
print("Table has been created")

connection.commit()
connection.close()

end = timeit.default_timer()
print("Run time: ", end - start, "ms")

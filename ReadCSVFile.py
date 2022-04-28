import sqlite3
import timeit

start = timeit.default_timer()

# Establish database connection
connection = sqlite3.connect("UmbrellaDataTable.db")
cursor = connection.cursor()

with open('UmbrellaData.csv', 'r') as file:
    numOfRecords = 0

    # Copy data from CSV file to database
    for row in file:
        cursor.execute("INSERT INTO UmbrellaDataTable VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", row.split(","))
        connection.commit()
        numOfRecords += 1

connection.close()
stop = timeit.default_timer()

print('\n{} Records Transferred'.format(numOfRecords))
print("Run time: ", stop - start, "ms")

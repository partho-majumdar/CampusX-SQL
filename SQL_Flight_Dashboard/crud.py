import mysql.connector

try:
    conn = mysql.connector.connect(
        host="127.0.0.1", user="root", password="", database="flight_dashboard"
    )
    mycursor = conn.cursor()
    print("Connection established")

except Exception:
    print("Connection error")

# ------------------- create a database
# mycursor.execute("CREATE DATABASE flight_dashboard")
# conn.commit()

# ------------------- create a table (airport -> airport_id, code, name, city)
# mycursor.execute(
#     """
# CREATE TABLE airport(
#     airport_id INTEGER PRIMARY KEY,
#     code VARCHAR(255) NOT NULL,
#     city VARCHAR(255) NOT NULL,
#     name VARCHAR(255) NOT NULL
# )
# """
# )
# conn.commit()

# ------------------- Insert data to the table
# mycursor.execute(
#     """
# INSERT INTO airport VALUES
# (1, "DEL", "New Delhi", "IGIA"),
# (2, "CCU", "Kolkata", "NSCA"),
# (3, "BOM", "Mumbai", "CSMA")

# """
# )
# conn.commit()

# ------------------- search / retrieve
mycursor.execute("SELECT * FROM airport WHERE airport_id > 1")
data = mycursor.fetchall()
print(data)

for i in data:
    print(i[3])

# ------------------- UPDATE
# mycursor.execute(
#     """
# UPDATE airport
# SET city = 'Bombay'
# WHERE airport_id = 3
# """
# )
# conn.commit()

# ------------------- DELETE
# mycursor.execute(
#     """ 
# DELETE FROM airport WHERE airport_id = 3
# """
# )
# conn.commit()

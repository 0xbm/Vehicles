import sqlite3

con = sqlite3.connect("vehicles.db")
cursor = con.cursor()
result = cursor.execute(
    "select count(*) from cars"
).fetchall()  # returns array of tupples
results = cursor.execute("select * from cars;").fetchall()
num_of_rows = result[0][0]
num_of_rowssss = results[0][0]
print("Number of rows: ", num_of_rows)
print(num_of_rowssss)

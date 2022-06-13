"""Database for the users."""

import sqlite3

conn = sqlite3.connect("src/database/users.db")

c = conn.cursor()

# Create a table
# c.execute("""CREATE TABLE user (
#         user_id integer,   # make it primanry key and auto increment
#         name text,
#         email text,
#         password text
#         )""")


# Insert data
# c.execute("INSERT INTO user VALUES ('Liis', 'U', 'liis@gmail.com', 'pass')")


name = "Hello"
email = "email@gmail.com"
password = "passwod"

# c.execute("INSERT INTO user VALUES (?, ?, ?)", (name, email, password))

# conn.commit()

# Select statement
c.execute("SELECT * FROM user")

res = c.fetchall()

print(res)

# conn.commit()

conn.close()

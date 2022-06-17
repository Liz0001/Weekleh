"""Here we create the user account."""

import sqlite3


def connection():
    """Connect to database."""
    conn = sqlite3.connect("src/database/weekleh.db")
    c = conn.cursor()

    # Create a table
    c.execute("""CREATE TABLE user (
            user_id integer PRIMARY KEY  AUTO INCREMENT,
            name text,
            email text,
            password text,
            notes_id FOREINGN KEY references()
            )""")

"""
CREATE TABLE IF NOT EXISTS weekleh.own_weeks (
    weeks_id integer PRIMARY KEY AUTOINCREMENT,
    individual_week integer
);

CREATE TABLE IF NOT EXISTS weekleh.days (
    days_id integer PRIMARY KEY AUTOINCREMENT,
    task_days text
);


CREATE TABLE IF NOT EXISTS weekleh.task_list (
    task_id        integer     PRIMARY KEY AUTOINCREMENT,
    task_name      text        NOT NULL,
    task_how_often integer,              -- how often, weekly, monthly etc...
    task_done      integer,              -- is the task done or not
    weeks_id       integer,              -- user chooses their own weeks
    days_id        integer,              -- Mon - fri etc
    task_date      datetime,             -- for example for birthdays 1 day a year
    
     FOREIGN KEY (days_id)
         REFERENCES days (days_id) 
);

CREATE TABLE IF NOT EXISTS weekleh.user (
    user_id        integer     PRIMARY KEY AUTOINCREMENT,
    name           text        NOT NULL,
    email          text        UNIQUE NOT NULL,
    password       text        NOT NULL,
    task_id        integer,
    
    FOREIGN KEY (task_id)
        REFERENCES task_list (task_id)
);
"""


    # Insert data
    # c.execute("INSERT INTO user VALUES ('Liis', 'U', 'liis@gmail.com', 'pass')")


    # name = "Hello"
    # email = "email@gmail.com"
    # password = "passwod"

    # c.execute("INSERT INTO user VALUES (?, ?, ?)", (name, email, password))

    # conn.commit()

    # Select statement
    c.execute("SELECT * FROM user")

    res = c.fetchall()

    print(res)

    # conn.commit()

    conn.close()


def create_account(name, email, pwd):
    """."""
    print(name, email, pwd)


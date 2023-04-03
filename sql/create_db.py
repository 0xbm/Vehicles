import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"vehicles.db"

    sql_create_make_table = """ CREATE TABLE IF NOT EXISTS make (
                                        id INTEGER PRIMARY KEY,
                                        make TEXT NOT NULL
                                    ); """

    sql_create_model_table = """ CREATE TABLE IF NOT EXISTS model (
                                        id INTEGER PRIMARY KEY,
                                        model TEXT NOT NULL
                                    ); """

    sql_create_card_table = """ CREATE TABLE IF NOT EXISTS card (
                                        id INTEGER PRIMARY KEY,
                                        registration_number TEXT,
                                        odometer_start INTEGER,
                                        odometer_end INTEGER,
                                        kilometers_in_month INTEGER,
                                        fuel_start FLOAT,
                                        fuel_tank_in_month FLOAT,
                                        fuel_total FLOAT,
                                        fuel_consumption FLOAT,
                                        fuel_standard_consumption FLOAT,
                                        fuel_abnormal_consumption FLOAT,
                                        fuel_savings FLOAT,
                                        fuel_for_the_next_month FLOAT
                                    ); """

    sql_create_paragons_table = """ CREATE TABLE IF NOT EXISTS paragons (
                                        id INTEGER PRIMARY KEY,
                                        date TEXT,
                                        fuel FLOAT,
                                        price FLOAT
                                    ); """

    sql_create_addons_table = """ CREATE TABLE IF NOT EXISTS addons (
                                        id INTEGER PRIMARY KEY,
                                        vin TEXT,
                                        fuel_type TEXT,
                                        capacity FLOAT,
                                        kw FLOAT,
                                        technical_inspection TEXT
                                    ); """

    # sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
    #                                 id integer PRIMARY KEY,
    #                                 name text NOT NULL,
    #                                 priority integer,
    #                                 status_id integer NOT NULL,
    #                                 project_id integer NOT NULL,
    #                                 begin_date text NOT NULL,
    #                                 end_date text NOT NULL,
    #                                 FOREIGN KEY (project_id) REFERENCES projects (id)
    #                             );"""

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_make_table)
        create_table(conn, sql_create_model_table)
        create_table(conn, sql_create_card_table)
        create_table(conn, sql_create_paragons_table)
        create_table(conn, sql_create_addons_table)
        # create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == "__main__":
    main()

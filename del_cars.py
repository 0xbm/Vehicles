import sqlite3
from sqlite3 import Error
from update_cars import select_vehicles


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def delete(conn, id):
    sql = "DELETE FROM cars WHERE id=?"
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def delete_all(conn):
    sql = "DELETE FROM asd"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def main():
    database = r"vehicles.db"
    conn = create_connection(database)
    with conn:
        select_vehicles()
        id = input("Select id to update: ")
        delete(conn, id)
        # delete_all(conn);


if __name__ == "__main__":
    main()

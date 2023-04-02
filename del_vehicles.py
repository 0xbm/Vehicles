import sqlite3
from sqlite3 import Error
from update_cars import select_make


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def delete(conn, id):
    sql = "DELETE FROM make WHERE id=?"
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def delete_all_make(conn):
    # sql = "DELETE FROM make"
    sql = "DELETE FROM make, model WHERE id=1"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def delete_all_model(conn):
    sql = "DELETE FROM model"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def main():
    database = r"vehicles.db"
    conn = create_connection(database)
    with conn:
        choice = input(
            "What would you like to do?\n1.Delete specify car \n2.Delete all cars or q for quit:"
        )
        match choice:
            case "1":
                select_make()
                id = input("Select id to update: ")
                delete(conn, id)

            case "2":
                delete_all_make(conn)


if __name__ == "__main__":
    main()

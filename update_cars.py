import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def edit_make(conn, project):
    sql = """ UPDATE make
              SET make = ?
              WHERE id = ?"""

    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()


def edit_model(conn, project):
    sql = """ UPDATE model
              SET model = ?
              WHERE id = ?"""

    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()


# def update_card(conn, project):
#     sql = """ UPDATE registration_number
#               SET model = ?
#               WHERE id = ?"""

#     cur = conn.cursor()
#     cur.execute(sql, project)
#     conn.commit()


def select_make():
    con = sqlite3.connect("vehicles.db")
    cursor = con.cursor()
    result = cursor.execute(
        "SELECT id, make FROM make"
    ).fetchall()  # returns array of tupples
    num_of_vehicles = " ".join(map(str, result))
    print("Select make ID: ", "\x1b[5;30;42m" + num_of_vehicles + "\x1b[0m")


def select_model():
    con = sqlite3.connect("vehicles.db")
    cursor = con.cursor()
    result = cursor.execute(
        "SELECT id, model FROM model"
    ).fetchall()  # returns array of tupples
    num_of_vehicles = " ".join(map(str, result))
    print("Select model ID: ", "\x1b[5;30;42m" + num_of_vehicles + "\x1b[0m")


def list_vehicles():
    con = sqlite3.connect("vehicles.db")
    cursor = con.cursor()
    result = cursor.execute(
        "SELECT make.id, make.make, model.model  FROM make INNER JOIN model ON make.ID=model.ID"
    ).fetchall()  # returns array of tupples
    num_of_vehicles = " ".join(map(str, result))
    print("Your cars: " + "\x1b[5;30;42m" + num_of_vehicles + "\x1b[0m")


def main():
    database = r"vehicles.db"
    conn = create_connection(database)
    list_vehicles()
    with conn:
        choice = input(
            "What would you like to do?\n1.Edit make \n2.Edit model \n8. Edit whole car \nor q for quit: \n"
        )
        match choice:
            case "1":
                select_make()
                id = input("Select make ID to edit: ")
                make = input("Car make: ")

                edit_make(
                    conn,
                    (
                        make.capitalize(),
                        id,
                    ),
                )
                main()

            case "2":
                select_model()
                id = input("Select model ID to edit: ")
                model = input("Car model: ")

                edit_model(
                    conn,
                    (
                        model.capitalize(),
                        id,
                    ),
                )
                main()

            case "q":
                print("\x1b[5;30;42m" + "QUIT" + "\x1b[0m")
                quit()


if __name__ == "__main__":
    main()

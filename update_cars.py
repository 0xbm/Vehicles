import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def update_car(conn, project):
    sql = """ UPDATE cars
              SET make = ? ,
                  model = ? ,
                  registration_number = ?,
                  technical_inspection = ?
              WHERE id = ?"""

    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()


def update_make(conn, project):
    sql = """ UPDATE cars
              SET make = ?

              WHERE id = ?"""

    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()


def update_model(conn, project):
    sql = """ UPDATE cars
              SET model = ?

              WHERE id = ?"""

    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()


def update_reg_number(conn, project):
    sql = """ UPDATE cars
              SET registration_number = ?

              WHERE id = ?"""

    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()


def update_tech_insp(conn, project):
    sql = """ UPDATE cars
              SET technical_inspection = ?

              WHERE id = ?"""

    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()


def number_of_vehicles():
    con = sqlite3.connect("vehicles.db")
    cursor = con.cursor()
    result = cursor.execute(
        "SELECT id, make, model FROM cars"
    ).fetchall()  # returns array of tupples
    num_of_vehicles = result
    print("Number of vehicles: ", "\x1b[5;30;42m" + str(num_of_vehicles) + "\x1b[0m")


def select_vehicles():
    con = sqlite3.connect("vehicles.db")
    cursor = con.cursor()
    result = cursor.execute(
        "SELECT id, make, model FROM cars"
    ).fetchall()  # returns array of tupples
    num_of_vehicles = result
    print("Select vehicles ID: ", "\x1b[5;30;42m" + str(num_of_vehicles) + "\x1b[0m")


def main():
    database = r"vehicles.db"
    conn = create_connection(database)

    with conn:
        choice = input(
            "What would you like to do?\n1.Update make \n2.Update model \n3.Update reg number \n4.Update tech_insp \n5. Update whole car or q for quit: \n"
        )
        match choice:
            case "1":
                select_vehicles()

                make = input("Car make: ")
                # model = input("Car model: ")
                # reg_number = input("Registration number: ")
                # tech_insp = input("Technical inspection date (ones in a year): ")
                # number_of_vehicles()
                #
                id = input("Select id to update: ")
                update_make(
                    conn,
                    (
                        make.capitalize(),
                        # model.capitalize(),
                        # reg_number.upper(),
                        # tech_insp,
                        id,
                    ),
                )
                main()
            case "2":
                select_vehicles()
                model = input("Car model: ")
                id = input("Select id to update: ")
                update_model(
                    conn,
                    (
                        # make.capitalize(),
                        model.capitalize(),
                        # reg_number.upper(),
                        # tech_insp,
                        id,
                    ),
                )
                main()
            case "3":
                select_vehicles()
                reg_number = input("Registration number: ")
                id = input("Select id to update: ")
                update_reg_number(
                    conn,
                    (
                        # make.capitalize(),
                        # model.capitalize(),
                        reg_number.upper(),
                        # tech_insp,
                        id,
                    ),
                )
                main()
            case "4":
                select_vehicles()
                tech_insp = input("Technical inspection date (ones in a year): ")
                id = input("Select id to update: ")
                update_tech_insp(
                    conn,
                    (
                        # make.capitalize(),
                        # model.capitalize(),
                        # reg_number.upper(),
                        tech_insp,
                        id,
                    ),
                )
                main()
            case "5":
                select_vehicles()

                make = input("Car make: ")
                model = input("Car model: ")
                reg_number = input("Registration number: ")
                tech_insp = input("Technical inspection date (ones in a year): ")
                number_of_vehicles()
                id = input("Select id to update: ")
                update_car(
                    conn,
                    (
                        make.capitalize(),
                        model.capitalize(),
                        reg_number.upper(),
                        tech_insp,
                        id,
                    ),
                )
                main()
            case "q":
                print("\x1b[5;30;42m" + "QUIT" + "\x1b[0m")
                quit()


if __name__ == "__main__":
    main()

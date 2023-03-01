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
                  vin = ?,
                  capacity = ?,
                  kW = ?,
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


def update_registration_number(conn, project):
    sql = """ UPDATE cars
              SET registration_number = ?
              WHERE id = ?"""

    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()


def update_vin(conn, project):
    sql = """ UPDATE cars
              SET vin = ?
              WHERE id = ?"""

    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()


def update_capacity(conn, project):
    sql = """ UPDATE cars
              SET capacity = ?
              WHERE id = ?"""

    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()


def update_kw(conn, project):
    sql = """ UPDATE cars
              SET kw = ?
              WHERE id = ?"""

    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()


def update_technical_inspection(conn, project):
    sql = """ UPDATE cars
              SET technical_inspection = ?
              WHERE id = ?"""

    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()


# def number_of_vehicles():
#     con = sqlite3.connect("vehicles.db")
#     cursor = con.cursor()
#     result = cursor.execute(
#         "SELECT id, make, model FROM cars"
#     ).fetchall()  # returns array of tupples
#     num_of_vehicles = result
#     print("Number of vehicles: ", "\x1b[5;30;42m" + str(num_of_vehicles) + "\x1b[0m")


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
            "What would you like to do?\n1.Update make \n2.Update model \n3.Update registration number \n4.Update VIN number \n5.Update capacity \n6.Update kW \n7.Update technical inspection \n8. Update whole car or q for quit: \n"
        )
        match choice:
            case "1":
                select_vehicles()
                id = input("Select id to update: ")
                make = input("Car make: ")

                update_make(
                    conn,
                    (
                        make.capitalize(),
                        id,
                    ),
                )
                main()
            case "2":
                select_vehicles()
                id = input("Select id to update: ")
                model = input("Car model: ")

                update_model(
                    conn,
                    (
                        model.capitalize(),
                        id,
                    ),
                )
                main()

            case "3":
                select_vehicles()
                id = input("Select id to update: ")
                reg_number = input("Registration number: ")

                update_registration_number(
                    conn,
                    (
                        reg_number.upper(),
                        id,
                    ),
                )
                main()

            case "4":
                select_vehicles()
                id = input("Select id to update: ")
                vin = input("VIN number: ")

                update_vin(
                    conn,
                    (
                        vin,
                        id,
                    ),
                )
                main()

            case "5":
                select_vehicles()
                id = input("Select id to update: ")
                capacity = input("Capacity: ")

                update_capacity(
                    conn,
                    (
                        capacity,
                        id,
                    ),
                )
                main()

            case "6":
                select_vehicles()
                id = input("Select id to update: ")
                kw = input("kW: ")

                update_kw(
                    conn,
                    (
                        kw,
                        id,
                    ),
                )
                main()

            case "7":
                select_vehicles()
                id = input("Select id to update: ")
                tech_insp = input("Technical inspection date (ones in a year): ")

                update_technical_inspection(
                    conn,
                    (
                        tech_insp,
                        id,
                    ),
                )
                main()
            case "8":
                select_vehicles()
                id = input("Select id to update: ")

                make = input("Car make: ")
                model = input("Car model: ")
                reg_number = input("Registration number: ")
                vin = input("VIN number: ")
                capacity = input("capacity: ")
                kw = input("Kw: ")
                tech_insp = input("Technical inspection date (ones in a year): ")

                update_car(
                    conn,
                    (
                        make.capitalize(),
                        model.capitalize(),
                        reg_number.upper(),
                        vin,
                        capacity,
                        kw,
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

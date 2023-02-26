import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def update_cars(conn, project):
    sql = """ UPDATE cars
              SET make = ? ,
                  model = ? ,
                  registration_number = ?,
                  technical_inspection = ?
              WHERE id = ?"""

    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()


def number_of_vehicles():
    con = sqlite3.connect("vehicles.db")
    cursor = con.cursor()
    result = cursor.execute(
        "select id, make, model from cars"
    ).fetchall()  # returns array of tupples
    num_of_vehicles = result
    print("Number of vehicles: ", "\x1b[5;30;42m" + str(num_of_vehicles) + "\x1b[0m")


def main():
    database = r"vehicles.db"
    conn = create_connection(database)

    with conn:
        choice = input("What would you like to do?\n1.Update car or q for quit: \n")
        match choice:
            case "1":
                make = input("Car make: ")
                model = input("Car model: ")
                reg_number = input("Registration number: ")
                tech_insp = input("Technical inspection date (ones in a year): ")
                number_of_vehicles()
                id = input("Select id to update: ")
                update_cars(
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

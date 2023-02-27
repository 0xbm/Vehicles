import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_project(conn, project):
    sql = """ INSERT INTO cars(make,model,registration_number,technical_inspection)
              VALUES(?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


# def create_task(conn, task):
#     """
#     Create a new task
#     :param conn:
#     :param task:
#     :return:
#     """

#     sql = """ INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
#               VALUES(?,?,?,?,?,?) """
#     cur = conn.cursor()
#     cur.execute(sql, task)
#     conn.commit()
#     return cur.lastrowid


def main():
    database = r"vehicles.db"
    conn = create_connection(database)

    with conn:
        choice = input("What would you like to do?\n1.Add car or q for quit: \n")
        match choice:
            case "1":
                make = input("Car make: ")
                model = input("Car model: ")
                reg_number = input("Registration number: ")
                tech_insp = input("Technical inspection date (one in year): ")
                project = (
                    make.capitalize(),
                    model.capitalize(),
                    reg_number.upper(),
                    tech_insp,
                )
                project_id = create_project(conn, project)

                main()
            case "q":
                print("\x1b[5;30;42m" + "QUIT" + "\x1b[0m")
                quit()

        # made = input("Car made: ")
        # model = input("Car model: ")
        # technical_insp = input("Tech insp: ")
        # project = (made, model, technical_insp)
        # # project = ("skoda", "fabia", "2023-02-23")
        # project_id = create_project(conn, project)

        # main()

        # tasks
        # task_1 = (
        #     "Analyze the requirements of the app",
        #     1,
        #     1,
        #     project_id,
        #     "2015-01-01",
        #     "2015-01-02",
        # )
        # task_2 = (
        #     "Confirm with user about the top requirements",
        #     1,
        #     1,
        #     project_id,
        #     "2015-01-03",
        #     "2015-01-05",
        # )

        # # create tasks
        # create_task(conn, task_1)
        # create_task(conn, task_2)


if __name__ == "__main__":
    main()

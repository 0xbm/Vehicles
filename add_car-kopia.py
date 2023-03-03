import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_make(conn, project):
    sql = """ INSERT INTO make(make)
              VALUES(?) """
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


def create_model(conn, project):
    sql = """ INSERT INTO model(model)
              VALUES(?) """
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


# def create_card(conn, project):
#     sql = """ INSERT INTO card(***)
#               VALUES(?) """
#     cur = conn.cursor()
#     cur.execute(sql, project)
#     conn.commit()
#     return cur.lastrowid


# def create_paragons(conn, project):
#     sql = """ INSERT INTO paragons(date, fuel)
#               VALUES(?,?) """
#     cur = conn.cursor()
#     cur.execute(sql, project)
#     conn.commit()
#     return cur.lastrowid


# def create_addons(conn, project):
#     sql = """ INSERT INTO addons(vin, fuel_type,capacity,kw,technical_inspection)
#               VALUES(?,?,?,?,?) """
#     cur = conn.cursor()
#     cur.execute(sql, project)
#     conn.commit()
#     return cur.lastrowid


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
    database = r"vehicles_1.db"
    conn = create_connection(database)

    with conn:
        choice = input(
            "What would you like to do?\n1.Add make car \n2.Add model \3.Add card or q for quit: \n"
        )
        match choice:
            case "1":
                make = input("Car make: ")
                project = (make.capitalize(),)
                project_id = create_make(conn, project)
                main()
            case "2":
                model = input("Car model: ")
                project = (model.capitalize(),)
                project_id = create_model(conn, project)
                main()
            # with conn:
            #     choice = input("What would you like to do?\n1.Add car or q for quit: \n")
            #     match choice:
            #         case "1":
            #             make = input("Car make: ")
            #             model = input("Car model: ")
            #             reg_number = input("Registration number: ")
            #             vin = input("VIN number: ")
            #             capacity = input("capacity: ")
            #             kw = input("Kw: ")
            #             tech_insp = input("Technical inspection date (one in year): ")

            #             project = (
            #                 make.capitalize(),
            #                 model.capitalize(),
            #                 reg_number.upper(),
            #                 vin,
            #                 capacity,
            #                 kw,
            #                 tech_insp,
            #             )
            #             project_id = create_project(conn, project)

            #             main()
            case "q":
                print("\x1b[5;30;42m" + "QUIT" + "\x1b[0m")
                quit()

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

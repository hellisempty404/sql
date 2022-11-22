import sqlite3
  
try:
    sqlite_connection = sqlite3.connect('books.db')
    sqlite_create_table_query = '''CREATE TABLE auth (
                                id INTEGER PRIMARY KEY,
                                age TEXT NOT NULL,
                                first_name TEXT NOT NULL,
                                last_name TEXT NOT NULL);'''

    cursor = sqlite_connection.cursor()
    print("База данных подключена")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print("Таблица Auth создана")

    cursor.close()

except sqlite3.Error as error:
    pass

finally:
    pass
   
def main():
    print("\n\n")
    print("1) Ввести данные в таблицу")
    print("2) Вывести данные")
    print("3) Выход ")
    s = str(input(">"))
    if s=='1':
        return write_table()
    if s=='2':
        return read_table()
    if s=='3':
        exit()
    else:
        return main()

def write_table():
    name = str(input("Введите имя:"))
    second_name = str(input("Введите фамилию:"))
    age = str(input("Введите возраст:"))

    sqlite_connection = sqlite3.connect('books.db')
    cursor = sqlite_connection.cursor()


    sqlite_insert_query = """INSERT INTO auth(age, first_name, last_name)  VALUES('{}','{}','{}')""".format(age, name, second_name)

    cursor.execute(sqlite_insert_query)
    sqlite_connection.commit()
    return main()

def read_table():
    print("\n\n")
    print("id|age|name|second_name|")
    con = sqlite3.connect('books.db')
    with con:
        cur = con.cursor()    
        cur.execute("SELECT * FROM auth")
 
        while True:
            row = cur.fetchone()
        
            if row == None:
                break
            
            print(row[0], row[1], row[2],row[3])
    return main()
if __name__ == '__main__':
    main()


import sqlite3 

class Database:
    
    def __init__(self):
        self.conn = sqlite3.connect("database.db") 
        self.cursor = self.conn.cursor()
        self.create()

    def create(self):
        self.cursor.execute(""" 
CREATE TABLE IF NOT EXISTS Shop(
                            Shoes_id INTEGER PRIMARY KEY, 
                            Shoe_type TEXT NOT NULL,
                            Cost INT NOT NULL,
                            Amount INT,
                            UNIQUE (Soe_type)
)""")
        self.cursor.executemany("INSERT INTO SHOP (Shoe_type, Cost, Amount) VALUES(?,?,?)",
                            [('Regular', 2000, 10),
                             ('Tactical', 3000, 10),
                             ('Sports', 2500, 10)])
        self.conn.commit()

        self.cursor.execute(""" 
CREATE TABLE IF NOT EXISTS Users(
                            User_id INTEGER PRIMARY KEY,
                            Name TEXT NOT NULL,
                            Password NOT NULL,
                            ShopList Text,
)""")
        self.cursor.executemany("INSERT INTO User (Name, Pawword) VALUES(?)",
                            [('Tom', "12314")])
        self.conn.commit()

        self.cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS Admins(
                                Admin_id NOT NULL,
                                Name TEXT NOT NULL,
                                Password NOT NULL,
    )""")
        self.cursor.executemany("INSERT INTO Admins (Name, Password) VALUES(?)",
                                [('Mike', "12314412")])
        self.conn.commit()

        
        self.cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS Workers(
                            
                                Name TEXT NOT NULL,
                                Password NOT NULL,
    )""")
        self.cursor.executemany("INSERT INTO Workers (Name, Password) VALUES(?)",
                                [('Andrew', "1213")])
        self.conn.commit()


    
    def executeQuerry(self, query, value = None):
        try: 
            with self.conn:
                if value: 
                    self.cursor.execute(query, value)
                else: self.cursor.execute(query)
        except sqlite3.Error as e:
            print(f"Ошибка: {e}")

    def insertDate(self, table, data):
        columns = ",".join(data.keys()) 
        print (columns)
        placholders = ", ".join("?" for _ in data)
        print(placholders)
        query = f"INSERT INTO {table} ({columns}) VALUES ({placholders})" 
        self.executeQuerry(query, tuple(data.values()))

    def updateData(self, table,data , condition):
        updateData = ", ".join(f"{column} = ?" for column in data.keys())
        print(updateData)
        query = f"UPDATE {table} SET {updateData} WHERE {condition} = ?"
        self.executeQuerry(query, tuple(data.values() + condition.values())[0])

    def deleteData(self, table, data):
        query = f"DELETE FROM {table} IF EXISTS WHERE {data.keys()[0]} = ?"
        self.executeQuerry(query, tuple(data.values())[0])

    def getData(self, table):
        query = f"SELECT * FROM {table}"
        self.executeQuerry(query)




class Main:
    def __init__(self):
        self.base = Database()

    def reg(self):
        
        print("Выберете действие 1-зарегестрироваться как пользователь 2-как админ 3-как рабочий")
        a = input()
        if a == 1:
            self.user_login = input('Login: ')
            self.user_password = input('Password: ')

           
            if self.base.fetchone() is None:
                self.base.insertDate("Admins",self.user_login)
                self.base.commit()
            else: 
                pass

            self.Useractions()

        elif a == 2: 
            self.user_login = input('Login: ')
            self.user_password = input('Password: ')

            
            if self.base.fetchone() is None:
                self.base.insertDate("Admins",self.user_login)
                self.base.commit()
            else: 
                pass
            self.AdminActions()

        else: 
            self.user_login = input('Login: ')
            self.user_password = input('Password: ')

           
            if self.base.fetchone() is None:
                self.base.insertDate("Workers",self.user_login)
                self.base.commit()
            else: 
                pass
            self.WorkerActions()

        print("Ready")
    
    def Useractions(self):
        input("Нажмите ввод для вывода списка товаров")
        for i in self.base.execute('SELECT Shoe_type , Cost'):
            print(i)

        a = input("Выберете ботинки")

        for i in self.base.execute(f"SELECT Amount FROM Shoes WHERE Shoe_type = '{a}'"):
            shoebalance = self.base.fetchone()[0]

        self.base.updateData( "Shoes", shoebalance-1, a)

        self.base.updateData( "Users", )

        for i in self.base.execute(f"SELECT Shoplist FROM Users WHERE Name  = '{self.user.login}'"):
            shoebalance = self.base.fetchone()[0]

        print("ваша корзина")
        for i in self.base.execute("SELECT Shoplist, FROM USERS where Name =  '{self.user.login}'"):
            print(i)
    
    def AdminActions(self):
        a = input("выберете действие 1-добавить данные, 2-обновить данные, 3-удалить данные 4-вывести данные")
        if a == 1:
            b=input("таблица")
            c=input("данные")
            self.base.insertDate(b,c)
        elif a==2:
            b=input("таблица")
            c=input("данные")
            f=input("условие")
            self.base.insertDate(b,c,f)

        elif a==3:
            b=input("таблица")
            c=input("данные")
            self.base.deleteData(b,c)

        elif a==4:
            b=input("таблица")
            c=input("столбец")
            f=input("переменная")
            p=input("условие")

            for i in self.base.execute("SELECT {с}, FROM {b} where {f} =  {p}"):
                print(i)

    def WorkerActions(self):
         
        a = input("выберете действие 1-добавить данные, 2-обновить данные, 3-удалить данные 4-вывести данные")
        if a == 1:
            c=input("данные")
            self.base.insertDate("Shop",c)
        elif a==2:
            c=input("данные")
            f=input("условие")
            self.base.insertDate("Shop",c,f)

        elif a==3:
            c=input("данные")
            self.base.deleteData("Shop",c)

        elif a==4:
            c=input("столбец")
            f=input("переменная")
            p=input("условие")

            for i in self.base.execute("SELECT {с}, FROM Shop where {f} =  {p}"):
                print(i)
    def main(self):
        self.reg()

main = Main()
Main.main()
                

            











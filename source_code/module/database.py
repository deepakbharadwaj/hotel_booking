import pymysql

class Database:
    def connect(self):
        return pymysql.connect(host="hotel-mysql", user="dev", password="dev", database="hotel_booking", charset='utf8mb4')

    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM hotel order by name asc")
            else:
                cursor.execute(
                    "SELECT * FROM hotel where hid = %s order by name asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO hotel(name,phone,email,zip) VALUES(%s, %s, %s, %s)",
                           (data['name'], data['phone'], data['email'], data['zip'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE hotel set name = %s, phone = %s, email = %s, zip = %s where id = %s",
                           (data['name'], data['phone'], data['email'], data['zip'], id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM hotel where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

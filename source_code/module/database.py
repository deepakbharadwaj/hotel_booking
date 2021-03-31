import pymysql

class Database:
    def connect(self):
        return pymysql.connect(host="hotel-mysql", user="dev", password="dev", database="hotel_booking", charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    def getHotels(self, id):
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

    def addHotel(self,data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO hotel(name,phone,email,zip) VALUES(%s, %s, %s, %s)", (data['name'], data['phone'], data['email'], data['zip']))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def updateHotel(self, id, data):
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

    def deleteHotel(self, id):
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
    
    def getRooms(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM room order by hid asc")
            else:
                cursor.execute(
                    "SELECT * FROM room where rid = %s order by hid asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def addRoom(self, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO room(hid, rtype, rnumber, price ) VALUES(%s, %s, %s, %s)",
                           (data['hid'], data['rtype'], data['rnumber'], data['price'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
    
    def getBookings(self,id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM bookings;")
            else:
                cursor.execute(
                    "SELECT * FROM bookings where bid = %s", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()
    
    def checkAvailability(self,rid,fromdate,todate):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("SELECT * FROM bookings where rid = %s AND ( `from` BETWEEN %s AND %s OR `to` BETWEEN %s AND %s);",(rid,fromdate,todate,fromdate,todate))
            if len(list(cursor.fetchall())) == 0:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return ()
        finally:
            con.close()



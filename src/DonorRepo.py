import DonorModel


class Repo():
    def __init__(self, db) -> None:
        self.conn = db.conn
        self.cur = db.cur

    def createDONORTable(self):
        try:
            query = """CREATE TABLE IF NOT EXISTS "DONOR" (
                        "Name" TEXT,
                        "Mobile" TEXT,
                        "Email" TEXT PRIMARY KEY UNIQUE,
                        "Address" TEXT,
                        "Donation_Item_Name" TEXT,
                        "Donation_Item_Number" INTEGER,
                        "TimeSlot" TEXT,
                        "Date" TEXT
                    );"""
            self.cur.execute(query)
        except Exception as e:
            print(e)
            return False
        return True

    def addDonor(self, donor):
        try:
            query = """INSERT INTO "DONOR" ( "Name" ,"Mobile","Email","Address","Donation_Item_Name","Donation_Item_Number","TimeSlot","Date") VALUES ('{}','{}','{}','{}','{}','{}','{}','{}');""".format(
                donor.name, donor.mobile, donor.email, donor.address, donor.donation_Item_Name, donor.donation_Item_Number, donor.timeSlot, donor.date)
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print(e)
            return False
        return True


    def getDonorByName(self, name):
        try:
            query = """ SELECT * from "DONOR" WHERE "Name" = '{}';""".format(
                name)
            self.cur.execute(query)
            donorTable = self.cur.fetchall()
            donor = DonorModel.Donor(
                donorTable[0][0], donorTable[0][1], donorTable[0][2], donorTable[0][3], donorTable[0][4], donorTable[0][5], donorTable[0][6], donorTable[0][7])
        except Exception as e:
            print(e)
            return [False, None]
        return [True, donor]

    def getDonorByEmail(self, email):
        try:
            query = """ SELECT * from "DONOR" WHERE "Email" = '{}';""".format(
                email)
            self.cur.execute(query)
            donorTable = self.cur.fetchall()
            donor = DonorModel.Doner(
                donorTable[0][0], donorTable[0][1], donorTable[0][2], donorTable[0][3], donorTable[0][4], donorTable[0][5], donorTable[0][6], donorTable[0][7])
        except Exception as e:
            print(e)
            return [False, None]
        return [True, donor]

    def getAllDonors(self):
        try:
            query = """ SELECT * from "DONOR"; """
            self.cur.execute(query)
            donorTable = self.cur.fetchall()
        except Exception as e:
            print(e)
            return [False, None]
        donors = []
        for row in donorTable:
            donor = DonorModel.Donor(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            donors.append(donor)
        return [True, donors]

    def deleteDonorByEmail(self, email):
        try:
            query = """DELETE from "DONOR" WHERE "Email" = '{}';""".format(
                email)
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print(e)
            return False
        return True

    
    def deleteDonorByName(self, name):
        try:
            query = """DELETE from "DONOR" WHERE "Name" = '{}';""".format(
                name)
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print(e)
            return False
        return True

    
    def deleteDonorByAddress(self, address):
        try:
            query = """DELETE from "DONOR" WHERE "Address" = '{}';""".format(
                address)
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print(e)
            return False
        return True

    def deleteDONORTable(self):
        try:
            query = """ DROP TABLE IF EXISTS "DONOR"; """
            self.cur.execute(query)
        except Exception as e:
            print(e)
            return False
        return True 

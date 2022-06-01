import NgoModel


class Repo():
    def __init__(self, db) -> None:
        self.conn = db.conn
        self.cur = db.cur

    def createNGOTable(self):
        try:
            query = """CREATE TABLE IF NOT EXISTS "NGO" (
                        "Name" TEXT,
                        "Email" TEXT PRIMARY KEY UNIQUE,
                        "Address" TEXT
                    );"""
            self.cur.execute(query)
        except Exception as e:
            print(e)
            return False
        return True

    def addNgo(self, ngo):
        try:
            query = """INSERT INTO "NGO" ( "Name" ,"Email","Address") VALUES ('{}','{}','{}');""".format(
                ngo.name, ngo.email, ngo.address)
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print(e)
            return False
        return True


    def getNgoByName(self, name):
        try:
            query = """ SELECT * from "NGO" WHERE "Name" = '{}';""".format(
                name)
            self.cur.execute(query)
            ngoTable = self.cur.fetchall()
            ngo = NgoModel.Ngo(ngoTable[0][0], ngoTable[0][1], ngoTable[0][2])
        except Exception as e:
            print(e)
            return [False, None]
        return [True, ngo]

    def getNgoByEmail(self, email):
        try:
            query = """ SELECT * from "NGO" WHERE "Email" = '{}';""".format(
                email)
            self.cur.execute(query)
            ngoTable = self.cur.fetchall()
            ngo = NgoModel.Ngo(ngoTable[0][0], ngoTable[0][1], ngoTable[0][2])
        except Exception as e:
            print(e)
            return [False, None]
        return [True, ngo]

    def getAllNgos(self):
        try:
            query = """ SELECT * from "NGO"; """
            self.cur.execute(query)
            ngoTable = self.cur.fetchall()
        except Exception as e:
            print(e)
            return [False, None]
        ngos = []
        for row in ngoTable:
            ngo = NgoModel.Ngo(row[0], row[1], row[2])
            ngos.append(ngo)
        return [True, ngos]

    def deleteNgoByEmail(self, email):
        try:
            query = """DELETE from "NGO" WHERE "Email" = '{}';""".format(
                email)
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print(e)
            return False
        return True

    
    def deleteNgoByName(self, name):
        try:
            query = """DELETE from "NGO" WHERE "Name" = '{}';""".format(
                name)
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print(e)
            return False
        return True

    
    def deleteNgoByAddress(self, address):
        try:
            query = """DELETE from "NGO" WHERE "Address" = '{}';""".format(
                address)
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print(e)
            return False
        return True

    def deleteNGOTable(self):
        try:
            query = """ DROP TABLE IF EXISTS "NGO"; """
            self.cur.execute(query)
        except Exception as e:
            print(e)
            return False
        return True
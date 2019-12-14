import mysql.connector
import Config as cfg
class AccidentDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host=cfg.mysql['host'],
        user=cfg.mysql['username'],
        password=cfg.mysql['password'],
        database=cfg.mysql['database']
        )

    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into accidents (province,VehicleType,DriverAge,DriverSex, MonthYear) values (%s,%s,%s,%s,%s)"
        cursor.execute(sql, (values))
        self.db.commit()
        rowid = cursor.lastrowid
        cursor.close()
        return rowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from accidents"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        cursor.close()
        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from accidents where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="update accidents set province=%s,VehicleType=%s,DriverAge=%s,DriverSex=%s, MonthYear=%s where id=%s"
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()

    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from accidents where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
 
    def convertToDictionary(self, result):
        colnames=['id','province','VehicleType','DriverAge','DriverSex', 'MonthYear']
        item = {}
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        return item
        
AccidentDAO = AccidentDAO()
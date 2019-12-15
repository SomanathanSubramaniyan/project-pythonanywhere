# import the mysql connector module to estabilish connection with the database, the database config parameters
import mysql.connector
import Config as cfg

# The class definitions to connect to the mysql databases
class AccidentDAO:
    # Ensure there is no existing db connection while initiating the class
    db=""

     # function:: Connection to DB
     def connectToDB(self):
        self.db = mysql.connector.connect(
        host=cfg.mysql['host'],
        user=cfg.mysql['username'],
        password=cfg.mysql['password'],
        database=cfg.mysql['database']
        )

    # function:: Instantiating class to connet to the db
    def __init__(self): 
        self.connectToDB()
    
    # function:: Cursor for the DB connection
    def getCursor(self):
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()

    # function: To Post the values in the database accidents
    def create(self, values):
        cursor = self.getCursor()
        sql="insert into accidents (province,VehicleType,DriverAge,DriverSex, MonthYear) values (%s,%s,%s,%s,%s)"
        cursor.execute(sql, (values))
        self.db.commit()
        rowid = cursor.lastrowid
        cursor.close()
        return rowid
    
    #function: To get all the accident details from the database
    def getAll(self):
        cursor = self.getCursor()
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

    # function: To find the accident details by ID
    def findByID(self, id):
        cursor = self.getCursor()
        sql="select * from accidents where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        return self.convertToDictionary(result)
    
    #function: To update the accident details by ID
    def update(self, values):
        cursor = self.getCursor()
        sql="update accidents set province=%s,VehicleType=%s,DriverAge=%s,DriverSex=%s, MonthYear=%s where id=%s"
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()

    #function: To update the accident details by ID
    def delete(self, id):
        cursor = self.getCursor()
        sql="delete from accidents where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()

    #function: To convert the input value (DB output) into the python dictionary
    def convertToDictionary(self, result):
        colnames=['id','province','VehicleType','DriverAge','DriverSex', 'MonthYear']
        item = {}
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        return item
        
AccidentDAO = AccidentDAO()
from flask import Flask,jsonify,request,abort
from AccidentDAO import AccidentDAO

app = Flask(__name__,static_url_path='', static_folder='.')

@app.route('/Accidents')
def getAll():
    results = AccidentDAO.getAll()
    return jsonify(results)

#curl -X GET "http://127.0.0.1:5000/Accidents/2"
@app.route('/Accidents/<int:id>')
def findByid(id):
    foundAccident = AccidentDAO.findByID(id)
    return jsonify(foundAccident)

#curl -i -H "Content-Type:application/json" -X POST -d "{\"province\":\"Munster\", \"VehicleType\":\"Bus\", \"DriverAge\":\"40 to 50\", \"DriverSex\":\"Male\",\"Month-Year\":\"Feb-2019\"}" http://127.0.0.1:5000/Accidents
@app.route('/Accidents', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    Accident = {
    "province":request.json['province'],
    "VehicleType":request.json['VehicleType'] ,
    "DriverAge":request.json['DriverAge'] ,
    "DriverSex":request.json['DriverSex'] ,
    "MonthYear":request.json['MonthYear'] }
    values = ( Accident["province"],Accident["VehicleType"],Accident["DriverAge"],Accident["DriverSex"],Accident["MonthYear"] )
    newId = AccidentDAO.create(values)
    Accident["id"]=newId
    return jsonify(Accident) 

#curl -i -H "Content-Type:application/json" -X PUT -d "{\"VehicleType\":\"Bus\"}" http://127.0.0.1:5000/Accidents/3
@app.route('/Accidents/<int:id>', methods=['PUT'])
def update(id):
    foundAccident = AccidentDAO.findByID(id)
    if not foundAccident:
        abort(404)
    if not request.json:
        abort(400)
    reqJson = request.json
    print(reqJson)
    if 'province' in reqJson:
        foundAccident['province'] = reqJson['province']
    if 'VehicleType' in reqJson:
        foundAccident['VehicleType'] = reqJson['VehicleType']
    if 'DriverAge' in reqJson:
        foundAccident['DriverAge'] = reqJson['DriverAge']
    if 'DriverSex' in reqJson:
        foundAccident['DriverSex'] = reqJson['DriverSex']
    if 'MonthYear' in reqJson:
        foundAccident['MonthYear'] = reqJson['MonthYear']
    values = (foundAccident["province"],foundAccident["VehicleType"],foundAccident["DriverAge"],foundAccident["DriverSex"],foundAccident["MonthYear"],foundAccident["id"]  )
    print(values)
    AccidentDAO.update(values)
    return jsonify(foundAccident)
    
#curl -X DELETE "http://127.0.0.1:5000/Accidents/1"
@app.route('/Accidents/<int:id>', methods=['DELETE'])
def delete(id):
    AccidentDAO.delete(id)
    return jsonify({"done":True})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify, abort, send_from_directory
from module.database import Database
import os

app = Flask(__name__)
db = Database()

UPLOAD_DIRECTORY = "/app/uploaded_images"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@app.route('/', methods = ['GET'])
def test():
    return "Welcome To Hotel Booking Application", 200

@app.route('/getHotels', methods = ['GET'])
def getHotels():
    return jsonify(db.getHotels(None)),200

@app.route('/getHotel/<int:id>/', methods = ['GET'])
def getHotel(id):
    return jsonify(db.getHotels(id)),200

@app.route('/addHotel', methods = ['POST'])
def addHotel():
    if db.addHotel():
        return "Hotel Added", 201
    else:
        return "DB error", 500

@app.route('/updateHotel/<int:id>/', methods = ['PUT'])
def updateHotel(id):
    data = db.getHotels(id)

    if len(data) == 0:
        return "no Hotel found", 204
    else:
        if db.updateHotel(id, request.json):
            return "Hotel updated",201
        else:
            return "DB error",500

@app.route('/deleteHotel/<int:id>/')
def delete(id):
    data = db.getHotels(id)

    if len(data) == 0:
        return "no Hotel found", 204
    else:
        if db.deleteHotel(id):
            return "Hotel deleted",201
        else:
            return "DB error",500

@app.route('/getRooms', methods = ['GET'])
def getRooms():
    return jsonify(db.getRooms(None)),200

@app.route('/getRoom/<int:id>/', methods = ['GET'])
def getRoom(id):
    return jsonify(db.getRooms(id)),200

@app.route('/addRoom', methods = ['POST'])
def addRoom():
    if db.addRoom(request.json):
        return "Room added",201
    else:
        return "DB error",500

@app.errorhandler(404)
def page_not_found(error):
    return "PAGE NOT FOUND", 404

if __name__ == '__main__':
    app.run(port=8181, host="0.0.0.0")  
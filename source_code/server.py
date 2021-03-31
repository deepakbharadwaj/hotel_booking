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
    return "Welcome To Hotel Booking Application!!!", 200

@app.route('/getHotels', methods = ['GET'])
def getHotels():
    return jsonify(db.getHotels(None)),200

@app.route('/getHotel/<int:id>/', methods = ['GET'])
def getHotel(id):
    return jsonify(db.getHotels(id)),200

@app.route('/addHotel', methods = ['POST'])
def addHotel():
    if db.addHotel(request.json):
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

# Images
@app.route("/images")
def list_images():
    folder_str = {}
    for folder in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, folder)
        folder_str[folder] = []
        for filename in os.listdir(path):
            folder_str[folder].append(filename)

    return jsonify(folder_str)

@app.route("/images/<path:path>")
def get_image(path):
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


@app.route("/addImage/<int:id>/", methods=["POST"])
def post_file(id):
    data = db.getHotels(id)

    if len(data) == 0:
        return "No Hotel found", 204
    else:
        fh = request.files['file']
        image_folder = os.path.join(UPLOAD_DIRECTORY,str(id))
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
        image_name = str(len(os.listdir(image_folder))+1) + '.jpg'
        image_path = os.path.join(image_folder, image_name)
        fh.save(image_path)
        return "Image added", 201

# Bookings
@app.route('/getBookings', methods = ['GET'])
def getBookings():
    return jsonify(db.getBookings(None)),200

@app.route('/getBooking/<int:id>/', methods = ['GET'])
def getBooking(id):
    return jsonify(db.getBookings(id)),200

@app.route('/checkAvailability', methods = ['POST'])
def checkAvailability():
    params = request.json
    data = db.getRooms(int(params['rid']))
    if len(data) == 0:
        return "No such Room found", 200
    else:
        if db.checkAvailability(int(params['rid']),params['from'],params['to']):
            return "Room Available",200
        else:
            return "Room not Available",200

@app.errorhandler(404)
def page_not_found(error):
    return "PAGE NOT FOUND", 404

if __name__ == '__main__':
    app.run(port=8181, host="0.0.0.0",debug=True)
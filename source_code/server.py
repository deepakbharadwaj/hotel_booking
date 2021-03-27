from flask import Flask
from module.database import Database

app = Flask(__name__)
db = Database()

@app.route('/')
def index():
    data = db.read(1)
    return str(data)

if __name__ == '__main__':
    app.run(port=8181, host="0.0.0.0")    
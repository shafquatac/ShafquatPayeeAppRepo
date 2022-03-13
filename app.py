from flask import Flask

from flask_cors import CORS

app = Flask(__name__)
CORS(app)



app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Shafquat!'




if __name__ == '__main__':
    app.run()






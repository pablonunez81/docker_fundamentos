from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "Juan",
        "lastname": "Perez",
        "socialMedia":
        {
            "facebookUser": "juaniperez",
            "instagramUser": "juaniperez",
            "xUser": "juaniperez",
            "linkedin": "juan-perez",
            "githubUser": "juaniperez"
        },
        "blog": "https://juanperez.com",
        "author": "Juan Perez"
    }

    return jsonify(value)

if __name__ == '__main__':
    app.run(port=5000)
import json
from flask import Flask
app = Flask(__name__)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "Juan",
        "lastname": "Perez",
        "socialMedia":
        [
            {"facebookUser": "juaniperez"},
            {"instagramUser": "juaniperez"},
            {"xUser": "juaniperez"},
            {"linkedin": "juaniperez"},
            {"githubUser": "juaniperez"}
        ],
        "blog": "https://juaniperez.com",
        "author": "Juan Perez"
    }
    return json.dumps(value)
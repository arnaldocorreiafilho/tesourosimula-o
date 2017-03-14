from flask import Flask, jsonify, request
import json
import tesouro

app = Flask("Tesouro")

@app.route("/")
def hello_world():
    return json.dumps( { "email": "bill@microsoft.com",
  "url": "http://www.microsoft.com",
  "since": "2011-09-08T08:06:48Z",
  "bio": "I am awesome"
})


@app.route('/colors', methods = ['GET'])
def get_colors():
    return tesouro.get_data()

app.run()



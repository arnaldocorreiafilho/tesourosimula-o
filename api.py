from flask import Flask, jsonify, request
import json
import tesouro

app = Flask("Tesouro")

@app.route("/email")
def hello_world():
    return json.dumps( { "email": "bill@microsoft.com",
  "url": "http://www.microsoft.com",
  "since": "2011-09-08T08:06:48Z",
  "bio": "I am awesome"
})


@app.route('/colors', methods = ['GET'])
def get_colors():
    return tesouro.get_data()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
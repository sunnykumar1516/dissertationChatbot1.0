from flask import Flask, request, jsonify
from jokes import handle_response,get_responsefronwit
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "sunny"

@app.route('/get-resp/')
def getUser():
    text = request.args.get("text")
    reply = get_responsefronwit(text)
    return reply

@app.route('/response/data', methods=['POST'])
def post_data():
    data = request.json  # Assuming the client sends JSON data in the request body
    # Process the data as needed
    response_data = {'message': 'Data received successfully'}
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

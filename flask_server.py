from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "alive"})

@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()
    direction = data.get("direction")
    speed = data.get("speed")

    print(f"Received command: Direction={direction}, Speed={speed}")

    return jsonify({"status": "ok", "direction": direction, "speed": speed})

if __name__ == "__main__":
    app.run(debug=True)

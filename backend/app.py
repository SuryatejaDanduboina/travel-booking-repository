from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "message": "Travel Booking API is running"
    }), 200


@app.route("/api/destinations", methods=["GET"])
def destinations():
    return jsonify([
        {"id": 1, "name": "Hyderabad"},
        {"id": 2, "name": "Sydney"},
        {"id": 3, "name": "Singapore"}
    ]), 200


@app.route("/api/bookings", methods=["POST"])
def create_booking():
    data = request.get_json(silent=True) or {}

    name = data.get("name", "").strip()
    destination = data.get("destination", "").strip()

    if not name or not destination:
        return jsonify({
            "error": "Name and destination are required"
        }), 400

    allowed_destinations = [
        "Hyderabad", "Sydney", "Singapore"
    ]

    if destination not in allowed_destinations:
        return jsonify({
            "error": "Invalid destination"
        }), 400

    # Database integration will be added in the RDS step.
    return jsonify({
        "message": f"Booking request received for {destination}",
        "name": name,
        "destination": destination
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

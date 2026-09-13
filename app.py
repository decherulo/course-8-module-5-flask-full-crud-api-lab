from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# Welcome route - confirms the API is running
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Events API"})

# Return all events as a JSON array
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify([event.to_dict() for event in events])

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    # Task 2 - Design and Develop the Code
    data = request.get_json()

    # Task 3 - Implement the Loop and Process Each Element
    # Guard clause: reject the request early if no title was sent
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    # New ID = one more than the current highest ID, so it stays unique
    # even after events are deleted
    new_id = max((e.id for e in events), default=0) + 1
    new_event = Event(new_id, data["title"])
    events.append(new_event)

    # Task 4 - Return and Handle Results
    # 201 Created tells the client the new resource now exists
    return jsonify(new_event.to_dict()), 201

# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # Task 2 - Design and Develop the Code
    data = request.get_json()

    # Task 3 - Implement the Loop and Process Each Element
    # Search through events for the one matching this ID
    event = next((e for e in events if e.id == event_id), None)

    if event is None:
        return jsonify({"error": "Event not found"}), 404

    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    event.title = data["title"]

    # Task 4 - Return and Handle Results
    return jsonify(event.to_dict()), 200

# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # Task 2 - Design and Develop the Code
    global events

    # Task 3 - Implement the Loop and Process Each Element
    event = next((e for e in events if e.id == event_id), None)

    if event is None:
        return jsonify({"error": "Event not found"}), 404

    events = [e for e in events if e.id != event_id]

    # Task 4 - Return and Handle Results
    # 204 No Content: successful delete, nothing to send back
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
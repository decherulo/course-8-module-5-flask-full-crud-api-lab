# Events API — Flask Full CRUD RESTful API

A simple RESTful API built with Flask that manages a list of events. It supports full CRUD operations (Create, Read, Update, Delete) using an in-memory data store, and returns structured JSON responses with appropriate HTTP status codes.

## Purpose

This API allows a client to manage event records — for example, adding new events, viewing existing ones, updating an event's title, or removing an event entirely. It was built to practice RESTful route design, JSON request/response handling, and HTTP status code conventions using Flask.

## Routes

| Method | Route             | Description                          |
|--------|-------------------|--------------------------------------|
| GET    | `/`               | Returns a welcome message            |
| GET    | `/events`         | Returns a list of all events         |
| POST   | `/events`         | Creates a new event                  |
| PATCH  | `/events/<id>`    | Updates the title of an existing event |
| DELETE | `/events/<id>`    | Deletes an event                     |

## Example Requests and Responses

### GET /
**Response (200 OK)**
```json
{ "message": "Welcome to the Events API" }
```

### GET /events
**Response (200 OK)**
```json
[
  { "id": 1, "title": "Tech Meetup" },
  { "id": 2, "title": "Python Workshop" }
]
```

### POST /events
**Request Body**
```json
{ "title": "Hackathon" }
```
**Response (201 Created)**
```json
{ "id": 3, "title": "Hackathon" }
```
**Missing title (400 Bad Request)**
```json
{ "error": "Title is required" }
```

### PATCH /events/1
**Request Body**
```json
{ "title": "Updated Tech Meetup" }
```
**Response (200 OK)**
```json
{ "id": 1, "title": "Updated Tech Meetup" }
```
**Event not found (404 Not Found)**
```json
{ "error": "Event not found" }
```

### DELETE /events/2
**Response (204 No Content)**
No response body.

**Event not found (404 Not Found)**
```json
{ "error": "Event not found" }
```

## Running the Project

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask
python app.py
```

The server runs at `http://127.0.0.1:5000`.

## Notes

- Data is stored in memory (a Python list), so it resets each time the server restarts.
- All responses are formatted using Flask's `jsonify()`.
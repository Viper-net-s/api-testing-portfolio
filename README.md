# API testing: Postman + Python (pytest)

Automated checks for the public JSONPlaceholder API, written in two ways:
a Postman collection and Python tests with pytest and requests.

## What is checked
- GET /posts/1: status 200, response time, JSON fields
- POST /posts: status 201, id in the response
- GET /posts/9999: status 404 (negative test)

## How to run the Python tests
1. Create a virtual environment: `py -m venv .venv`
2. Install dependencies: `.venv\Scripts\python -m pip install -r requirements.txt`
3. Run: `.venv\Scripts\python -m pytest -v`

## How to run the Postman collection
Import the `.postman_collection.json` file into Postman and run it with Collection Runner.

## Notes
The response-time limit is set to 3 seconds: a strict limit made the test flaky because network speed varies.
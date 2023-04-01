# flask-mongodb-api
Flask application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource using a REST API.

Python version used : `3.10.6`

## Setup
1. Clone the repository
2. Create a virtual environment
3. Install the requirements
4. Create a `.env` file and add the following variables
```bash
MONGO_URI=<your_mongo_uri>
MONGO_DB_NAME=<your_mongo_dbname>
```

To install the required packages
```bash
pip  install -r requirements.txt
```
To Run the app
```bash
python app.py
```

The app will be availiable on http://localhost:8000/

## API Endpoints
1. GET /users - Returns a list of all users.
2. GET /users/<id> - Returns the user with the specified ID.
3. POST /users - Creates a new user with the specified data.
4. PUT /users/<id> - Updates the user with the specified ID with the new data.
5. DELETE /users/<id> - Deletes the user with the specified ID.

## Testing Results

![Alt text](screenshots/user_get.png?raw=true "GET")
![Alt text](screenshots/user_id_get.png?raw=true "GET ID")
![Alt text](screenshots/user_post.png?raw=true "POST")
![Alt text](screenshots/user_update.png?raw=true "PUT")
![Alt text](screenshots/user_delete.png?raw=true "DELETE")


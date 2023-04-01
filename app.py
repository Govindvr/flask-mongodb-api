import os
from bson import ObjectId
from flask import Flask, request, jsonify
import jsonschema
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


user_schema = {
    "type": "object",
    "properties": {
        '_id': {'type': 'integer'},
        'name': {'type': 'string'},
        'email': {'type': 'string'},
        'password': {'type': 'string'}
    },
    "required": ["_id","name", "email", "password"]
}

app = Flask(__name__)
client = MongoClient(os.getenv('MONGO_URI'))
db = client[os.getenv('MONGO_DB_NAME')]
collection = db[os.getenv('MONGO_DB_NAME')]

@app.route('/')
def index():
    return 'Hello World'

@app.route('/users',methods=['GET'])
def get_users():
    users = list(collection.find())
    return jsonify(users)

@app.route('/users/<int:id>',methods=['GET'])
def get_user_id(id):
    
    user = collection.find_one({'_id':id})
    print(user)
    return jsonify(user)

@app.route('/users',methods=['POST'])
def create_user():
    data = request.get_json()
    data = request.get_json()
    try:
        validation = jsonschema.validate(data, user_schema)
        if validation is None:
            collection.insert_one(data)
            return jsonify({'message': 'User created successfully'})
    except jsonschema.exceptions.ValidationError as e:
        return jsonify({'message': 'Validation failed {}'.format(e)})

@app.route('/users/<int:id>',methods=['PUT'])
def update_user(id):
    data = request.get_json()
    try:
        validation = jsonschema.validate(data, user_schema)
        if validation is None:
            collection.update_one({'_id':id},{'$set':data})
            return jsonify({'message': 'User Updated successfully'})
    except jsonschema.exceptions.ValidationError as e:
        return jsonify({'message': 'Validation failed {}'.format(e)})
    
@app.route('/users/<int:id>',methods=['DELETE'])
def delete_user(id):
    collection.delete_one({'_id':id})
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
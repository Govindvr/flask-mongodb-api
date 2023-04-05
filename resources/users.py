from flask import Blueprint, Response, request, jsonify
import jsonschema
from .db import collection, user_schema
from flask_restful import Resource

users = Blueprint('users', __name__)

# @users.route('/')
# def index():
#     return 'Hello World'

# @users.route('/users',methods=['GET'])
# def get_users():
#     users = list(collection.find())
#     return jsonify(users)

# @users.route('/users/<int:id>',methods=['GET'])
# def get_user_id(id):
    
#     user = collection.find_one({'_id':id})
#     print(user)
#     return jsonify(user)

# @users.route('/users',methods=['POST'])
# def create_user():
#     data = request.get_json()
#     data = request.get_json()
#     try:
#         validation = jsonschema.validate(data, user_schema)
#         if validation is None:
#             collection.insert_one(data)
#             return jsonify({'message': 'User created successfully'})
#     except jsonschema.exceptions.ValidationError as e:
#         return jsonify({'message': 'Validation failed {}'.format(e)})

# @users.route('/users/<int:id>',methods=['PUT'])
# def update_user(id):
#     data = request.get_json()
#     try:
#         validation = jsonschema.validate(data, user_schema)
#         if validation is None:
#             collection.update_one({'_id':id},{'$set':data})
#             return jsonify({'message': 'User Updated successfully'})
#     except jsonschema.exceptions.ValidationError as e:
#         return jsonify({'message': 'Validation failed {}'.format(e)})
    
# @users.route('/users/<int:id>',methods=['DELETE'])
# def delete_user(id):
#     collection.delete_one({'_id':id})
#     return jsonify({'message': 'User deleted successfully'})

class UsersApi(Resource):
    def get(self):
        users = list(collection.find())
        return users, 200
    
    def post(self):
        data = request.get_json()
        try:
            validation = jsonschema.validate(data, user_schema)
            if validation is None:
                collection.insert_one(data)
                return{'message': 'User created successfully'}
        except jsonschema.exceptions.ValidationError as e:
            return{'message': 'Validation failed {}'.format(e)}
        
class UserApi(Resource):
    def get(self,id):
        user = collection.find_one({'_id':id})
        return user, 200
    
    def put(self,id):
        data = request.get_json()
        print(data)
        try:
            validation = jsonschema.validate(data, user_schema)
            if validation is None:
                collection.update_one({'_id':id},{'$set':data})
                return {'message': 'User Updated successfully'}
        except jsonschema.exceptions.ValidationError as e:
            return {'message': 'Validation failed {}'.format(e)}
    
    def delete(self,id):
        collection.delete_one({'_id':id})
        return {'message': 'User deleted successfully'}
    


    """
       {
        "_id": 1,
        "name": "Danny",
        "email": "danny@email.com",
        "password": "fuhfbd"
    },
    {
        "_id": 2,
        "name": "Das",
        "email": "das@hello.com",
        "password": "sdhbcsc"
    },
    """
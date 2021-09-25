######################################################################################
# THIS IS Posting BLUEPRINT for posting page
#retriveing a user
######################################################################################
from flask import Blueprint, jsonify, request, session


def UserAPI(db) :
    userApi = Blueprint('userApi', __name__)

    @userApi.route('/users', methods=['GET'])
    def get_all_record():
        user = User.objects()
        if not user:
            return jsonify({'error': 'data not found'})
        else:
            return jsonify(user.to_json())
    @userApi.route('/users', methods=['GET'])
    def get_a_record():
        user = User.objects(name=record['email']).first()
        if not user:
            return jsonify({'error': 'data not found'})
        else:
            return jsonify(user.to_json())
    @userApi.route('/users', methods=['POST'])
    def create_record():
        record = json.loads(request.data)
        user = User(name=record['email'], email=record['password'])
        user.save()
        return jsonify(user.to_json())

    @userApi.route('/<username>', methods=['PUT'])
    def update_record():
        record = json.loads(request.data)
        user = User.objects(name=record['email']).first()
        if not user:
            return jsonify({'error': 'data not found'})
        else:
            user.update(email=record['email'])
        return jsonify(user.to_json())


    
        
    return userApi
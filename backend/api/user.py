######################################################################################
# THIS IS Posting BLUEPRINT for posting page
#retriveing a user
######################################################################################
from flask import Blueprint, jsonify, request, session
import json


def UserAPI(User) :
    userApi = Blueprint('userApi', __name__)

    @userApi.route('/api/users', methods=['GET'])
    def get_all_record():
        user = User.objects()
        if not user:
            return jsonify({'error': 'data not found'})
        else:
            return jsonify(user.to_json())
    @userApi.route('/api/<username>', methods=['GET'])
    def get_a_record(username):
        record = {}
        record['email'] = username
        user = User.objects(email=record['email']).first()
        if not user:
            return jsonify({'error': 'data not found'})
        else:
            return jsonify(user.to_json())
    @userApi.route('/api/users', methods=['POST'])
    def create_record():
        record = json.loads(request.get_data())
        user = User(email=record['email'], password=record['password'] , stack = record['stack'])
        user.save()
        return jsonify(user.to_json())


    @userApi.route('/api/<username>', methods=['PUT'])
    def update_record(username):
        record['email'] = username
        user = User.objects(email=record['email']).first()
        if not user:
            return jsonify({'error': 'data not found'})
        else:
            user.update(email=record['email'])
        return jsonify(user.to_json())
    
    @userApi.route('/api/login', methods=['POST'])
    def verify_record():
        if request.method == 'POST':
            record = json.loads(request.get_data())
            email =record['email']
            password = record['password']
        check_user = User.objects(email=record['email']).first()
        if check_user :
            if check_user['password'] == password  :
                return jsonify(check_user.to_json())
            else :
                return jsonify({'error': 'password is incorrect'})
        if not check_user :
            return jsonify({'error': 'user is incorrect'})

    @userApi.route('/filter', methods=['POST'])
    def find_a_record():
        if request.method == 'POST':
            record = json.loads(request.get_data())
            stack =record['stack']
        same_tech = []
        for u in User :
            if stack in u['stack'] :
                same_tech.append(u)
        return jsonify({'users' : same_tech })
        
    return userApi
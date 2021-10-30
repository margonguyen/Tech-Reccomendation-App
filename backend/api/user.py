######################################################################################
# THIS IS Posting BLUEPRINT for posting page
#retriveing a user
######################################################################################
from flask import Blueprint, jsonify, request, session
import json
import datetime
import jwt
from functools import wraps
from flask_jwt_extended import create_access_token


def UserAPI(User) :
    userApi = Blueprint('userApi', __name__)

    def token_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None

            if 'Authorization' in request.headers:
                token = request.headers['Authorization']

            if not token:
                return jsonify({'message' : 'Token is missing!'}), 401

            try: 
                print("SSS")
                data = jwt.decode(token, 'SECRET', algorithms=["HS256"])
                print(data)
                current_user = User.objects(email=data['email']).first()
            except:
                return jsonify({'message' : 'Token is invalid!'}), 401

            return f(current_user, *args, **kwargs)

        return decorated
    @userApi.route('/', methods=['GET'])
    def get_Home():
        return jsonify({'message': 'sucess in api'})

    @userApi.route('/api/users', methods=['GET'])
    def get_all_record():
        user = User.objects()
        if not user:
            return jsonify({'error': 'data not found'})
        else:
            all = []
            for u in user :
                all.append(u.to_json())
            return jsonify(all)
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
        print("SSSS")
        record = json.loads(request.get_data())
        print(record)
        user = User(email=record['email'], password=record['password'] , stack = record['stack'])
        user.save()
        return jsonify(user.to_json())


    @userApi.route('/api/<username>', methods=['PUT'])
    @token_required
    def update_record(u,username):
        record['email'] = username
        user = User.objects(email=record['email']).first()
        if not user:
            return jsonify({'error': 'data not found'})
        else:
            user.update(email=record['email'])
        return jsonify(user.to_json())
    
    @userApi.route('/api/login', methods=['POST', 'GET'])
    def verify_record():
        if request.method == 'GET':
            return jsonify({'message' : ' sucess in login api'})
        if request.method == 'POST':
            record = json.loads(request.get_data())
            email =record['email']
            password = record['password']
        check_user = User.objects(email=record['email']).first()
        #CHecking if password is match
        if check_user :
            if check_user['password'] == password  :
                token = jwt.encode({'email' : email}, "SECRET" )
                return jsonify({'token' : token })
            else :
                return jsonify({'error': 'password is incorrect'})
        if not check_user :
            return jsonify({'error': 'user is incorrect'})


    @userApi.route('/api/signup', methods=['POST', 'GET'])
    def verify_signup():
        if request.method == 'GET':
            return jsonify({'message' : ' sucess in signup api'})
        if request.method == 'POST':
            record = json.loads(request.get_data())
            email =record['email']
            password = record['password']
            stack = record['stacks']
            if 'project' in record :
                project = record['project']
        check_user = User.objects(email=record['email']).first()
        #CHecking if password is match
        if check_user :
            if check_user['password'] == password  :
                token = jwt.encode({'email' : email}, "SECRET" )
                return jsonify({'token' : token })
            else :
                return jsonify({'error': 'password is incorrect'})
        if not check_user :
            return jsonify({'error': 'user is incorrect'})
    

    @userApi.route('/filter', methods=['POST','GET'])
    # @token_required
    def find_a_record():
        if request.method == 'GET' :
            return jsonify({'messsage' : 'success to get filter'})
        if request.method == 'POST':
            record = json.loads(request.get_data())
            print(record)
            stack =record['stack']
        same_tech = []
        user = User.objects()
        for u in user :
            if stack in u['stack'] :
                same_tech.append(u)
        return jsonify({'users' : same_tech })
        
    return userApi
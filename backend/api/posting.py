######################################################################################
# THIS IS Posting BLUEPRINT for posting page
#retriveing a posting 
# /posting/<postingid>
######################################################################################
from flask import Blueprint, jsonify

def PostingAPI(Posting) :
    postApi = Blueprint('postingApi', __name__)

    @postApi.route('/api/postings')
    def get_all_record():
        post = Posting.objects()
        if not user:
            return jsonify({'error': 'data not found'})
        else:
            return jsonify(post.to_json())
    
    @postApi.route('/api/postings/<postid>')
    def get_a_record(postid):
        post = Posting.objects(post_id=postid).first()
        if not post:
            return jsonify({'error': 'data not found'})
        else:
            return jsonify(post.to_json())    
    @postApi.route('/api/postings/<postid>')
    def create_a_record():
        record = json.loads(request.get_data())
        post = Posting(post_name= record['name'], description = record['description'])
        post.save()
        return jsonify(post.to_json()) 
        
    return postApi
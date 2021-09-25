######################################################################################
# THIS IS Posting BLUEPRINT for posting page
#retriveing a posting 
# /posting/<postingid>
######################################################################################
from flask import Blueprint, jsonify

def PostingAPI(db) :
    postApi = Blueprint('postingApi', __name__)

    @postApi.route('/api/posting/<postid>')
    def getPostAPI(postid):
        post = db.post.getAPosting("postID", postid)
        posts = db.post.getPostingOrganizedData(post)
        return jsonify({"posting" : posts})
    
    @postApi.route('/api/postings')
    def getAllPostAPI():
        postings = db.post.getAllPostings()
        posts = db.post.getPostingOrganizedData(postings)
        return jsonify({"postings" : posts})
    
        
    return postApi
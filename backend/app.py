#Using blue print to structure the file
#Blueprint is the collection of views , static file and template
#In this application, the structure is divided  by its function
#The blueprint in views folder collections of views
#The same static files will be used for the views in most of the blueprints
# Most of the templates will extend a master template

from flask import Flask
# from views.home import initHome
# from views.posting import initPost
# from views.dashboard import initDashBoard
# from views.profile import profile
# from views.message import initChat

## Database model 
from model.user import User
from model.posting import Posting
# mongodb
from flask_mongoengine import MongoEngine

from api.posting import PostingAPI
from api.user import UserAPI
from datetime import timedelta
# from db import SearchingDB
from flask import send_from_directory

from flask_socketio import SocketIO


socket_io = SocketIO()

#Initialize flask app
app = Flask(__name__)

# Setting key for session
app.config.from_object('config.Config')
app.config.from_object('config.DevConfig')

# Setting app session
app.permanent_session_lifetime=timedelta(days=1)

#Initialize db
db = MongoEngine(app)

# Passing db to all the api blueprints & get blueprints
user_API = UserAPI(User)
post_Api = PostingAPI(Post)

########## All the blue print is inside the views application #######
# Register blueprint
app.register_blueprint(user_API)
app.register_blueprint(post_API)




socket_io.init_app(app)

if __name__ == "__main__":
    socket_io.run(app, debug=True)
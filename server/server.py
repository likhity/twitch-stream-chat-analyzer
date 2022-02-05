from flask import Flask, request
from flask_restful import Api, Resource
from flask_socketio import SocketIO
from flask_cors import CORS, cross_origin
# from sentiment import Analyzer

app = Flask(__name__)
# api = Api(app)
CORS(app, supports_credentials=True)
socketio = SocketIO(app, cors_allowed_origins='*')

# class HelloWorld(Resource):
#   def get(self):
#     print(request.form['channel'])
#     return { "data": "Hello World!" }
#     #self.analyzer = Analyzer()

# api.add_resource(HelloWorld, "/helloworld")

@socketio.on("connection")
def handle_connection(data):
  print(data.user + '\n')
  # print(data.numMessages + '\n')

@socketio.on('message')
def handle_message(data):
  print(data['msg'])
  #at this point we also want to have recieved the numcomments update
  #access the dropdown
  # self.analyzer.setNumComments(numComments)
  # self.analyzer.recieve(data)

if __name__ == "__main__":
  socketio.run(app)
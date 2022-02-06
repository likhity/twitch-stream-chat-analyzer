from flask import Flask, request
from flask_restful import Api, Resource
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from sentiment import Analyzer

app = Flask(__name__)
# api = Api(app)
CORS(app, supports_credentials=True)
socketio = SocketIO(app, cors_allowed_origins='*')
analyzer = Analyzer()

@socketio.on("connection")
def handle_connection(data):
  # print(data.numMessages + '\n')
  numComments = int(data['numMessages'])
  analyzer.setNumComments(numComments)

@socketio.on('message')
def handle_message(data):
  #at this point we also want to have recieved the numcomments update
  #access the dropdown
  msg = data['msg']
  analyzer.recieve(msg, data['streamer'])
  emit("percentage-update", analyzer.getSentiment())
  print(data['streamer'] + " " + str(analyzer.getSentiment()))
  

@socketio.on('changeNumMessages')
def change_dropdown(data):
  numComments = int(data['numMessages'])
  analyzer.setNumComments(numComments)

if __name__ == "__main__":
  socketio.run(app)
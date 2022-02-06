from flask import Flask, request
from flask_restful import Api, Resource
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask_cors import CORS
from sentiment import Analyzer

app = Flask(__name__)
# api = Api(app)
CORS(app, supports_credentials=True)
socketio = SocketIO(app, cors_allowed_origins='*')

clients = []

@socketio.on("connection")
def handle_connection(data):
  # print(data.numMessages + '\n')
  numComments = int(data['numMessages'])
  new_analyzer = Analyzer()
  new_analyzer.setNumComments(numComments)
  new_client = {
    'id': request.sid,
    'analyzer': new_analyzer
  }
  clients.append(new_client)
  join_room(request.sid)
  # print(clients)

@socketio.on("disconnect")
def handle_disconnect():
  client_index = next((i for i, item in enumerate(clients) if item["id"] == request.sid), None)
  del clients[client_index]
  leave_room(request.sid)
  # print(clients)

@socketio.on('message')
def handle_message(data):
  #at this point we also want to have recieved the numcomments update
  #access the dropdown
  emit("test-event", "test-string " + request.sid, to=request.sid)
  msg = data['msg']
  client_analyzer = next((item for item in clients if item['id'] == request.sid), None)['analyzer']
  client_analyzer.recieve(msg)
  emit("percentage-update", client_analyzer.getSentiment(), to=request.sid)
  
@socketio.on('changeNumMessages')
def change_dropdown(data):
  numComments = int(data['numMessages'])
  client_analyzer = next((item for item in clients if item['id'] == request.sid), None)['analyzer']
  client_analyzer.setNumComments(numComments)

if __name__ == "__main__":
  socketio.run(app)
from flask import Flask, request
from flask_restful import Api, Resource
from flask_socketio import SocketIO

app = Flask(__name__)
api = Api(app)
socketio = SocketIO(app)

class HelloWorld(Resource):
  def get(self):
    print(request.form['channel'])
    return { "data": "Hello World!" }

api.add_resource(HelloWorld, "/helloworld")

@socketio.on('message')
def handle_message(data):
  print('recieved message: ' + data)

if __name__ == "__main__":
  app.run(debug=True)
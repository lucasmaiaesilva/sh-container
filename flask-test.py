from flask import Flask, render_template
from flask.ext.socketio import SocketIO
# import json

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
  return render_template('index.html',)

@socketio.on('connect')
def test_connect():
    print('test')
    emit('my response', {'data': 'Connected'})

if __name__ == "__main__":
  socketio.run(app)

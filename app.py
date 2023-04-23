from flask import Flask, render_template
from flask_socketio import SocketIO
import time, csv



app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'
socket = SocketIO(app)

def unpack_csv(filename):
    myfile = open(filename, 'r')
    print("-I- Creating CSV reader object...")
    lines = csv.reader(myfile)
    return lines

alldata = unpack_csv('ProcessedData/sample.csv')
header_info = next(alldata)


@socket.on('message')
def handlemsg(msg):
    time.sleep(1)
    new_msg = next(alldata)
    socket.send(new_msg)
    print('-I- Sent: ')
        
@app.route('/')
def main():
    return render_template('main.html', headers=header_info, datalen = len(header_info))


if __name__ == '__main__':
    socket.run(app)
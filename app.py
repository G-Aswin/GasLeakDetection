from flask import Flask, render_template
from flask_socketio import SocketIO
import time, csv, os
import pandas as pd



app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'
socket = SocketIO(app)

def unpack_csv(filename):
    myfile = open(filename, 'r')
    print("-I- Creating CSV reader object...")
    lines = csv.reader(myfile)
    return lines

def aggregate_processed_data():
    dflist = []
    # All processed data present in Data/ProcessedRawData with a format of .*_dat.csv
    for filename in os.listdir('Data/ProcessedRawData'):
        if '_dat.csv' in filename:
            df = pd.read_csv('Data/ProcessedRawData/' + filename)
            dflist.append(df)
            
    combined_df = pd.concat(dflist, ignore_index=True)
    return combined_df

cdf = aggregate_processed_data()
i = 0
header_info = cdf.columns



@socket.on('message')
def handlemsg(msg):
    global i
    time.sleep(1)
    new_msg = cdf.iloc[i].tolist()
    mod_new_msg = []
    for ele in new_msg:
        mod_new_msg.append(str(ele))
    new_msg = mod_new_msg
    print("********************************************************************************")
    print(new_msg, type(new_msg))
    i += 1
    socket.send(new_msg)
    print('-I- Sent: ', new_msg)
        
@app.route('/')
def main():
    return render_template('main.html', headers=header_info, datalen = len(header_info))


if __name__ == '__main__':
    socket.run(app)
    # print(cdf.sample(n=3))
    # print(cdf.info())
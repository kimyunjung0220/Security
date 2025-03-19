from flask import Flask, render_template, Response, request
import time
import capture
#import test

app = Flask(__name__)
count = 0

white_list = ['192.168.111.128', '127.0.0.1']

@app.before_request
def acsses_ctl():
    if request.remote_addr not in white_list:
        return "Access Denied"
        
def collect_data():
    packet = capture.sniffing()
    print("I got a packet : \n", packet)
    print("\n endpoint")
    return packet

def packet_capture():
    while True:
        data = collect_data()
        yield f"data: {[str(data)]}\n\n"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/packet')
def sse():
    return Response(packet_capture(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
#help me.... I sick my brain..
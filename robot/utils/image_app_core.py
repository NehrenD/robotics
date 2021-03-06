import time
from multiprocessing import Process,Queue

from flask import Flask,render_template,Response

app = Flask(__name__,template_folder='../resources/templates')
control_queue = Queue()
display_queue = Queue()
display_template = 'image_server.html'

@app.route('/')
def index():
    return render_template(display_template)

@app.route('/display')
def display():
    return Response(frame_generator(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/control/<control_name>')
def control(control_name):
    control_queue.put(control_name)
    return Response('queued')

def frame_generator():

    while True:
        time.sleep(0.05)
        encoded_bytes = display_queue.get()
        yield b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + encoded_bytes + b'\r\n'


def start_server_process(template_name):
    global display_template
    display_template = template_name
    server = Process(target=app.run,kwargs={"host":"0.0.0.0","port": 5001})
    server.start()
    return server

def put_output_image(encoded_bytes):
    if display_queue.empty():
        display_queue.put(encoded_bytes)


def get_control_instruction():

    if control_queue.empty():
        return None
    else:
        return control_queue.get()


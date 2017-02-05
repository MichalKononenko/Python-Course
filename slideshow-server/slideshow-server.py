from flask import Flask, send_file, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return 'The server is up'

@app.route('/lectures/0', methods=["GET"])
def get_lecture_0():
    return send_file( 
        '../lectures/lecture_0_course_outline_and_installation/slideshow.html'
    )

@app.route('/static/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static', filename))

if __name__ == '__main__':
    app.run()

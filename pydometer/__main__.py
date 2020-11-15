from flask import Flask, requests

app = Flask(__name__)

@app.route('/uploads', methods=['GET'])
def get_uploads():
    pass

@app.route('/upload/*', methods=['GET'])
#TODO: is this right?
def get_upload():
    pass

@app.route('/create', methods=['POST'])
def create():
    pass

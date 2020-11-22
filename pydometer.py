#!/usr/bin/env python3

from flask import Flask, request, render_template
from gevent.pywsgi import WSGIServer
import logging

from pydometer.models.upload import Upload
from pydometer.models.pipeline import Pipeline
from pydometer.helpers.view_helper import ViewHelper

app = Flask(__name__)
app.add_template_global(Upload, 'Upload')
app.add_template_global(ViewHelper, 'ViewHelper')

@app.route('/uploads', methods=['GET'])
def get_uploads():
    #TODO: @error = "A #{params[:error]} error has occurred." if params[:error]
    pipelines = [Pipeline(open(upload.file_path).read(), upload.user, upload.trial) for upload in Upload.all()]
    return render_template('uploads.html', pipelines=pipelines)

@app.route('/upload/<path:file_path>', methods=['GET'])
def get_upload(file_path):
    upload = Upload.find(file_path)
    pipeline = Pipeline(open(file_path).read(), upload.user, upload.trial)
    return render_template('upload.html', pipeline=pipeline)

@app.route('/create', methods=['POST'])
def create():
    pass #TODO

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    LISTEN = ('localhost', 8000)
    http_server = WSGIServer(LISTEN, app)
    print(f"Serving on http://{LISTEN[0]}:{LISTEN[1]}/uploads")
    http_server.serve_forever()

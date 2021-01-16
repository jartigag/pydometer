#!/usr/bin/env python3

from flask import Flask, request, render_template, redirect
from gevent.pywsgi import WSGIServer
import logging

from models.upload import Upload
from models.pipeline import Pipeline
from helpers.view_helper import ViewHelper

app = Flask(__name__)
app.add_template_global(Upload, 'Upload')
app.add_template_global(ViewHelper, 'ViewHelper')

app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 # max. file size = 1MB
#app.config['UPLOAD_EXTENSIONS'] = ['.csv', '.txt']
app.config['UPLOAD_PATH'] = Upload.UPLOAD_DIRECTORY

@app.route('/uploads', methods=['GET'])
def get_uploads():
    error_description = f": {request.args.get('errdescr')}." if request.args.get('errdescr') else "."
    error = f"A {request.args.get('error')} error has occurred{error_description}" if request.args.get('error') else ""
    pipelines = [Pipeline(open(upload.file_path).read(), upload.user, upload.trial) for upload in Upload.all()]
    return render_template('uploads.html', pipelines=pipelines, error=error)

@app.route('/upload/<path:file_path>', methods=['GET'])
def get_upload(file_path):
    upload = Upload.find(file_path)
    pipeline = Pipeline(open(file_path).read(), upload.user, upload.trial)
    return render_template('upload.html', pipeline=pipeline)

@app.route('/create', methods=['POST'])
def create():
    try:
        form = request.form.to_dict()
        #TODO: prevent public/uploads/None-None-74.0_x-None-None.txt from happening
        params = {
            'trial': {'name': form['trial[name]'], 'rate': form['trial[rate]'], 'steps': form['trial[steps]']},
            'user': {'gender': form['user[gender]'], 'height': form['user[height]'], 'stride': form['user[stride]']}
        }
        tempfile = request.files['data'].filename
        #Upload.create(tempfile, params['user'], params['trial'])
        datafile = request.files['file']
        if datafile.filename:
            upload = Upload.create(tempfile, params['user'], params['trial'])
            datafile.save(upload.file_path)

        return redirect('/uploads')
    except Exception as e:
        return redirect(f'/uploads?error=creation&errdescr={e}')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    LISTEN = ('localhost', 8000)
    httpd = WSGIServer(LISTEN, app)
    print(f"Serving on http://{LISTEN[0]}:{LISTEN[1]}/uploads")
    httpd.serve_forever()

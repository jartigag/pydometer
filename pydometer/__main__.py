from flask import Flask, request, render_template
from gevent.pywsgi import WSGIServer
import logging

from pydometer.models.upload import Upload
from pydometer.models.pipeline import Pipeline

app = Flask(__name__)

@app.route('/uploads', methods=['GET'])
def get_uploads():
    #TODO: @error = "A #{params[:error]} error has occurred." if params[:error]
    pipelines = [Pipeline(open(upload.file_path).read(), upload.user, upload.trial) for upload in Upload.all()]
    return render_template('views/uploads.html', pipelines=pipelines)

@app.route('/upload/*', methods=['GET'])
#TODO: is this right?
def get_upload():
    pass

@app.route('/create', methods=['POST'])
def create():
    pass

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    LISTEN = ('localhost', 8000)
    http_server = WSGIServer(LISTEN, app)
    print(f"Serving on http://{LISTEN[0]}:{LISTEN[1]}/uploads")
    http_server.serve_forever()

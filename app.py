from flask import Flask, flash, request, render_template, render_template_string, abort
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp3'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.secret_key = 'my_secret_key'

@app.route('/')
def hello():
    return 'Please enter a song.'

@app.route('/sample')
def sample():
    return 'Now sampling...'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('File not found', 'error')
            '''return render_template('upload.html', message='No file part')'''
        file = request.files['file']
        if file.filename == '':
            flash('No selected file', 'error')
            '''return render_template('upload.html', message='No selected file')'''
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File uploaded successfully!', 'success')
            list_of_files = os.listdir(app.config['UPLOAD_FOLDER'])
            return render_template('upload.html', files=list_of_files)
        '''else: abort(400, description="File type not allowed")'''
        flash('Invalid file type', 'error')
    list_of_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('upload.html', files=list_of_files)

'''
return 
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
'''

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)

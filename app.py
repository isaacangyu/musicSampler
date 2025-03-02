<<<<<<< HEAD
from flask import Flask, flash, redirect, request, render_template, render_template_string, abort, url_for
=======
from flask import Flask, flash, request, render_template, render_template_string, abort, redirect, url_for
>>>>>>> 0279604f78c501ec04d7ad414872198e6d99d252
import os
from werkzeug.utils import secure_filename
from blocks import Block  # Import the Block class

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
        file = request.files['file']
        if file.filename == '':
            flash('No selected file', 'error')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File uploaded successfully!', 'success')
            list_of_files = os.listdir(app.config['UPLOAD_FOLDER'])
            return render_template('upload.html', files=list_of_files)
        flash('Invalid file type', 'error')
    list_of_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('upload.html', files=list_of_files)

<<<<<<< HEAD
def index():
    text = ""
    if request.method == "POST":
        text = request.form["text"]
        # Process the text with newlines here (e.g., save to a file or database)
    return render_template("upload.html", text=text)



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
=======
@app.route('/create_block', methods=['POST'])
def create_block():
    block_name = request.form['block_name']
    start_time = int(request.form['start_time'])
    end_time = int(request.form['end_time'])
    block_type = request.form['block_type']
    audio_file = request.form['audio_file']
    duration = request.form.get('duration', type=int)

    if block_type != "Empty" and not audio_file:
        flash('Audio file is required for non-empty blocks', 'error')
        return redirect(url_for('upload_file'))

    if block_type == "Empty" and not duration:
        flash('Duration is required for empty blocks', 'error')
        return redirect(url_for('upload_file'))

    if audio_file:
        audio_file_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_file)
    else:
        audio_file_path = None

    block = Block(
        name = block_name,
        start = start_time*1000,
        end = end_time*1000,
        block_type = block_type,
        audio_file = audio_file_path,
        duration = 1000*(end_time - start_time)
    )

    flash(f'Block "{block_name}" created successfully!', 'success')
    return redirect(url_for('upload_file'))
>>>>>>> 0279604f78c501ec04d7ad414872198e6d99d252

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)

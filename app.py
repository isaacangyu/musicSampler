from flask import Flask, flash, request, render_template, render_template_string, abort, redirect, send_file, url_for
import os
import json
from werkzeug.utils import secure_filename
from blocks import Block  # Import the Block class
import random

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
BLOCKS_FILE = 'blocks.json'
ALLOWED_EXTENSIONS = {'mp3'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.secret_key = 'my_secret_key'

# Load blocks from file (if it exists)
def load_blocks():
    if os.path.exists(BLOCKS_FILE) and os.path.getsize(BLOCKS_FILE) > 0:
        try:
            with open(BLOCKS_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            # If the file is malformed, return an empty dictionary
            return {}
    else:
        # If the file doesn't exist or is empty, return an empty dictionary
        return {}

# Save blocks to file
def save_blocks(blocks):
    with open(BLOCKS_FILE, 'w') as f:
        json.dump(blocks, f, indent=4)

# Initialize blocks dictionary
blocks = load_blocks()

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
    # Load existing blocks
    blocks = load_blocks()

    # Handle file upload
    if request.method == 'POST':
        # Check if the request is for file upload
        if 'file' in request.files:
            file = request.files['file']
            if file.filename == '':
                flash('No selected file', 'error')
            elif file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                flash('File uploaded successfully!', 'success')

        # Check if the request is for block creation
        elif 'block_name' in request.form:
            block_name = request.form['block_name']
            start_time = int(request.form['start_time'])
            end_time = int(request.form['end_time'])
            block_type = request.form['block_type']
            audio_file = request.form['audio_file']
            duration = request.form.get('duration', type=int)

            # Validate input
            if block_type != "Empty" and not audio_file:
                flash('Audio file is required for non-empty blocks', 'error')
            elif block_type == "Empty" and not duration:
                flash('Duration is required for empty blocks', 'error')
            else:
                # Set audio file path
                if audio_file:
                    audio_file_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_file)
                else:
                    audio_file_path = None

                # Create a new Block object
                block = Block(
                    name=block_name,
                    start=start_time * 1000,  # Convert to milliseconds
                    end=end_time * 1000,  # Convert to milliseconds
                    block_type=block_type,
                    audio_file=audio_file_path,
                    duration=1000 * (end_time - start_time)  # Convert to milliseconds
                )

                # Add the block to the dictionary
                blocks[block_name] = block.to_dict()

                # Save the updated blocks dictionary to the JSON file
                save_blocks(blocks)

                # Flash success message
                flash(f'Block "{block_name}" created successfully!', 'success')


        elif 'play_block' in request.form:
            block_name = request.form['play_block']
            if block_name in blocks:
                block_data = blocks[block_name]

                block = Block(
                    name=str(random.randint(1,100000)) +block_data['name'],
                    start=block_data['start'],
                    end=block_data['end'],
                    block_type=block_data['block_type'],
                    audio_file=block_data['audio_file'],
                    duration=block_data['duration']
                )
                
                # Call the play method
                block.play()
                flash(f'Playing block: {block_name}', 'success')
            else:
                flash(f'Block "{block_name}" not found', 'error')

    # Get the list of uploaded files
    list_of_files = os.listdir(app.config['UPLOAD_FOLDER'])

    # Render the template with the files and blocks data
    return render_template('upload.html', files=list_of_files, blocks=blocks)


def index():
    text = ""
    if request.method == "POST":
        text = request.form["text"]
        # Process the text with newlines here (e.g., save to a file or database)
    return render_template("upload.html", text=text)

def download_mp3():
        # Path to your MP3 file
        mp3_path = 'faded.mp3' 
        
        # Send the file as an attachment
        return send_file(mp3_path, as_attachment=True, download_name='exported_audio.mp3')

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
    
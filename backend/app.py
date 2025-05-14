from flask import Flask, request, jsonify
import sqlite3
import os
from werkzeug.utils import secure_filename
from mutagen import File

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['DATABASE'] = 'mydatabase.db'

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Initialize the database
def init_db():
    with sqlite3.connect(app.config['DATABASE']) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS metadata (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                metadata TEXT NOT NULL
            )
        ''')
        conn.commit()

init_db()

# Function to save metadata to the database
def save_metadata(filename, metadata):
    with sqlite3.connect(app.config['DATABASE']) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO metadata (filename, metadata)
            VALUES (?, ?)
        ''', (filename, metadata))
        conn.commit()

# Function to retrieve metadata from the database
def get_metadata(filename):
    with sqlite3.connect(app.config['DATABASE']) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT metadata FROM metadata
            WHERE filename = ?
        ''', (filename,))
        result = cursor.fetchone()
        return result[0] if result else None

# Route to handle file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        metadata = extract_metadata(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        save_metadata(filename, metadata)
        return jsonify({'message': 'File uploaded successfully', 'metadata': metadata}), 200

# Function to extract metadata from a file
def extract_metadata(filepath):
    media_file = File(filepath)
    metadata = {}
    for key, value in media_file.tags.items():
        metadata[key] = str(value)
    return metadata

# Route to retrieve metadata
@app.route('/metadata/<filename>', methods=['GET'])
def metadata(filename):
    metadata = get_metadata(filename)
    if metadata:
        return jsonify({'metadata': metadata}), 200
    else:
        return jsonify({'error': 'Metadata not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

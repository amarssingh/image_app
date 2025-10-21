from flask import Flask, render_template, request, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads')
OUTPUT_IMAGE_PATH = os.path.join('static', 'output.jpg')

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    input_image_path = None
    output_image_path = None

    if request.method == 'POST':
        if 'image' not in request.files:
            return render_template('index.html', error="No file uploaded")

        file = request.files['image']
        if file.filename == '':
            return render_template('index.html', error="No file selected")

        filename = secure_filename(file.filename)
        input_image_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(input_image_path)

        # Convert to URL paths for rendering in HTML
        input_image_path = url_for('static', filename=f'uploads/{filename}')
        output_image_path = url_for('static', filename='output.jpg')

    return render_template('index.html',
                           input_image=input_image_path,
                           output_image=output_image_path)

if __name__ == "__main__":
    app.run(debug=True)

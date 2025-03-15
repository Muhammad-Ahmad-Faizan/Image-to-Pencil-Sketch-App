from flask import Flask, render_template, request, send_file, url_for, after_this_request, flash, redirect
import cv2
import os
import imghdr

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

UPLOAD_FOLDER = "static/uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files.get('image')

        if not file or file.filename == '':
            flash("No file uploaded!", "error")
            return redirect(url_for('home'))

        if not allowed_file(file.filename):
            flash("Unsupported file format! Please upload a JPG or PNG image.", "error")
            return redirect(url_for('home'))

        filename = "uploaded.jpg"
        img_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(img_path)

        # Validate if it's a real image
        if imghdr.what(img_path) not in ALLOWED_EXTENSIONS:
            os.remove(img_path)
            flash("Invalid image file!", "error")
            return redirect(url_for('home'))

        # Convert image to sketch
        sketch_path = convert_to_sketch(img_path)

        if not sketch_path:
            flash("Failed to create sketch!", "error")
            return redirect(url_for('home'))

        return render_template('index.html', 
                               image=url_for('static', filename='uploads/uploaded.jpg'), 
                               sketch=url_for('static', filename='uploads/sketch.jpg'))

    return render_template('index.html', image=None, sketch=None)


def convert_to_sketch(img_path):
    """Converts an image to a pencil sketch and saves it."""
    if not os.path.exists(img_path):
        return None

    image = cv2.imread(img_path)
    if image is None:
        return None

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted = cv2.bitwise_not(gray)
    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
    inverted_blur = cv2.bitwise_not(blurred)
    sketch = cv2.divide(gray, inverted_blur, scale=256.0)

    sketch_path = os.path.join(UPLOAD_FOLDER, "sketch.jpg")
    cv2.imwrite(sketch_path, sketch)

    return sketch_path


@app.route('/download/<filename>')
def download_file(filename):
    """Allows users to download the sketch and deletes stored images after downloading."""
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(file_path):
        return "File not found", 404

    @after_this_request
    def remove_files(response):
        """Deletes images after download is complete."""
        try:
            for file in ["uploaded.jpg", "sketch.jpg"]:
                file_to_remove = os.path.join(UPLOAD_FOLDER, file)
                if os.path.exists(file_to_remove):
                    os.remove(file_to_remove)
        except Exception as e:
            print(f"Error deleting files: {e}")  
        return response

    return send_file(file_path, as_attachment=True)

@app.route('/clear')
def clear_images():
    """Clears the uploaded and sketched images."""
    try:
        for file in ["uploaded.jpg", "sketch.jpg"]:
            file_to_remove = os.path.join(UPLOAD_FOLDER, file)
            if os.path.exists(file_to_remove):
                os.remove(file_to_remove)
        flash("Images cleared!", "success")
    except Exception as e:
        flash(f"Error clearing images: {e}", "error")

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

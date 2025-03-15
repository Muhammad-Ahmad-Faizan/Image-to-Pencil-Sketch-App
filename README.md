**#Image to Pencil Sketch App**
This is a web application that converts an image into a pencil sketch using OpenCV and Python. The app provides an intuitive interface where users can upload an image, generate a sketch, and download the final output.
✨ Features

    📤 Upload an image and convert it into a pencil sketch
    📥 Download the sketched image
    🖥️ Simple and user-friendly UI
    🔧 Built with Flask, OpenCV, and HTML/CSS

🛠️ Installation
1️⃣ Clone the Repository

    git clone https://github.com/Muhammad-Ahmad-Faizan/Image-to-Pencil-Sketch-App.git
    cd Image-to-Pencil-Sketch-App

2️⃣ Create a Virtual Environment and Activate It

    python -m venv .venv
    source .venv/bin/activate  # For macOS/Linux
# OR
    .venv\Scripts\activate  # For Windows

3️⃣ Install Dependencies

    pip install -r requirements.txt

4️⃣ Run the Application

    python app.py

Now, open your browser and go to http://127.0.0.1:5000/.
🚀 Deployment on Render

    Create a new Render web service
    Connect your GitHub repository
    Set the build command:

    pip install -r requirements.txt

Set the start command:

    gunicorn app:app

Image to Pencil Sketch App

This is a web application that converts an image into a pencil sketch using OpenCV and Python. The app provides a simple interface for users to upload an image, generate a sketch, and download the final output.

Features

Upload an image and convert it into a pencil sketch

Download the sketched image

Simple and user-friendly UI

Built with Flask, OpenCV, and HTML/CSS

Installation

1. Clone the Repository

  git clone https://github.com/Muhammad-Ahmad-Faizan/Image-to-Pencil-Sketch-App.git
  cd Image-to-Pencil-Sketch-App

2. Create a Virtual Environment (Optional but Recommended)

python -m venv .venv
source .venv/bin/activate   # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows

3. Install Dependencies

pip install -r requirements.txt

4. Run the Application Locally

python app.py

Open your browser and go to http://127.0.0.1:5000/ to access the app.

Deployment on Render

To deploy this app on Render, follow these steps:

Push your code to GitHub using the following commands:

git add .
git commit -m "Initial commit"
git push origin main

Go to Render and log in.

Click on New Web Service and connect your GitHub repository.

Choose the branch (main) and set up the build command:

pip install -r requirements.txt

Set the start command:

python app.py

Click Deploy, and Render will handle the deployment.

Technologies Used

Flask (Backend Framework)

OpenCV (Image Processing)

HTML/CSS (Frontend UI)

Bootstrap (Styling)

Folder Structure

Image-to-Pencil-Sketch-App/
│── static/           # CSS and JS files
│── templates/        # HTML files
│── app.py           # Main application script
│── requirements.txt  # Dependencies
│── README.md        # Project documentation

Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License

This project is licensed under the MIT License.

Contact

If you have any questions, feel free to reach out via GitHub Issues or email me at zmarketingcompany@gmail.com


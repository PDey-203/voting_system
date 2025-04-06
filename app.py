from flask import Flask, request, render_template, redirect, url_for, flash
import google.generativeai as gemini
import base64
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY") 

gemini.configure(api_key= os.getenv("API_KEY"))

file_path = 'Book.csv'
df = pd.read_csv(file_path)

def encode_image(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
    except FileNotFoundError:
        return None

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and file.filename.endswith('.jpg'):

        image_path = os.path.join('static', file.filename)
        file.save(image_path)
        base64_image = encode_image(image_path)

        if base64_image:
            try:
    
                model = gemini.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(
                    [
                        "Extract only the Voter ID number from this image.",
                        {"mime_type": "image/jpeg", "data": base64_image}
                    ]
                )

                response_text = response.text.strip()
                if response_text in df['ID'].values:
                    df.loc[df['ID'] == response_text, 'VOTED'] = 1
                    df.to_csv(file_path, index=False)
                    flash(f"Voter ID {response_text} marked as voted.")
                else:
                    flash(f"Voter ID {response_text} not found in the dataset.")

            except Exception as e:
                flash(f"Error during model processing: {e}")
        else:
            flash("Image encoding failed.")

        os.remove(image_path)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
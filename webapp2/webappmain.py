from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app=Flask(__name__)
''' app.config['UPLOAD_FOLDER']
app.config['MAX_CONTENT_PATH'] '''

@app.route('/')
def home():
    return render_template("home.html")

""" 
==============
UPLOAD
==============
"""

@app.route('/upload')
def upload_file():
    return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'

uploaded_list = []

for file in uploaded_list:
    uploaded_list.append(file)
        
print(uploaded_list)














""" run"""
if __name__=="__main__":
    app.run(debug=True)
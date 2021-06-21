import cv2
from flask import Flask, render_template, request, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from tessocr_module.tessocr_module import ocr, img_preprocessing
from datetime import datetime
import os
import pytesseract
import numpy as np

app = Flask(__name__)
app.app_context().push()

@app.route('/')
def home():
    return render_template('homepage.html')

# Routers -------------------------------------------------------------------------
@app.route('/ocr_reader', methods=['POST'])
def ocr_reader():
    isthisFile = request.files['file']
    # filename = request.form['text']
    filename = "input"
    # print(filename)
    dir_img = "static/" + isthisFile.filename
    isthisFile.save(dir_img)
    ocr_ = ocr(dir_img)
    output = ocr_.ocr_reader(threshold=False, remove_noise=False, sharpen=False)
    output = output.replace("\n", " ")
    # print(output)
    output_time = datetime.now().strftime("%Y%m%d %H:%M:%S")
    data = {
        'Image': filename,
        'Extract_datetime': output_time,
        'Text': output
    }
    os.remove(dir_img)
    return data

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    # app.run(port="5000", host="0.0.0.0", debug=True, use_reloader=False)
    # app.run(host="0.0.0.0", debug=True, use_reloader=False)
    app.run(host='0.0.0.0', port=os.environ.get('PORT', '5000'))

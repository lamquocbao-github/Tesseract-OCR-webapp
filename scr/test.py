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

dir_img = "static/bill.png"
# ocr_ = ocr(dir_img)
img = cv2.imread(dir_img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_proc = img_preprocessing(gray)
img1 = img_proc.sharpening()
# output = ocr_.ocr_reader(threshold=False, remove_noise=False, erosion=True)
cv2.imshow("input",img)
cv2.imshow("output",img1)
cv2.imshow("output_gray",gray)
cv2.waitKey(0)
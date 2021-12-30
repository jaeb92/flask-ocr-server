import os
import cv2
import easyocr
import numpy as np

from ocr.service.utils.reg import *
from tqdm import tqdm
# class OcrService:
#     def __init__(self):
#         print("ocr service")
#
#     def upload(self):
#         pass

def file_save(f, save_path):
    save_dirname = os.path.dirname(save_path)
    if not os.path.exists(save_dirname):
        # print(f"{save_path} not exists")
        msg = f"Cannot found {save_dirname}"
        code = 404
    else:
        f.save(save_path)
        msg = f"success to save {f.filename}  >> {os.path.dirname(save_path)}"
        code = 201

    return msg, code

def ocr_text(file_path):
    if not os.path.exists(file_path):
        msg = f"Cannot found {file_path}"
        code = 404

    else:
        print("Getting text from image now...")
        ff = np.fromfile(file_path, np.uint8)
        image = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
        reader = easyocr.Reader(['ko','en'], gpu=False)
        result = reader.readtext(image, mag_ratio=2.)
        text_arr = []
        for (bbox,text,prob) in result:
            text = text.replace(' ', '')
            text_arr.append(text)

        text = "\n".join(text_arr)
        print(f"text >> {text}")
        msg = f"{text}"
        code = 201

    return msg, code

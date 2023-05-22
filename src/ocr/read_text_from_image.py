import cv2
import easyocr
import numpy as np
from PIL.Image import Image
from pytesseract import pytesseract

from ocr.crop_image import crop_image_by_rectangle


def read_text_from_image_rectangles(table_fields, input_image, table_rectangles):
    image_of_table = crop_image_by_rectangle(input_image, table_rectangles)
    # convert image to greyscale
    image_of_table = image_of_table.convert('L')

    languages = ["en"]
    reader = easyocr.Reader(languages)

    read_data = {}
    for col_label, coordinates in table_fields.items():
        cell_image = crop_image_by_rectangle(image_of_table, coordinates)
        image_data = np.asarray(cell_image)
        result = reader.readtext(image_data, detail=0)

        if len(result) > 0:
            read_data[col_label] = result[0]
        else:
            read_data[col_label] = ""

    return read_data

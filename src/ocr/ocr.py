import cv2
import easyocr
import numpy as np
from PIL.Image import Image
from pytesseract import pytesseract

from ocr.transformation_image import crop_image_by_rectangle, enlarge_image


def read_text_from_image(reader, cell_image):
    image_data = np.asarray(cell_image)
    return reader.readtext(image_data, detail=0)


def read_text_from_image_rectangles(table_fields, input_image, table_rectangles):
    image_of_table = crop_image_by_rectangle(input_image, table_rectangles)

    # convert image to greyscale
    image_of_table = image_of_table.convert('L')

    languages = ["en", "pl"]
    reader = easyocr.Reader(languages, verbose=False)

    read_data = {}
    for col_label, coordinates in table_fields.items():
        cell_image = crop_image_by_rectangle(image_of_table, coordinates)
        result = read_text_from_image(reader, cell_image)

        for percent in range(50, 150, 50):
            if len(result) <= 0:
                enlarge_cell_image = enlarge_image(cell_image, percent)
                result = read_text_from_image(reader, enlarge_cell_image)
            else:
                break

        if len(result) > 0:
            read_data[col_label] = result[0]
        else:
            read_data[col_label] = ""

    return read_data

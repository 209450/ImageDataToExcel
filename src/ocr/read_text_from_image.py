import easyocr
import numpy as np


def read_text_from_image(languages, images):
    reader = easyocr.Reader(languages)
    table_data = []
    for image_of_excel_table in images:
        image_data = np.asarray(image_of_excel_table)
        table_data.append(reader.readtext(image_data))

    return table_data
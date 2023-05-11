import easyocr
import numpy as np

from ocr.crop_image import crop_image_by_rectangle_coordinates_with


def read_text_from_image_rectangles(input_file_path, table_rectangles):
    images_of_excel_table = crop_image_by_rectangle_coordinates_with(input_file_path, table_rectangles)

    languages = ["en", "pl"]
    reader = easyocr.Reader(languages)

    table_data = []
    for image in images_of_excel_table:
        image_data = np.asarray(image)
        table_data.append(reader.readtext(image_data))

    return table_data

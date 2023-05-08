import sys
import re
import numpy as np
from PIL import Image
from enum import Enum

from PyQt5.QtWidgets import QApplication, QMessageBox

from data_structures.rectangle_coordinates import RectangleCoordinates
from gui.form_change_rectangle_coordinates import FormChangeRectangleCoordinates
from gui.image_window_with_rectangles import ImageWindowWithRectangles


class FileType(Enum):
    RETINA = ["retina", [RectangleCoordinates(0, 0, 100, 100)]]
    DISC = ["disc", [RectangleCoordinates(100, 100, 200, 200),
                     RectangleCoordinates(300, 300, 400, 400)]]
    ANTERIOR_RADIAL = ["anterior_radial", [RectangleCoordinates(500, 500, 600, 600)]]
    ANTERIOR_3D = ["anterior_3d"]
    NOT_FOUND = ["not found"]


def find_if_word_was_found_in_text(text, word):
    lower_word = word.lower()
    lower_text = text.lower()

    word_occurrence_indexes = re.findall(lower_word, lower_text)
    if len(word_occurrence_indexes) == 0:
        return False
    else:
        return True


def check_input_file_type(input_file_path):
    file_type = FileType.NOT_FOUND
    for type in FileType:
        if type == FileType.NOT_FOUND:
            continue
        if find_if_word_was_found_in_text(input_file_path, type.value[0]):
            file_type = type
            break
    return file_type


print("Program started")
print(sys.argv)
print(sys.argv[1])

input_file_path = sys.argv[1]
file_type = check_input_file_type(input_file_path)
print(file_type)

try:
    table_rectangles = list(file_type.value[1])
except IndexError:
    print(f"{file_type} can not be processed")
    print("Program ended")
    sys.exit(1)

app_image_window = QApplication(sys.argv)
image_window = ImageWindowWithRectangles(input_file_path)
image_window.show()

placement_of_rectangles_is_not_correct = True
while placement_of_rectangles_is_not_correct:

    image_window.clear_drawings()
    for index, rectangle in enumerate(table_rectangles):
        image_window.draw_rectangle(rectangle.top_left, rectangle.bottom_right)

        label_padding_y = 5
        label_coordinates = (rectangle.top_left[0], rectangle.top_left[1] - label_padding_y)
        image_window.draw_label(label_coordinates, str(index))

    message_box_answer = QMessageBox.question(image_window, "Rectangles placement",
                                              "Do the coordinates of rectangle are "
                                              "valid?")
    if message_box_answer == QMessageBox.Yes:
        placement_of_rectangles_is_not_correct = False
    else:
        form = FormChangeRectangleCoordinates(image_window, table_rectangles)
        form.show()

        form_result = form.exec_()
        if form_result:
            table_rectangles = list(form.get_fields_values())

input_image = Image.open(input_file_path)
images_of_excel_table = []
for table_rectangle in table_rectangles:
    x1, y1 = table_rectangle.top_left
    x2, y2 = table_rectangle.bottom_right

    image_of_excel_table = input_image.crop((x1, y1, x2, y2))
    images_of_excel_table.append(image_of_excel_table)

for image_of_excel_table in images_of_excel_table:
    image_of_excel_table.show()


app_image_window.exec_()

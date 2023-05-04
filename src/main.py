import sys
import re
from PIL import Image
from enum import Enum

from PyQt5.QtWidgets import QApplication

from gui.image_window_with_rectangles import ImageWindowWithRectangles


class FileType(Enum):
    RETINA = ["retina", [0, 0], [10, 10]]
    DISC = ["disc", [[0, 0], [10, 10]], [[0, 0], [10, 10]]]
    ANTERIOR_RADIAL = ["anterior_radial", [0, 0], [10, 10]]
    ANTERIOR_3D = ["anterior_3d"]
    NOT_FOUND = ["not found"]


def find_if_word_occured_in_text(text, word):
    lower_word = word.lower()
    lower_text = text.lower()

    word_occurence_indexes = re.findall(lower_word, lower_text)
    if len(word_occurence_indexes) == 0:
        return False
    else:
        return True


print("Program started")
print(sys.argv)
print(sys.argv[1])

input_file_path = sys.argv[1]

file_type = FileType.NOT_FOUND
for type in FileType:
    if type == FileType.NOT_FOUND:
        continue
    if find_if_word_occured_in_text(input_file_path, type.value[0]):
        file_type = type
        break

print(file_type)

try:
    app_image_window = QApplication(sys.argv)
    image_window = ImageWindowWithRectangles(input_file_path)
    image_window.show()

    image_window.draw_rectangle((100, 100), (300, 200))

    app_image_window.exec_()
    # im = Image.open(input_file_path)
    # im.show()
except FileNotFoundError:
    print("file not found for path: " + input_file_path)

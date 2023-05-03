import sys
import re
from PIL import Image
from enum import Enum


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
    if(find_if_word_occured_in_text(input_file_path, type.value[0])):
        file_type = type
        break

print(file_type)
# if find_if_word_occured_in_text(input_file_path, "retina") == True:
#     print("retina found")
# elif find_if_word_occured_in_text(input_file_path, "disc") == True:
#     print("disc found")
# else:
#     print("unknown file")

try:
    im = Image.open(input_file_path)
    im.show()
except FileNotFoundError:
    print("file not found for path: " + input_file_path)

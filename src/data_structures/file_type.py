import re
from enum import Enum

from data_structures.rectangle_coordinates import RectangleCoordinates


class FileType(Enum):
    RETINA = ["retina", [RectangleCoordinates(261, 883, 335, 968)]]
    DISC_3D_DWOJE = ["disc_3d_dwoje", [RectangleCoordinates(725, 226, 921, 496),
                                       RectangleCoordinates(778, 811, 920, 873)]]
    DISC_3D_R = ["disc_3d_r", [RectangleCoordinates(801, 232, 986, 871)]]
    DISC_3D_L = ["disc_3d_l", [RectangleCoordinates(801, 232, 986, 871)]]
    ANTERIOR_RADIAL_L = ["anterior_radial_l", [RectangleCoordinates(255, 699, 308, 875)]]
    ANTERIOR_RADIAL_R = ["anterior_radial_r", [RectangleCoordinates(255, 699, 308, 875)]]
    DISC_ANGIO = ["disc_angio"]
    ANTERIOR_3D = ["anterior_3d"]
    NOT_FOUND = ["not found"]


def check_input_file_type(input_file_path):
    file_type = FileType.NOT_FOUND
    for type in FileType:
        if type == FileType.NOT_FOUND:
            continue
        if find_if_word_was_found_in_text(input_file_path, type.value[0]):
            file_type = type
            break
    return file_type


def find_if_word_was_found_in_text(text, word):
    lower_word = word.lower()
    lower_text = text.lower()

    word_occurrence_indexes = re.findall(lower_word, lower_text)
    if len(word_occurrence_indexes) == 0:
        return False
    else:
        return True
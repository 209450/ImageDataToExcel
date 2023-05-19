import re
from enum import Enum

from data_structures.rectangle_coordinates import RectangleCoordinates


class Tables:
    short_box = (46, 23)
    DISC_3D = {
        "Tarcza [mm2]": RectangleCoordinates.from_box(8, 0, short_box),
        "Zagłębienie [mm2]": RectangleCoordinates.from_box(8, 21, short_box),
        "Rąbek [mm2]": RectangleCoordinates.from_box(8, 42, short_box),
        "Cup/Disc": RectangleCoordinates.from_box(8, 63, short_box),
        "Zagłębienie [mm3]": RectangleCoordinates.from_box(8, 105, short_box),
        "Rąbek [mm3]": RectangleCoordinates.from_box(8, 124, short_box),
        "Śr. głęb. zagłębienia [mm]": RectangleCoordinates.from_box(8, 165, short_box),
        "Maks. głęb. zagłębienia [mm]": RectangleCoordinates.from_box(8, 206, short_box),
        "Pozioma średnica tarczy [mm]": RectangleCoordinates.from_box(8, 264, short_box),
        "Pionowa średnia tarczy [mm]": RectangleCoordinates.from_box(8, 304, short_box),
        "Średnica tarczy [mm]": RectangleCoordinates.from_box(8, 346, short_box),
        "Pozioma średnica zagłębienia [mm]": RectangleCoordinates.from_box(8, 368, short_box),
        "Pionowa średnica zagłębienia [mm]": RectangleCoordinates.from_box(8, 407, short_box),
        "średnica zagłębienia [mm]": RectangleCoordinates.from_box(8, 447, short_box),
        "C/D poziomo": RectangleCoordinates.from_box(8, 489, short_box),
        "C/D pionowo": RectangleCoordinates.from_box(8, 510, short_box),
        "Tarcza V/H": RectangleCoordinates.from_box(8, 530, short_box),
        "Zagłębienie V/H": RectangleCoordinates.from_box(8, 551, short_box),
        "R/D minimum": RectangleCoordinates.from_box(8, 573, short_box),
        "Brak rąbka []": RectangleCoordinates.from_box(8, 593, short_box),
        "DDLS": RectangleCoordinates.from_box(0, 613, short_box),
        "Zagłębienie [mm2] Norma min": RectangleCoordinates.from_box(76, 20, short_box),
        "Zagłębienie [mm2] Norma max": RectangleCoordinates.from_box(130, 20, short_box),
        "Rąbek [mm2] Norma min": RectangleCoordinates.from_box(75, 42, short_box),
        "Rąbek [mm2] Norma max": RectangleCoordinates.from_box(130, 42, short_box),
        "Cup/Disc Norma min": RectangleCoordinates.from_box(79, 63, short_box),
        "Cup/Disc Norma max": RectangleCoordinates.from_box(132, 62, short_box),
        "Zagłębienie [mm3] Norma min": RectangleCoordinates.from_box(80, 103, short_box),
        "Zagłębienie [mm3] Norma max": RectangleCoordinates.from_box(130, 101, short_box),
        "Rąbek [mm3] Norma min": RectangleCoordinates.from_box(74, 125, short_box),
        "Rąbek [mm3] Norma max": RectangleCoordinates.from_box(129, 125, short_box),
        "Śr. głęb. zagłębienia [mm] Norma min": RectangleCoordinates.from_box(80, 166, short_box),
        "Śr. głęb. zagłębienia [mm] Norma max": RectangleCoordinates.from_box(131, 166, short_box),
        "Maks. głęb. zagłębienia [mm] Norma min": RectangleCoordinates.from_box(77, 205, short_box),
        "Maks. głęb. zagłębienia [mm] Norma max": RectangleCoordinates.from_box(131, 205, short_box),
    }


class FileType(Enum):
    RETINA = ["retina", [RectangleCoordinates(261, 883, 335, 968)]]
    DISC_3D_DWOJE = ["disc_3d_dwoje", [RectangleCoordinates(725, 226, 921, 496),
                                       RectangleCoordinates(778, 811, 920, 873)]]
    DISC_3D_R = ["disc_3d_r", [RectangleCoordinates(803, 232, 984, 866)], Tables.DISC_3D]
    DISC_3D_L = ["disc_3d_l", [RectangleCoordinates(803, 232, 984, 866)], Tables.DISC_3D]
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

import json
import sys
import os
import easyocr
import numpy as np
from PIL import Image

from PyQt5.QtWidgets import QApplication, QMessageBox

from data_structures.file_type import check_input_file_type
from gui.change_rectangle_coordinates_dialog import FormChangeRectangleCoordinates
from gui.image_with_rectangles_window import ImageWindowWithRectangles
from gui.scanned_data_check_dialog import ScannedDataCheckDialog
from ocr.read_text_from_image import read_text_from_image_rectangles


def open_change_rectangle_window(image_path, input_table_rectangles):
    image_window = ImageWindowWithRectangles(image_path)
    image_window.show()

    placement_of_rectangles_is_not_correct = True
    while placement_of_rectangles_is_not_correct:

        image_window.clear_drawings()
        for input_table_index, rectangle in enumerate(input_table_rectangles):
            image_window.draw_rectangle(rectangle.top_left, rectangle.bottom_right)

            label_padding_y = 5
            label_coordinates = (rectangle.top_left[0], rectangle.top_left[1] - label_padding_y)
            image_window.draw_label(label_coordinates, str(input_table_index))

        message_box_answer = QMessageBox.question(image_window, "Rectangles placement",
                                                  "Do the coordinates of rectangle are "
                                                  "valid?")
        if message_box_answer == QMessageBox.Yes:
            placement_of_rectangles_is_not_correct = False
        else:
            form = FormChangeRectangleCoordinates(image_window, input_table_rectangles)
            form.show()

            form_result = form.exec_()
            if form_result:
                input_table_rectangles = list(form.get_fields_values())

    image_window.deleteLater()
    return input_table_rectangles


if __name__ == '__main__':
    print("Program started")
    print(f"current dir: {os.getcwd()}")
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

    config_path = "config.json"
    with open(config_path, encoding="utf-8") as file:
        loaded_json = json.load(file)
        output_data = loaded_json[file_type.value[0]].copy()

    input_image = Image.open(input_file_path)

    output_tables = {}
    output_data_is_not_correct = True
    app_image_window = QApplication(sys.argv)
    while output_data_is_not_correct:

        table_rectangles = open_change_rectangle_window(input_file_path, table_rectangles)
        app_image_window.closeAllWindows()

        tables_names = file_type.value[2]
        output_tables_names = dict.fromkeys(tables_names, "")
        output_tables_fields = file_type.value[2]
        for table_name, rectangle in zip(output_tables_names, table_rectangles):
            output_tables[table_name] = read_text_from_image_rectangles(output_tables_fields[table_name], input_image,
                                                                        rectangle)

        # for table_name, table_data in zip(output_data.keys(), tables_read_text):
        #     for label, text in zip(output_data[table_name].keys(), table_data):
        #         output_data[table_name][label] = text

        for table_name, output_table in output_tables.items():
            for rectangle in table_rectangles:
                dialog = ScannedDataCheckDialog(input_file_path, rectangle, output_table)
                dialog.show()

                dialog_result = dialog.exec_()
                if dialog_result:
                    # output_table = dialog.get_fields_values()
                    output_tables[table_name] = dialog.get_fields_values()
                    output_data_is_not_correct = False
                else:
                    output_data_is_not_correct = True

    # for table in output_tables:
    #     for key, value in table.items():
    #         print(f"{key}:{value}")

    for key, value in output_tables.items():
        print(f"{key}:{value}")

    # for table_name in output_data.keys():
    #     for key, value in output_data[table_name].values():
    #         print(f"{key}:{value}")

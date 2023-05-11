import sys
import os
import easyocr
import numpy as np

from PyQt5.QtWidgets import QApplication, QMessageBox

from data_structures.file_type import check_input_file_type
from gui.change_rectangle_coordinates_dialog import FormChangeRectangleCoordinates
from gui.image_with_rectangles_window import ImageWindowWithRectangles
from gui.scanned_data_check_dialog import ScannedDataCheckDialog
from ocr.crop_image import crop_image_by_rectangle_coordinates_with
from ocr.read_text_from_image import read_text_from_image_rectangles


def open_change_rectangle_window(input_table_rectangles):
    image_window = ImageWindowWithRectangles(input_file_path)
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

    output_data = {
        "Min. grubość w dołeczku [μm]": "",
        "Centralny sektor [μm]": "",
        "Średnia grubość [μm]": "",
        "Objętość [mm3]": ""
    }

    output_data_is_not_correct = True
    app_image_window = QApplication(sys.argv)
    while output_data_is_not_correct:

        table_rectangles = open_change_rectangle_window(table_rectangles)
        app_image_window.closeAllWindows()

        read_text = read_text_from_image_rectangles(input_file_path, table_rectangles)
        # read_text[0] - 1 table
        for key, text in zip(output_data.keys(), read_text[0]):
            output_data[key] = text

        for rectangle in table_rectangles:
            dialog = ScannedDataCheckDialog(input_file_path, rectangle, output_data)
            dialog.show()

            dialog_result = dialog.exec_()
            if dialog_result:
                output_data = dialog.get_fields_values()
                output_data_is_not_correct = False
            else:
                output_data_is_not_correct = True

    print(output_data)

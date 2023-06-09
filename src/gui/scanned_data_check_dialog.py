from PyQt5.QtCore import QPoint, QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QLabel, QDialog, QWidget, QVBoxLayout, QPushButton

from gui.horizontal_qline_edit_with_label import HorizontalQLineEditWithLabel


class ScannedDataCheckDialog(QDialog):
    MAX_ROWS_TABLE_DATA_CONTAINER = 10
    LEFT_MARGIN = -300

    def __init__(self, input_image_path, rectangle_coordinates, table_data):
        super().__init__()
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.image = QPixmap()
        self.label_image = QLabel()
        self.init_label_image(input_image_path, rectangle_coordinates)
        self.grid.addWidget(self.label_image, 0, 0)

        self.line_edits = {}
        self.table_data_container = QWidget()
        self.init_table_data(table_data)
        self.grid.addWidget(self.table_data_container, 0, 1)

        self.accept_button = QPushButton("accept")
        self.accept_button.clicked.connect(self.accept_data)
        self.grid.addWidget(self.accept_button, 1, 0)

        self.cancel_button = QPushButton("cancel")
        self.cancel_button.clicked.connect(self.reject_data)
        self.grid.addWidget(self.cancel_button, 1, 1)

    def accept_data(self):
        self.accept()

    def reject_data(self):
        self.reject()

    def get_fields_values(self):
        output_dict = {}
        for label_text, horizontal_line_edit in self.line_edits.items():
            output_dict[label_text] = horizontal_line_edit.line_edit.text()

        return output_dict

    def init_table_data(self, table_data):
        table_data_container_layout = QGridLayout()

        row_counter = 0
        col_counter = 0
        for key, value in table_data.items():
            new_line = HorizontalQLineEditWithLabel(str(value), key)
            table_data_container_layout.addWidget(new_line, row_counter, col_counter)

            row_counter = row_counter + 1
            if row_counter >= self.MAX_ROWS_TABLE_DATA_CONTAINER:
                row_counter = 0
                col_counter = col_counter + 1

            self.line_edits[key] = new_line

        self.table_data_container.setLayout(table_data_container_layout)

    def init_label_image(self, input_image_path, rectangle_coordinates):
        x1, y1 = rectangle_coordinates.top_left
        x2, y2 = rectangle_coordinates.bottom_right
        x1 = self.LEFT_MARGIN + x1

        top_left = QPoint(x1, y1)
        bottom_right = QPoint(x2, y2)
        crop_rectangle = QRect(top_left, bottom_right)

        self.image = QPixmap(input_image_path).copy(crop_rectangle)
        self.label_image = QLabel()
        self.label_image.setPixmap(self.image)

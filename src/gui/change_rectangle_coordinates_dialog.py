from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QLineEdit, QWidget, QHBoxLayout, QLabel

from data_structures.rectangle_coordinates import RectangleCoordinates
from gui.horizontal_qline_edit_with_label import HorizontalQLineEditWithLabel


class FormChangeRectangleCoordinates(QDialog):

    def __init__(self, parent, rectangles):
        super(FormChangeRectangleCoordinates, self).__init__(parent)
        self.return_rectangles = rectangles
        self.line_edits = {}

        widgets_to_display = []
        for rectangle_index, rectangle in enumerate(self.return_rectangles):
            x1, y1 = rectangle.top_left
            x2, y2 = rectangle.bottom_right
            coordinates = {"x1": x1, "y1": y1, "x2": x2, "y2": y2}

            for key, value in coordinates.items():
                label_text = f"Rectangle:{rectangle_index}, {key}:{value}"
                horizontal_line_edit_with_label = HorizontalQLineEditWithLabel(str(value), label_text)

                self.line_edits[(rectangle_index, key)] = horizontal_line_edit_with_label.line_edit
                widgets_to_display.append(horizontal_line_edit_with_label)

        self.button = QPushButton("Accept")
        self.button.clicked.connect(self.form_accepted)
        widgets_to_display.append(self.button)

        vertical_layout = QVBoxLayout()
        for widget in widgets_to_display:
            vertical_layout.addWidget(widget)

        self.setLayout(vertical_layout)

    def form_accepted(self):
        self.accept()

    def get_fields_values(self):
        line_edits = self.line_edits
        return_rectangles = []
        coordinates_labels = ["x1", "y1", "x2", "y2"]

        for rectangle_index, rectangle in enumerate(self.return_rectangles):
            new_values = []
            for coordinates_label in coordinates_labels:
                text_value = line_edits[(rectangle_index, coordinates_label)].text()
                new_value = int(text_value)
                new_values.append(new_value)

            x1, y1, x2, y2 = new_values
            new_rectangle = RectangleCoordinates(x1, y1, x2, y2)
            return_rectangles.append(new_rectangle)

        self.return_rectangles = list(return_rectangles)
        return self.return_rectangles



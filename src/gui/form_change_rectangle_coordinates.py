from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QLineEdit, QWidget, QHBoxLayout, QLabel


class FormChangeRectangleCoordinates(QDialog):

    def __init__(self, parent, rectangles):
        super(FormChangeRectangleCoordinates, self).__init__(parent)
        self.return_rectangles = rectangles

        widgets_to_display = []
        for rectangle_index, rectangle in enumerate(rectangles):
            x1, y1 = rectangle.top_left
            x2, y2 = rectangle.bottom_right
            coordinates = {"x1": x1, "y1": y1, "x2": x2, "y2": y2}

            for key, value in coordinates.items():
                label_text = f"Rectangle:{rectangle_index}, {key}:{value}"
                horizontal_line_edit_with_label = HorizontalQLineEditWithLabel(str(value), label_text)
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
        return self.return_rectangles


class HorizontalQLineEditWithLabel(QWidget):

    def __init__(self, line_edit_init_value, label_text):
        super(HorizontalQLineEditWithLabel, self).__init__()

        self.label = QLabel(label_text)
        self.line_edit = QLineEdit(line_edit_init_value)

        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(self.label)
        horizontal_layout.addWidget(self.line_edit)
        self.setLayout(horizontal_layout)

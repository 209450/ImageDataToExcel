from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QLineEdit


class FormChangeRectangleCoordinates(QDialog):

    def __init__(self, parent, rectangles):
        super(FormChangeRectangleCoordinates, self).__init__(parent)
        self.return_rectangles = rectangles

        self.edit_fields = []
        for index, rectangle in enumerate(rectangles):
            x1, y1 = rectangle.top_left
            x2, y2 = rectangle.bottom_right

            edit_field_x1 = QLineEdit(f"Rectangle {index}, x1:{x1}")
            edit_field_y1 = QLineEdit(f"Rectangle {index}, y1:{y1}")
            edit_field_x2 = QLineEdit(f"Rectangle {index}, x2:{x2}")
            edit_field_y2 = QLineEdit(f"Rectangle {index}, y2:{y2}")

            self.edit_fields.extend([edit_field_x1, edit_field_y1, edit_field_x2, edit_field_y2])

        self.button = QPushButton("Accept")
        self.button.clicked.connect(self.form_accepted)

        widgets = []
        widgets.extend(self.edit_fields)
        widgets.append(self.button)

        layout = QVBoxLayout()
        for widget in widgets:
            layout.addWidget(widget)

        self.setLayout(layout)

    def form_accepted(self):
        self.accept()

    def get_fields_values(self):
        return self.return_rectangles

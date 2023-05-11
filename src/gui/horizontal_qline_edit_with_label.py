from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout


class HorizontalQLineEditWithLabel(QWidget):

    def __init__(self, line_edit_init_value, label_text):
        super(HorizontalQLineEditWithLabel, self).__init__()

        self.label = QLabel(label_text)
        self.line_edit = QLineEdit(line_edit_init_value)

        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(self.label)
        horizontal_layout.addWidget(self.line_edit)
        self.setLayout(horizontal_layout)

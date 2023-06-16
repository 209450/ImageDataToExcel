from PyQt5.QtWidgets import QDialog, QGridLayout, QPushButton, QLabel


class ContinueProgramDialog(QDialog):
    def __init__(self, communicate):
        super().__init__()

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.label = QLabel(communicate)
        self.grid.addWidget(self.label, 0, 0)

        self.accept_button = QPushButton("accept")
        self.accept_button.clicked.connect(self.accept_data)
        self.grid.addWidget(self.accept_button, 1, 0)

        self.cancel_button = QPushButton("EXIT")
        self.cancel_button.clicked.connect(self.reject_data)
        self.grid.addWidget(self.cancel_button, 1, 1)

    def accept_data(self):
        self.accept()

    def reject_data(self):
        self.reject()

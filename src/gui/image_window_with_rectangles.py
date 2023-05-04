from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QMainWindow


class ImageWindowWithRectangles(QMainWindow):

    def __init__(self, image_path):
        super().__init__()

        self.image = QPixmap(image_path)
        self.label = QLabel()
        self.label.setPixmap(self.image)
        self.setCentralWidget(self.label)


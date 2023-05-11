from PyQt5.QtCore import QPoint, QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QLabel, QDialog


class ScannedDataCheckDialog(QDialog):

    def __init__(self, input_image_path, rectangle_coordinates, table_data):
        super().__init__()
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        x1, y1 = rectangle_coordinates.top_left
        x2, y2 = rectangle_coordinates.bottom_right
        top_left = QPoint(x1, y1)
        bottom_right = QPoint(x2, y2)

        self.image = QPixmap(input_image_path).copy(QRect(top_left, bottom_right))
        self.label_image = QLabel()
        self.label_image.setPixmap(self.image)

        self.grid.addWidget(self.label_image, 0, 0)

from PyQt5.QtCore import QRect, QPoint
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt5.QtWidgets import QWidget, QLabel, QMainWindow, QDesktopWidget


class ImageWindowWithRectangles(QMainWindow):

    def __init__(self, image_path):
        super().__init__()
        self.image = QPixmap(image_path)

        self.label = QLabel()
        self.painter = QPainter()
        self.pen = QPen()
        self.initialize_image_to_draw()

        self.center()

    def initialize_image_to_draw(self):
        self.label = QLabel()
        self.label.setPixmap(self.image)
        self.setCentralWidget(self.label)

        self.painter = QPainter(self.label.pixmap())
        self.pen = QPen()
        self.pen.setColor(QColor("red"))
        self.painter.setPen(self.pen)

    def draw_rectangle(self, top_left, bottom_right):
        x1, y1 = top_left
        x2, y2 = bottom_right

        rectangle = QRect(QPoint(x1, y1), QPoint(x2, y2))
        self.painter.drawRect(rectangle)

    def draw_label(self, coordinates, text):
        x, y = coordinates
        point = QPoint(x, y)

        self.painter.drawText(point, text)

    def clear_drawings(self):
        self.initialize_image_to_draw()

    def center(self):
        central_screen_point = QDesktopWidget().availableGeometry().center()
        self.move(QPoint(0, 0))

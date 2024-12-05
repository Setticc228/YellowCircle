import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtWidgets
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt
from PyQt6.uic.properties import QtCore

from UI import Ui_MainWindow


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.circles = []

    def add_circle(self, x, y, diameter):
        self.circles.append((x, y, diameter))
        self.update()

    def clear_circles(self):
        self.circles.clear()
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor('yellow'))
        for x, y, diameter in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.central_widget = Widget(self)
        self.setCentralWidget(self.central_widget)

        self.pushButton.setParent(self.central_widget)
        self.pushButton.setGeometry(150, 120, 100, 32)
        self.pushButton.clicked.connect(self.draw_circle)

    def draw_circle(self):
        self.central_widget.clear_circles()

        diameter = random.randint(10, 100)
        x = random.randint(0, self.central_widget.width() - diameter)
        y = random.randint(0, self.central_widget.height() - diameter)
        self.central_widget.add_circle(x, y, diameter)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.excepthook = except_hook
    window.show()
    sys.exit(app.exec())
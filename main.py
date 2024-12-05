import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
import random


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()
        self.flag = False

    def initUI(self):
        self.setWindowTitle('Рисование')
        self.pushButton.clicked.connect(self.pos)

    def pos(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_something(qp)
            qp.end()

    def draw_something(self, qp):
        for i in range(random.randint(1, 10)):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            x = random.randint(10, 200)
            y = random.randint(10, 200)
            h = random.randint(10, 50)
            qp.setBrush(QColor(r, g, b))
            qp.drawEllipse(x, y, h, h)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
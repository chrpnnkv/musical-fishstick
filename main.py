import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from random import randint


class YellowCircles(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.draw_flag = False
        self.color = QColor(255, 242, 66)

        self.pushButton.clicked.connect(self.start)

    def paintEvent(self, event):
        if self.draw_flag:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def start(self):
        self.draw_flag = True
        self.update()


    def draw(self, qp):
        qp.setBrush(self.color)
        for i in range(100):
            x, y, r = randint(0, 615), randint(0, 450), randint(2, 100)
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec())
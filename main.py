import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from random import randint
from ui_UI import Ui_Form


class RainbowCircles(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.draw_flag = False

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
        for i in range(100):
            qp.setBrush(QColor(*(randint(0, 255) for _ in range(3))))
            x, y, r = randint(0, 615), randint(0, 450), randint(2, 100)
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RainbowCircles()
    ex.show()
    sys.exit(app.exec())
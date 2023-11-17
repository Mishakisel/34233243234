import random
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Рисование')
        uic.loadUi('Ui.ui', self)
        self.button.clicked.connect(self.func)

    def func(self):
        self.flag = True
        self.update()


    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            # Завершаем рисование
            qp.end()

    def draw_circles(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        a = random.randint(0, 200)
        qp.drawEllipse(*[random.randint(0, 500), random.randint(0, 500)], a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QDialog

from layout import Ui_Dialog


class MyForm(QDialog):
    sumaKalorii = 0
    kcal = 1700

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Kalkulator kalorii")
        self.ui.dodaj.clicked.connect(self.add)
        self.ui.k.clicked.connect(self.gender1)
        self.ui.m.clicked.connect(self.gender2)

        self.ui.malaAkt.clicked.connect(self.activity1)
        self.ui.sredniaAkt.clicked.connect(self.activity2)
        self.ui.duzaAkt.clicked.connect(self.activity3)

        pixmap = QPixmap("1.jpg")
        pixmap = pixmap.scaled(471, 271)
        self.ui.image.setPixmap(pixmap)
    def gender1(self):
        self.ui.m.setChecked(False)
        self.setKcal()
    def gender2(self):
        self.ui.k.setChecked(False)
        self.setKcal()

    def activity1(self):
        self.ui.sredniaAkt.setChecked(False)
        self.ui.duzaAkt.setChecked(False)
        self.setKcal()
    def activity2(self):
        self.ui.malaAkt.setChecked(False)
        self.ui.duzaAkt.setChecked(False)
        self.setKcal()
    def activity3(self):
        self.ui.sredniaAkt.setChecked(False)
        self.ui.malaAkt.setChecked(False)
        self.setKcal()

    def setKcal(self):
        if(self.ui.m.isChecked()):
            if(self.ui.malaAkt.isChecked()):
                self.kcal = 1900
            if (self.ui.sredniaAkt.isChecked()):
                self.kcal = 2200
            if (self.ui.duzaAkt.isChecked()):
                self.kcal = 2500
        if (self.ui.k.isChecked()):
            if (self.ui.malaAkt.isChecked()):
                self.kcal = 1700
            if (self.ui.sredniaAkt.isChecked()):
                self.kcal = 1900
            if (self.ui.duzaAkt.isChecked()):
                self.kcal = 2100
    def add(self):
        x = self.ui.posilek.text()
        self.sumaKalorii += self.ui.kalorie.value()
        self.ui.iloscKalorii.setText(str(self.sumaKalorii))
        self.ui.lista.addItem(x + " - " + str(self.ui.kalorie.value()))

        max = self.kcal * 0.8

        if self.sumaKalorii > max:
            self.ui.labelKcal.setStyleSheet("background: black; color: white;")
            pixmap = QPixmap("2.jpg")
            pixmap = pixmap.scaled(471, 271)
            self.ui.image.setPixmap(pixmap)
        if self.sumaKalorii > self.kcal:
            self.ui.labelKcal.setStyleSheet("background: red; color: white;")
            pixmap = QPixmap("3.jpg")
            pixmap = pixmap.scaled(471, 271)
            self.ui.image.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())
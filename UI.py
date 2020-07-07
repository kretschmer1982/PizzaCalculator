import sys
import math
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QDoubleValidator
from decimal import Decimal


qtcreator_file  = "PizzaCalculator.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calculate_PB.clicked.connect(self.calculate_result)
        self.pizzaPrice1_LI.setValidator(QDoubleValidator(0.00, 20.00, 2))

    def calculate_result(self):
        input = self.pizzaPrice1_LI.text()
        if "," in input:
            priceCent = float(input) * 100
            #priceCent = float(input.replace(",", ".")) * 100
            print(priceCent)
        else:
            priceCent = float(input) * 100
        pizzaArea = float(self.pizzaSize1_CB.currentText())**2 * math.pi / 4

        relPrice = pizzaArea / priceCent
        #print(relPrice)
        self.relativePrice1.setText(str(relPrice))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
import sys
import math
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QSlider
from decimal import Decimal


qtcreator_file  = "PizzaCalculator.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calculate_PB.clicked.connect(self.calculate_result)
        validator = QDoubleValidator()
        validator.setNotation(QtGui.QDoubleValidator.StandardNotation)
        validator.setRange(0, 50.00, 2)
        self.pizzaPrice_LI_1.setValidator(validator)

        self.length_verticalSlider.valueChanged.connect(self.value_change)

    def calculate_result(self):
        price = self.pizzaPrice_LI_1.text()
        if "," in price:
            price = price.replace(",", ".")

        priceInCent = float(price) * 100
        pizzaArea = float(self.pizzaSize_CB_1.currentText())**2 * math.pi / 4

        relPrice = pizzaArea / priceInCent
        self.relativePrice_Out_1.setText(str(round(relPrice, 2))) # set rel. price in textbox

    def value_change(self, value):
        size = self.length_verticalSlider.value()
        print(value)
        self.length_label.setText(str(size))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
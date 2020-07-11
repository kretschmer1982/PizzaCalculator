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
        self.pizzaPrice_LI_2.setValidator(validator)
        self.pizzaPrice_LI_3.setValidator(validator)
        self.pizzaPrice_LI_4.setValidator(validator)

        self.length_verticalSlider.valueChanged.connect(self.set_length)
        self.width_verticalSlider.valueChanged.connect(self.set_width)

    def calculate_result(self):
        price_1 = self.pizzaPrice_LI_1.text()
        price_2 = self.pizzaPrice_LI_2.text()
        price_3 = self.pizzaPrice_LI_3.text()
        price_4 = self.pizzaPrice_LI_4.text()
        priceInCent_1 = self.price_as_float(price_1)
        priceInCent_2 = self.price_as_float(price_2)
        priceInCent_3 = self.price_as_float(price_3)
        priceInCent_4 = self.price_as_float(price_4)
        pizzaArea_1 = float(self.pizzaSize_CB_1.currentText())**2 * math.pi / 4
        pizzaArea_2 = float(self.pizzaSize_CB_2.currentText()) ** 2 * math.pi / 4
        pizzaArea_3 = float(self.pizzaSize_CB_3.currentText()) ** 2 * math.pi / 4
        pizzaArea_4 = self.length_verticalSlider.value() * self.width_verticalSlider.value()


        relPrice_1 = pizzaArea_1 / priceInCent_1
        relPrice_2 = pizzaArea_2 / priceInCent_2
        relPrice_3 = pizzaArea_3 / priceInCent_3
        relPrice_4 = pizzaArea_4 / priceInCent_4

        self.relativePrice_Out_1.setText(str(round(relPrice_1, 2))) # set rel. price in textbox
        self.relativePrice_Out_2.setText(str(round(relPrice_2, 2)))
        self.relativePrice_Out_3.setText(str(round(relPrice_3, 2)))
        self.relativePrice_Out_4.setText(str(round(relPrice_4, 2)))
        self.relChange_Label_1.setText(str(round(((relPrice_2/relPrice_1)-1)*100, 2)) + " %")
        self.relChange_Label_2.setText(str(round(((relPrice_3/relPrice_1)-1)*100, 2)) + " %")
        self.relChange_Label_3.setText(str(round(((relPrice_4/relPrice_1)-1)*100, 2)) + " %")

    def price_as_float(self, text):
        if text == "":
            return      #ToDo add Error handling for empty fields
        text = text.replace(",", ".")
        value_float = float(text) * 100
        return value_float

    def set_length(self, value):
        self.length_label.setText(str(value))

    def set_width(self, value):
        self.width_label.setText(str(value))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
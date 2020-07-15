import sys
import calculate
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QDoubleValidator

qtcreator_file  = "PizzaCalculator.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class GUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calculate_PB.clicked.connect(lambda: calculate.calculate_result(self))
        validator = QDoubleValidator()
        validator.setNotation(QtGui.QDoubleValidator.StandardNotation)
        validator.setRange(0, 50.00, 2)
        self.pizzaPrice_LI_1.setValidator(validator)
        self.pizzaPrice_LI_2.setValidator(validator)
        self.pizzaPrice_LI_3.setValidator(validator)
        self.pizzaPrice_LI_4.setValidator(validator)

        self.length_verticalSlider.valueChanged.connect(self.set_length)
        self.width_verticalSlider.valueChanged.connect(self.set_width)

    def set_length(self, value):
        self.length_label.setText(str(value))

    def set_width(self, value):
        self.width_label.setText(str(value))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = GUI()
    window.show()
    sys.exit(app.exec_())
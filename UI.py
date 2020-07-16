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
        # self.calculate_PB.clicked.connect(lambda: calculate.calculate_result(self))
        self.calculate_PB.clicked.connect(self.check_Inputs_AndCalc)
        self.clear_PB.clicked.connect(self.clear_all_LE)
        validator = QDoubleValidator()
        validator.setNotation(QtGui.QDoubleValidator.StandardNotation)
        validator.setRange(0, 50.00, 2)
        self.pizzaPrice_LE_1.setValidator(validator)
        self.pizzaPrice_LE_2.setValidator(validator)
        self.pizzaPrice_LE_3.setValidator(validator)
        self.pizzaPrice_LE_4.setValidator(validator)

        self.length_verticalSlider.valueChanged.connect(self.set_length)
        self.width_verticalSlider.valueChanged.connect(self.set_width)

        self.pizza_round_label.setHidden(True)
        self.pizza_quad_label.setHidden(True)
        self.hiddenButton_PB.clicked.connect(self.show_images)

        # if self.pizzaPrice_LE_1.text() == "":
        #     print("Textfeld 1 leer")


    def clear_all_LE(self):
        for widget in app.allWidgets():
            #print(widget)
            if isinstance(widget, QtWidgets.QLineEdit):
                print("-----------------------")
                print(widget)
                widget.clear()

    def set_length(self, value):
        self.length_label.setText(str(value))

    def set_width(self, value):
        self.width_label.setText(str(value))

    def check_Inputs_AndCalc(self):
        for widget in app.allWidgets():
            if isinstance(widget, QtWidgets.QLineEdit):
                if widget.text() == "":
                    self.missing_Input_Label.setText("Eine Eingabe fehlt")
                    return
        self.missing_Input_Label.setText("")
        calculate.calculate_result(self)

    def show_images(self):
        self.pizza_round_label.setHidden(False)
        self.pizza_quad_label.setHidden(False)

        for widget in app.allWidgets():
            if isinstance(widget, QtWidgets.QLineEdit):
                if widget.text() == "":
                    self.missing_Input_Label.setText("Eine Eingabe fehlt")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = GUI()
    window.show()
    sys.exit(app.exec_())
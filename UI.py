import sys
import calculate
from PyQt5.QtWidgets import QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QDoubleValidator
import pyqtgraph as pg

qtcreator_file  = "PizzaCalculator.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class GUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Init GUI elements
        validator = QDoubleValidator()
        validator.setNotation(QtGui.QDoubleValidator.StandardNotation)
        validator.setRange(0, 50.00, 2)
        self.pizzaPrice_LE_1.setValidator(validator)
        self.pizzaPrice_LE_2.setValidator(validator)
        self.pizzaPrice_LE_3.setValidator(validator)
        self.pizzaPrice_LE_4.setValidator(validator)
        self.pizza_round_label.setHidden(True)
        self.pizza_quad_label.setHidden(True)
        self.missing_Input_Label.setHidden(True)
        self.diagram_GV.setHidden(True)

        #signals (events)
        self.calculate_PB.clicked.connect(self.check_Inputs_AndCalc)
        self.clear_PB.clicked.connect(self.clear_all_LE)
        self.length_verticalSlider.valueChanged.connect(self.set_length)
        self.width_verticalSlider.valueChanged.connect(self.set_width)
        self.hiddenButton_PB.clicked.connect(self.show_images)
        self.diagram_PB.clicked.connect(self.show_diagram)

        self.diagram_GV.setBackground('#8c7e8c')
        styles = {'color': 'y', 'font-size': '18px'}
        self.diagram_GV.setLabel('left', 'rel. Preis [Cent/cm²]', **styles)
        self.diagram_GV.setLabel('bottom', 'Pizzafläche [cm²]', **styles)

    def clear_all_LE(self):
        for widget in app.allWidgets():
            if isinstance(widget, QtWidgets.QLineEdit):
                print(widget)
                widget.clear()

    def set_length(self, value):
        self.length_label.setText(str(value))

    def set_width(self, value):
        self.width_label.setText(str(value))

    def check_Inputs_AndCalc(self):
        for widget in app.allWidgets():
            if isinstance(widget, QtWidgets.QLineEdit): #ToDO finds too many inherited QlineEdits
                if widget.text() == "":
                    self.missing_Input_Label.setHidden(False)
                    print(widget)
                    #return
        self.missing_Input_Label.setHidden(True)
        calculate.calculate_result(self)

    def show_images(self):
        if self.hiddenButton_PB.isChecked():
            self.pizza_round_label.setHidden(False)
            self.pizza_quad_label.setHidden(False)
        else:
            self.pizza_round_label.setHidden(True)
            self.pizza_quad_label.setHidden(True)

    def show_diagram(self):
        self.diagram_GV.setHidden(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = GUI()
    window.show()
    sys.exit(app.exec_())
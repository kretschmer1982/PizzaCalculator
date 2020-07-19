import math
from PyQt5 import QtCore
import pyqtgraph as pg


def calculate_result(GUI):
    price = []
    priceInCent = []
    pizzaSize = []
    pizzaArea = []
    relativePrice = []
    price.append(GUI.pizzaPrice_LE_1.text())
    price.append(GUI.pizzaPrice_LE_2.text())
    price.append(GUI.pizzaPrice_LE_3.text())
    price.append(GUI.pizzaPrice_LE_4.text())
    price.append(GUI.pizzaPrice_LE_5.text())
    print(price)

    pizzaSize.append(float(GUI.pizzaSize_CB_1.currentText()))
    pizzaSize.append(float(GUI.pizzaSize_CB_2.currentText()))
    pizzaSize.append(float(GUI.pizzaSize_CB_3.currentText()))
    pizzaSize.append(float(GUI.pizzaSize_CB_4.currentText()))
    print(pizzaSize)

    for prc in price:
        priceInCent.append(price_as_float(prc)) # transform to cents as float

    for size in pizzaSize:
        area = round(size ** 2 * math.pi / 4, 2)
        pizzaArea.append(area)
    pizzaArea.append(GUI.length_verticalSlider.value() * GUI.width_verticalSlider.value()) #add pizza square
    print(pizzaArea)

    i = 0
    for prc in priceInCent:
        relativePrice.append(round(prc / pizzaArea[i],2))
        i = i +1
    print(relativePrice)

    GUI.relativePrice_Out_1.setText(str(relativePrice[0]))  # set rel. price in textbox
    GUI.relativePrice_Out_2.setText(str(relativePrice[1]))
    GUI.relativePrice_Out_3.setText(str(relativePrice[2]))
    GUI.relativePrice_Out_4.setText(str(relativePrice[3]))
    GUI.relativePrice_Out_5.setText(str(relativePrice[4]))

    relCngPrice_1 = round(((relativePrice[1] / relativePrice[0]) - 1) * 100, 2)
    relCngPrice_2 = round(((relativePrice[2] / relativePrice[0]) - 1) * 100, 2)
    relCngPrice_3 = round(((relativePrice[3] / relativePrice[0]) - 1) * 100, 2)
    relCngPrice_4 = round(((relativePrice[4] / relativePrice[0]) - 1) * 100, 2)

    GUI.relCngPrice_Label_1.setText(str(relCngPrice_1) + " %")
    GUI.relCngPrice_Label_2.setText(str(relCngPrice_2) + " %")
    GUI.relCngPrice_Label_3.setText(str(relCngPrice_3) + " %")
    GUI.relCngPrice_Label_4.setText(str(relCngPrice_4) + " %")

    relCngArea_1 = round(((pizzaArea[1] / pizzaArea[0]) - 1) * 100, 2)
    relCngArea_2 = round(((pizzaArea[2] / pizzaArea[0]) - 1) * 100, 2)
    relCngArea_3 = round(((pizzaArea[3] / pizzaArea[0]) - 1) * 100, 2)
    relCngArea_4 = round(((pizzaArea[4] / pizzaArea[0]) - 1) * 100, 2)

    GUI.relCngArea_Label_1.setText(str(relCngArea_1) + " %")
    GUI.relCngArea_Label_2.setText(str(relCngArea_2) + " %")
    GUI.relCngArea_Label_3.setText(str(relCngArea_3) + " %")
    GUI.relCngArea_Label_4.setText(str(relCngArea_4) + " %")

    GUI.Area_label_1.setText(str(round(pizzaArea[0], 0)))
    GUI.Area_label_2.setText(str(round(pizzaArea[1], 0)))
    GUI.Area_label_3.setText(str(round(pizzaArea[2], 0)))
    GUI.Area_label_4.setText(str(round(pizzaArea[3], 0)))
    GUI.Area_label_5.setText(str(round(pizzaArea[4], 0)))

    pen = pg.mkPen('y', width=2, style=QtCore.Qt.DashLine)
    GUI.diagram_GV.plot(pizzaArea, relativePrice, pen=pen)

def price_as_float(text):
    if text == "":
        return  # ToDo add Error handling for empty fields
    text = text.replace(",", ".")
    value_float = float(text) * 100
    return value_float

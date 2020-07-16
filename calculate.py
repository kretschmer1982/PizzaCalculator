import math

from PyQt5.QtWidgets import QLineEdit


def calculate_result(GUI):
    price = []
    price.append(GUI.pizzaPrice_LE_1.text())
    price.append(GUI.pizzaPrice_LE_2.text())
    price.append(GUI.pizzaPrice_LE_3.text())
    price.append(GUI.pizzaPrice_LE_4.text())
    price.append(GUI.pizzaPrice_LE_5.text())
    print(price)

    price_1 = GUI.pizzaPrice_LE_1.text()
    price_2 = GUI.pizzaPrice_LE_2.text()
    price_3 = GUI.pizzaPrice_LE_3.text()
    price_4 = GUI.pizzaPrice_LE_4.text()
    price_5 = GUI.pizzaPrice_LE_5.text()
    priceInCent_1 = price_as_float(price_1)
    priceInCent_2 = price_as_float(price_2)
    priceInCent_3 = price_as_float(price_3)
    priceInCent_4 = price_as_float(price_4)
    priceInCent_5 = price_as_float(price_5)
    pizzaArea_1 = float(GUI.pizzaSize_CB_1.currentText()) ** 2 * math.pi / 4
    pizzaArea_2 = float(GUI.pizzaSize_CB_2.currentText()) ** 2 * math.pi / 4
    pizzaArea_3 = float(GUI.pizzaSize_CB_3.currentText()) ** 2 * math.pi / 4
    pizzaArea_4 = float(GUI.pizzaSize_CB_4.currentText()) ** 2 * math.pi / 4
    pizzaArea_5 = GUI.length_verticalSlider.value() * GUI.width_verticalSlider.value()

    relPrice_1 = priceInCent_1 / pizzaArea_1
    relPrice_2 = priceInCent_2 / pizzaArea_2
    relPrice_3 = priceInCent_3 / pizzaArea_3
    relPrice_4 = priceInCent_4 / pizzaArea_4
    relPrice_5 = priceInCent_5 / pizzaArea_5

    GUI.relativePrice_Out_1.setText(str(round(relPrice_1, 2)))  # set rel. price in textbox
    GUI.relativePrice_Out_2.setText(str(round(relPrice_2, 2)))
    GUI.relativePrice_Out_3.setText(str(round(relPrice_3, 2)))
    GUI.relativePrice_Out_4.setText(str(round(relPrice_4, 2)))
    GUI.relativePrice_Out_5.setText(str(round(relPrice_5, 2)))

    relCngPrice_1 = round(((relPrice_2 / relPrice_1) - 1) * 100, 2)
    relCngPrice_2 = round(((relPrice_3 / relPrice_1) - 1) * 100, 2)
    relCngPrice_3 = round(((relPrice_4 / relPrice_1) - 1) * 100, 2)
    relCngPrice_4 = round(((relPrice_5 / relPrice_1) - 1) * 100, 2)

    GUI.relCngPrice_Label_1.setText(str(relCngPrice_1) + " %")
    GUI.relCngPrice_Label_2.setText(str(relCngPrice_2) + " %")
    GUI.relCngPrice_Label_3.setText(str(relCngPrice_3) + " %")
    GUI.relCngPrice_Label_4.setText(str(relCngPrice_4) + " %")

    relCngArea_1 = round(((pizzaArea_2 / pizzaArea_1) - 1) * 100, 2)
    relCngArea_2 = round(((pizzaArea_3 / pizzaArea_1) - 1) * 100, 2)
    relCngArea_3 = round(((pizzaArea_4 / pizzaArea_1) - 1) * 100, 2)
    relCngArea_4 = round(((pizzaArea_5 / pizzaArea_1) - 1) * 100, 2)

    GUI.relCngArea_Label_1.setText(str(relCngArea_1) + " %")
    GUI.relCngArea_Label_2.setText(str(relCngArea_2) + " %")
    GUI.relCngArea_Label_3.setText(str(relCngArea_3) + " %")
    GUI.relCngArea_Label_4.setText(str(relCngArea_4) + " %")

    GUI.Area_label_1.setText(str(round(pizzaArea_1, 0)))
    GUI.Area_label_2.setText(str(round(pizzaArea_2, 0)))
    GUI.Area_label_3.setText(str(round(pizzaArea_3, 0)))
    GUI.Area_label_4.setText(str(round(pizzaArea_4, 0)))
    GUI.Area_label_5.setText(str(round(pizzaArea_5, 0)))



def price_as_float(text):
    if text == "":
        return  # ToDo add Error handling for empty fields
    text = text.replace(",", ".")
    value_float = float(text) * 100
    return value_float

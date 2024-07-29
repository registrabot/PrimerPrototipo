import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from keypad_module.keypad_class import KeypadController
from buzzer_module.buzzer_class import BuzzerController
from weightsensor_module.weightsensor_conf import WeightSensor

from view_module.VProductListClass import *
from view_module.VProductClass import *
from view_module.VConfirmClass import *
from view_module.VPaymentClass import *
from view_module.VDWalletClass import *
from view_module.VTotalClass import *

import RPi.GPIO as GPIO
import threading

venta_info = []
def update_weight():
    while True:
        try:
            # Update weight
            weight_product = 0.00
            weight_product = weight_sensor.get_weight(time_sleep=1)
            if weight_product is not None:
                V_Product.weight_product = weight_product
        except (KeyboardInterrupt, SystemExit):
            print("error")
            weight_sensor.clean_and_exit()

def MainKeyController():

    actual_view = "VProduct"

    while(True):
        try:
            key = keypad_controller.get_key()
            
            if actual_view == "VProduct":
                next_view = V_Product.MatrixKeyPressEvent(key)
                if next_view == "VProductList":
                    V_ProductList.mostrar_elementos(V_Product.product_list)
                    V_ProductList.showFullScreen()
                    V_ProductList.show()
                    actual_view = "VProductList"
         
            elif actual_view == "VProductList":
                next_view = V_ProductList.MatrixKeyPressEvent(key)
                if next_view == "VProduct":
                    V_ProductList.overlay.setVisible(False)
                    V_Product.product_list = V_ProductList.product_list
                    V_Product._item.setText(f"{len(V_ProductList.product_list)}")
                    V_ProductList.hide()
                    V_Product.showFullScreen()
                    V_Product.show()
                    V_Product.seleccion = False # Por analizar cambio de variable
                    actual_view = "VProduct"

                elif next_view == "VConfirm":
                    V_ProductList.overlay.setVisible(True)
                    V_Confirm.show_in_center(V_ProductList.geometry())
                    actual_view = "VConfirm"
            
            elif actual_view == "VConfirm":
                next_view = V_Confirm.MatrixKeyPressEvent(key)
                if next_view == "VPayment":
                    V_Payment.show_in_center(V_ProductList.geometry())
                    actual_view = "VPayment"
                elif next_view == "VProductList":
                    V_ProductList.overlay.setVisible(False)
                    actual_view = "VProductList"
                elif next_view == "VProduct":
                    V_ProductList.product_list.clear()
                    V_ProductList.table_content.setRowCount(0)
                    V_ProductList.overlay.setVisible(False)
                    V_Product.product_list = V_ProductList.product_list
                    V_Product._item.setText(f"{len(V_ProductList.product_list)}")
                    V_ProductList.hide()
                    
                    V_Product.showFullScreen()
                    V_Product.show()
                    actual_view = "VProduct"
            
            elif actual_view == "VPayment":

                next_view, payment_method = V_Payment.MatrixKeyPressEvent(key)
                
                if next_view == "VDWallet":
                    V_DWallet.show_in_center(V_ProductList.geometry())
                    actual_view = "VDWallet"

                elif next_view == "VTotal":
                    V_Total.show_in_center(V_ProductList.geometry())
                    V_Total.show_total(V_ProductList.suma_total)
                    actual_view = "VTotal"

                    venta_info.clear()
                    venta_info.append(payment_method)
                    venta_info.append(V_ProductList.product_list)
                    V_Total.venta_info = venta_info

                elif next_view == "VConfirm":
                    V_Confirm.show_in_center(V_ProductList.geometry())
                    actual_view = "VConfirm"

                elif next_view == "VProduct":
                    V_ProductList.product_list.clear()
                    V_ProductList.table_content.setRowCount(0)
                    V_ProductList.overlay.setVisible(False)
                    V_Product.product_list = V_ProductList.product_list
                    V_Product._item.setText(f"{len(V_ProductList.product_list)}")
                    V_ProductList.hide()
                    
                    V_Product.showFullScreen()
                    V_Product.show()
                    actual_view = "VProduct"

            elif actual_view == "VDWallet":
                next_view, payment_method = V_DWallet.MatrixKeyPressEvent(key)
                if next_view == "VTotal":
                    V_Total.show_in_center(V_ProductList.geometry())
                    V_Total.show_total(V_ProductList.suma_total)
                    actual_view = "VTotal"

                    venta_info.clear()
                    venta_info.append(payment_method)
                    venta_info.append(V_ProductList.product_list)
                    V_Total.venta_info = venta_info

            elif actual_view == "VTotal":
                next_view = V_Total.MatrixKeyPressEvent(key)
                
                if next_view == "VPayment":
                    V_Payment.show_in_center(V_ProductList.geometry())
                    actual_view = "VPayment"
                    venta_info.clear()

                elif next_view == "VProduct":
                    V_ProductList.product_list.clear()
                    V_ProductList.table_content.setRowCount(0)
                    V_ProductList.overlay.setVisible(False)
                    V_Product.product_list = V_ProductList.product_list
                    V_Product._item.setText(f"{len(V_ProductList.product_list)}")
                    V_ProductList.hide()
                    
                    V_Product.showFullScreen()
                    V_Product.show()
                    V_Product.seleccion = False
                    actual_view = "VProduct"     
                    venta_info.clear()   
                    
            #buzzer_controller.finish_sound()

        except KeyboardInterrupt:
            print("\nSaliendo del programa...")
            GPIO.cleanup()
            break

if __name__ == '__main__':
    
    buzzer_controller = BuzzerController()
    keypad_controller = KeypadController()
    weight_sensor = WeightSensor()

    app = QApplication(sys.argv)

    V_Product = VProduct()
    V_ProductList = VProductList()
    V_Confirm=VConfirm()
    V_Payment=VPayment()
    V_DWallet=VDWallet()
    V_Total=VTotal()
    
    V_Product.show()

    keypad_thread = threading.Thread(target=MainKeyController)
    keypad_thread.daemon = True
    keypad_thread.start()

    weight_thread = threading.Thread(target=update_weight)
    weight_thread.daemon = True
    weight_thread.start()
    
    sys.exit(app.exec_())
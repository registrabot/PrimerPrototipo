## VPaymentClass.py

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class VPayment(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent, Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setFixedSize(400, 240)  # Tamaño del diálogo
        self.setModal(True)
        self.setStyleSheet("background-color: white; ")
        self.font = QFont('Tahoma', 12)


        self.roudend_borders()
        self.layout_general()
        self.layout_text_action()
        self.layout_button("1: Efectivo","2: Billetera Digital","#FF8811")
        self.layout_button("3: POS","4: Transferencia", "#FF8811")
        self.layout_button("#: Atras","D: Cancelar", "#898989")

    def roudend_borders(self): 
        radius = 15
        mask = QBitmap(self.size())
        mask.fill(Qt.white)
        painter = QPainter(mask)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(Qt.black)
        painter.drawRoundedRect(self.rect(), radius, radius)
        painter.end()
        self.setMask(mask)
   
    def layout_general(self):
        self.layout = QFrame(self)
        self.layout.setGeometry(50, 10, 300, 220)
        self.layout.setStyleSheet("background-color: white;")

        self.layout_vertical = QVBoxLayout(self.layout)
        self.layout_vertical.setAlignment(Qt.AlignVCenter)
        self.layout_vertical.setContentsMargins(0, 0, 0, 0)
        self.layout_vertical.setSpacing(5)

    def layout_text_action(self):
        self.text_action = QLabel("Elegir el método de Pago ", self.layout)
        self.text_action.setStyleSheet("color: #6C6C6C")
        self.text_action.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.text_action.setFixedHeight(30)
        self.layout_vertical.addWidget(self.text_action)

    def layout_button(self, optionA, optionB, color):

        buttons = QFrame(self.layout)
        #self.buttons.setStyleSheet("background-color: red;")
        buttons.setFixedHeight(45)

        layout_buttons = QHBoxLayout(buttons)
        layout_buttons.setContentsMargins(0, 0, 0, 0)

        # Label para "Terminar" (Layout -> Button -> Terminar)
        button_label_A = QLabel(optionA, self)
        button_label_A.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        button_label_A.setStyleSheet(f"background-color: {color}; border-radius: 5px; color: white;")
        button_label_A.setFont(self.font)

        # Label para "Cancelar" (Layout -> Button -> Cancelar)
        button_label_B = QLabel(optionB, self)
        button_label_B.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        button_label_B.setStyleSheet(f"background-color: {color}; border-radius: 5px; color: white;")
        button_label_B.setFont(self.font)
             
        # Añadir widgets a "Button" (Layout -> Header)
        layout_buttons.addWidget(button_label_A)
        layout_buttons.addWidget(button_label_B)

        # Añadir widgets al layout general
        self.layout_vertical.addWidget(buttons)

    def show_in_center(self, parent_geometry):
        self_geometry = self.geometry()
        x = parent_geometry.x() + (parent_geometry.width() - self_geometry.width()) // 2
        y = parent_geometry.y() + (parent_geometry.height() - self_geometry.height()) // 2
        self.move(x, y)
        self.show()

    def MatrixKeyPressEvent(self, key):
        if key == "1":
            self.hide() 
            return "VTotal", "efectivo"

        elif key == "3":
            self.hide() 
            return "VTotal", "pos"
        
        elif key == "4":
            self.hide() 
            return "VTotal", "transferencia"
                
        elif key == "2":
            self.hide() 
            return "VDWallet", ""
        
        elif key == "#":
            self.hide() 
            return "VConfirm", ""

        elif key == "D":
            self.hide() 
            return "VProduct", ""
        
        else:
            return "VPayment", ""
        
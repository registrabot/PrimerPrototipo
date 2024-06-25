## VTotalClass.py

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Esta clase ResizeImage se mantiene igual
class VTotal(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent, Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        #super().__init__(parent)
        self.setFixedSize(400, 240)  # Tamaño del diálogo
        self.setModal(True)
        self.setStyleSheet("background-color: white; ")

        self.font = QFont('Tahoma', 12)
        self.font2 = QFont('Tahoma', 30)
        self.font2.setBold(True)

        self.roudend_borders()
        self.layout_general()
        self.layout_text_action()
        self.layout_text_total()
        self.layout_button_finish()
        self.layout_button()
 
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
        self.layout.setGeometry(10, 10, 380, 220)
        self.layout.setStyleSheet("background-color: white;")

        self.layout_vertical = QVBoxLayout(self.layout)
        self.layout_vertical.setAlignment(Qt.AlignVCenter)
        self.layout_vertical.setContentsMargins(0, 0, 0, 0)
        self.layout_vertical.setSpacing(5)

    def layout_text_action(self):
        self.text_action = QLabel("Monto a Pagar ", self.layout)
        self.text_action.setStyleSheet("color: #6C6C6C")
        self.text_action.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.text_action.setFixedHeight(30)
        self.layout_vertical.addWidget(self.text_action)

    def layout_text_total(self):
        self.text_total = QLabel(self.layout)
        self.text_total.setStyleSheet("color: #6C6C6C")
        self.text_total.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.text_total.setFont(self.font2)
        self.text_total.setContentsMargins(0, 0, 0, 10)
        self.layout_vertical.addWidget(self.text_total)

    def layout_button_finish(self):

        self.buttons = QFrame(self.layout)
        self.buttons.setFixedHeight(45)

        self.layout_buttons = QHBoxLayout(self.buttons)
        self.layout_buttons.setContentsMargins(0, 0, 0, 0)

        # Label para "Terminar" (Layout -> Button -> Terminar)
        self.button_label_terminar = QLabel("C: Terminar", self)
        self.button_label_terminar.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.button_label_terminar.setStyleSheet("background-color: #FF8811; border-radius: 5px; color: white")
        self.button_label_terminar.setFont(self.font)
                                   
        # Añadir widgets a "Button" (Layout -> Header)
        self.layout_buttons.addWidget(self.button_label_terminar)
        # Añadir widgets al layout general
        self.layout_vertical.addWidget(self.buttons)

    def layout_button(self):

        self.buttons = QFrame(self.layout)
        self.buttons.setFixedHeight(45)

        self.layout_buttons = QHBoxLayout(self.buttons)
        self.layout_buttons.setContentsMargins(0, 0, 0, 0)

        # Label para "Terminar" (Layout -> Button -> Terminar)
        self.button_label_back = QLabel("#: Atrás", self)
        self.button_label_back.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.button_label_back.setStyleSheet("background-color: #898989; border-radius: 5px; color: white")
        self.button_label_back.setFont(self.font)


        # Label para "Cancelar" (Layout -> Button -> Cancelar)
        self.button_label_cancel = QLabel("D: Cancelar", self)
        self.button_label_cancel.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.button_label_cancel.setStyleSheet("background-color: #898989; border-radius: 5px; color: white")
        self.button_label_cancel.setFont(self.font)

                                                 
        # Añadir widgets a "Button" (Layout -> Header)
        self.layout_buttons.addWidget(self.button_label_back)
        self.layout_buttons.addWidget(self.button_label_cancel)

        # Añadir widgets al layout general
        self.layout_vertical.addWidget(self.buttons)

    def show_in_center(self, parent_geometry):
        self_geometry = self.geometry()
        x = parent_geometry.x() + (parent_geometry.width() - self_geometry.width()) // 2
        y = parent_geometry.y() + (parent_geometry.height() - self_geometry.height()) // 2
        self.move(x, y)
        self.show()

    def show_total(self, total):
        self.text_total.setText(f"S/{total}")
        


    def MatrixKeyPressEvent(self, key):
        if key == "C":
            self.hide() 
            return "VProduct"

        elif key == "#":
            self.hide() 
            return "VPayment"

        elif key == "D":
            self.hide() 
            return "VProduct"
        
        else:
            return "VTotal"
        
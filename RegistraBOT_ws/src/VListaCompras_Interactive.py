from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime

class VListaCompras(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(480, 320)
        self.setWindowTitle('Ventana Resumen')
        self.setStyleSheet("background-color: white; ")


        font = QFont('Tahoma', 13)
        font2 = QFont('Tahoma', 15)
        font2.setBold(True)

        ####################################################
        ###############    LAYOUT GENERAL   ################
        ####################################################
        
        self.layout = QFrame(self)
        self.layout.setGeometry(10, 10, 460, 300)
        self.layout.setStyleSheet("background-color: white;")

        self.layout_vertical = QVBoxLayout(self.layout)
        self.layout_vertical.setContentsMargins(0, 0, 0, 0)
        self.layout_vertical.setSpacing(5)

        ##################################################
        #####    LAYOUT HEADER (Layout -> Header)    #####
        ##################################################
                
        self.header = QFrame(self.layout)
        self.header.setStyleSheet("background-color: #FF8811; border-radius: 5px;")
        self.header.setFixedHeight(45)

        self.header_layout = QHBoxLayout(self.header)
        self.header_layout.setContentsMargins(15, 0, 15, 0)

        # Label para "Producto" (Layout -> Header -> Producto)
        self.header_label_producto = QLabel("Producto", self.header)
        self.header_label_producto.setStyleSheet("color: white;")
        self.header_label_producto.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.header_label_producto.setFont(font)

        # Label para "Subtotal" (Layout -> Header -> Subtotal)
        self.header_label_subtotal = QLabel("Subtotal (S/) ", self.header)
        self.header_label_subtotal.setStyleSheet("color: white;")
        self.header_label_subtotal.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.header_label_subtotal.setFont(font)

        
        # Añadir widgets a "Header" (Layout -> Header)
        self.header_layout.addWidget(self.header_label_producto)
        self.header_layout.addWidget(self.header_label_subtotal)

        ##################################################
        #####     LAYOUT TABLE (Layout -> Table)     #####
        ##################################################

        self.table = QFrame(self.layout)

        self.table_layout = QHBoxLayout(self.table)
        self.table_layout.setContentsMargins(10, 0, 5, 0)

        # Contenido de Table (Layout -> Table -> Table Content)
        self.table_content = QTableWidget(self.layout)
        self.table_content.setStyleSheet("""
            QTableWidget::item:selected { 
                background-color: darkgray;
                color: white; 
            }
            QTableWidget {
                color: #6C6C6C;    
                border: none;
            }
        """)

        self.table_content.setRowCount(10)  # Establecer número de filas
        self.table_content.setColumnCount(3)  # Establecer número de columnas
        self.table_content.setFont(font)

        # Llenar datos en la tabla
        self.table_content.setItem(0, 0, QTableWidgetItem("Lentejas"))
        self.table_content.setItem(0, 1, QTableWidgetItem("13.45 Kg"))
        self.table_content.setItem(0, 2, QTableWidgetItem("14.30"))
        self.table_content.item(0, 1).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # Alineación al centro
        self.table_content.item(0, 2).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)  # Alineación al centro


        self.table_content.setItem(1, 0, QTableWidgetItem("CocaCola 500mL"))
        self.table_content.setItem(1, 1, QTableWidgetItem("-"))
        self.table_content.setItem(1, 2, QTableWidgetItem("2.50"))
        self.table_content.item(1, 1).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # Alineación al centro
        self.table_content.item(1, 2).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)  # Alineación al centro

        self.table_content.setItem(2, 0, QTableWidgetItem("Leche Gloria UHT 100mL"))
        self.table_content.setItem(2, 1, QTableWidgetItem("-"))
        self.table_content.setItem(2, 2, QTableWidgetItem("7.30"))
        self.table_content.item(2, 1).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # Alineación al centro
        self.table_content.item(2, 2).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)  # Alineación al centro

        # Ocultar encabezado de fila y columna
        self.table_content.horizontalHeader().setVisible(False)
        self.table_content.verticalHeader().setVisible(False)
        self.table_content.setShowGrid(False)
        
        # Seleccionar fila 1
        #self.table_content.selectRow(0)


        # Ajustar tamaño de columnas para que se ajusten al contenido
        self.table_content.setColumnWidth(0, 270)  # Columna 0 con tamaño fijo de 100 píxeles
        self.table_content.setColumnWidth(1, 75)  # Columna 1 con tamaño fijo de 150 píxeles
        self.table_content.setColumnWidth(2, 80)  # Columna 1 con tamaño fijo de 150 píxeles'''

        # Añadir widgets a "Table" (Layout -> Table)
        self.table_layout.addWidget(self.table_content)


        ##################################################
        #####   LAYOUT BUTTONS (Layout -> Buttons)   #####
        ##################################################

        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setStyleSheet("border: 0.1px solid #6C6C6C; background-color: #B6B6B6;")

        ##################################################
        #####     LAYOUT TOTAL (Layout -> Total)     #####
        ##################################################

        # Contenedor total
        self.total = QFrame(self)
        self.total.setStyleSheet("color: #6C6C6C;")
        self.total.setFixedHeight(30)

        # Layout horizontal para los labels internos
        self.total_layout = QHBoxLayout(self.total)
        self.total_layout.setContentsMargins(20, 0, 25, 10)

        # Label para "Producto"
        self.total_label_total = QLabel("Total", self.total)
        self.total_label_total.setStyleSheet("color: black;")
        self.total_label_total.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.total_label_total.setFont(font2)

        # Label para "Subtotal"
        self.total_label_total_value = QLabel("110.10 ", self.total)
        self.total_label_total_value.setStyleSheet("color: black;")
        self.total_label_total_value.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.total_label_total_value.setFont(font2)
        
        # Añadir widgets a "Total" (Layout -> Total)
        self.total_layout.addWidget(self.total_label_total)
        self.total_layout.addWidget(self.total_label_total_value)

        ##################################################
        #####   LAYOUT BUTTONS (Layout -> Buttons)   #####
        ##################################################

        self.buttons = QFrame(self.layout)
        #self.buttons.setStyleSheet("background-color: red;")
        self.buttons.setFixedHeight(45)

        self.layout_buttons = QHBoxLayout(self.buttons)
        self.layout_buttons.setContentsMargins(0, 0, 0, 0)

        # Label para "Terminar" (Layout -> Button -> Terminar)
        self.button_label_terminar = QLabel("C: Terminar", self)
        self.button_label_terminar.setStyleSheet("color: white;")
        self.button_label_terminar.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.button_label_terminar.setStyleSheet("background-color: #FF8811; border-radius: 5px;")
        self.button_label_terminar.setFont(font)


        # Label para "Cancelar" (Layout -> Button -> Cancelar)
        self.button_label_subtotal = QLabel("D: Cancelar", self)
        self.button_label_subtotal.setStyleSheet("color: white;")
        self.button_label_subtotal.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.button_label_subtotal.setStyleSheet("background-color: #898989; border-radius: 5px;")
        self.button_label_subtotal.setFont(font)

                                                 
        # Añadir widgets a "Button" (Layout -> Header)
        self.layout_buttons.addWidget(self.button_label_terminar)
        self.layout_buttons.addWidget(self.button_label_subtotal)

        ####################################################
        #####   AGREGAR ELEMENTOS AL LAYOUT GENERAL    #####
        ####################################################

        self.layout_vertical.addWidget(self.header)
        self.layout_vertical.addWidget(self.table)
        self.layout_vertical.addWidget(self.line)
        self.layout_vertical.addWidget(self.total)
        self.layout_vertical.addWidget(self.buttons)


    def mostrar_elementos(self, elementos):
        self.lista_elementos = elementos
        self.table_content.setRowCount(len(elementos))
        self.table_content.setColumnCount(3)
        # Ajustar tamaño de columnas para que se ajusten al contenido
        self.table_content.setColumnWidth(0, 270)  # Columna 0 con tamaño fijo de 100 píxeles
        self.table_content.setColumnWidth(1, 75)  # Columna 1 con tamaño fijo de 150 píxeles
        self.table_content.setColumnWidth(2, 80)  # Columna 1 con tamaño fijo de 150 píxeles'''
        for i, elemento in enumerate(elementos):
            producto, cantidad, precio = elemento
            producto_item = QTableWidgetItem(producto)
            cantidad_item = QTableWidgetItem(str(cantidad))
            precio_item = QTableWidgetItem(str(precio))
            self.table_content.setItem(i, 0, producto_item)
            self.table_content.setItem(i, 1, cantidad_item)
            self.table_content.setItem(i, 2, precio_item)
        if len(elementos) > 0:
            self.table_content.selectRow(0)
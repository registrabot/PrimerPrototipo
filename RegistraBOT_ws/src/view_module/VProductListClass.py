## VProductListClass.py

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class VProductList(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(480, 320)
        self.setWindowTitle('Ventana Resumen')
        self.setStyleSheet("background-color: white; ")

        self.font = QFont('Tahoma', 12)
        self.font2 = QFont('Tahoma', 12)
        self.font2.setBold(True)

        self.layout_general()
        self.layout_header()
        self.layout_table()
        self.layout_total()
        self.layout_button()

                
        self.overlay = QWidget(self)
        self.overlay.setGeometry(self.rect())
        self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 128);")
        self.overlay.setVisible(False)
    


    def layout_general(self):
        self.layout = QFrame(self)
        self.layout.setGeometry(10, 10, 460, 300)
        self.layout.setStyleSheet("background-color: white;")

        self.layout_vertical = QVBoxLayout(self.layout)
        self.layout_vertical.setContentsMargins(0, 0, 0, 0)
        self.layout_vertical.setSpacing(5)

    def layout_header(self):
        self.header = QFrame(self.layout)
        self.header.setStyleSheet("background-color: #FF8811; border-radius: 5px;")
        self.header.setFixedHeight(45)

        self.header_layout = QHBoxLayout(self.header)
        self.header_layout.setContentsMargins(15, 0, 15, 0)

        # Label para "Producto" (Layout -> Header -> Producto)
        self.header_label_producto = QLabel("Producto", self.header)
        self.header_label_producto.setStyleSheet("color: white;")
        self.header_label_producto.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.header_label_producto.setFont(self.font)
        self.header_label_producto.setFixedWidth(180) 

         # Label para "Cantidad" (Layout -> Header -> Cantidad)
        self.header_label_cantidad = QLabel("Cantidad", self.header)
        self.header_label_cantidad.setStyleSheet("color: white;")
        self.header_label_cantidad.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.header_label_cantidad.setFont(self.font)

         # Label para "Precio Unitario" (Layout -> Header -> Precio Unitario)
        self.header_label_preciounitario = QLabel("PU", self.header)
        self.header_label_preciounitario.setStyleSheet("color: white;")
        self.header_label_preciounitario.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.header_label_preciounitario.setFont(self.font)


        # Label para "Subtotal" (Layout -> Header -> Subtotal)
        self.header_label_subtotal = QLabel("Subtotal (S/) ", self.header)
        self.header_label_subtotal.setStyleSheet("color: white;")
        self.header_label_subtotal.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.header_label_subtotal.setFont(self.font)

        
        # Añadir widgets a "Header" (Layout -> Header)
        self.header_layout.addWidget(self.header_label_producto)
        self.header_layout.addWidget(self.header_label_cantidad)
        self.header_layout.addWidget(self.header_label_preciounitario)
        self.header_layout.addWidget(self.header_label_subtotal)

        # Añadir widgets al layout general
        self.layout_vertical.addWidget(self.header)

    def layout_table(self):
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


        self.table_content.setFont(self.font)

        # Ocultar encabezado de fila y columna
        self.table_content.horizontalHeader().setVisible(False)
        self.table_content.verticalHeader().setVisible(False)
        self.table_content.setShowGrid(False)

        self.table_content.setSelectionBehavior(QTableWidget.SelectRows)
        self.table_content.setSelectionMode(QTableWidget.SingleSelection)
                
        self.table_content.setColumnCount(4)
        # Ajustar tamaño de columnas para que se ajusten al contenido
        self.table_content.setColumnWidth(0, 200)  # Columna 0 con tamaño fijo de 100 píxeles
        self.table_content.setColumnWidth(1, 80)  # Columna 1 con tamaño fijo de 150 píxeles
        self.table_content.setColumnWidth(2, 80)  # Columna 1 con tamaño fijo de 150 píxeles'''
        self.table_content.setColumnWidth(3, 80)  # Columna 1 con tamaño fijo de 150 píxeles'''

        # Añadir widgets a "Table" (Layout -> Table)
        self.table_layout.addWidget(self.table_content)

        # Añadir widgets al layout general
        self.layout_vertical.addWidget(self.table)

    def mostrar_elementos(self, elementos):
        print(elementos)
        self.product_list = self.agrupar_y_sumar(elementos)
        self.table_content.setRowCount(len(self.product_list))
        self.suma_total=self.sum_last_elements(self.product_list)
        self.total_label_total_value.setText(f"{self.suma_total}")
        for i, elemento in enumerate(self.product_list):
            producto, cantidad, precio , total, _ = elemento
            producto_item = QTableWidgetItem(producto)
            cantidad_item = QTableWidgetItem(str(cantidad))
            precio_item = QTableWidgetItem(str(precio))
            total_item = QTableWidgetItem(str(total))
            self.table_content.setItem(i, 0, producto_item)
            self.table_content.setItem(i, 1, cantidad_item)
            self.table_content.setItem(i, 2, precio_item)
            self.table_content.setItem(i, 3, total_item)
        print(self.product_list)
        if len(self.product_list) > 0:
            self.table_content.selectRow(0)

    def agrupar_y_sumar(self, lista):
    # Diccionario para almacenar los resultados
        resultado = {}
        # Iterar sobre la lista de entrada
        for item in lista:
            # Usar todos los elementos como clave
            clave = tuple(item)
            if clave in resultado:
                resultado[clave][1] += item[1]  # Sumar el segundo valor
                resultado[clave][3] += item[3]  # Sumar el tercer valor
            else:
                resultado[clave] = item.copy()  # Inicializar los valores
        # Convertir el diccionario a la lista deseada
        lista_resultado = list(resultado.values())
        
        return lista_resultado

    def sum_last_elements(self, list):
        total_sum = 0
        for sublist in list:
            total_sum += sublist[3]  # Añade el último elemento de cada sublista
        return total_sum
    
    def layout_total(self):
        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setStyleSheet("border: 0.1px solid #6C6C6C; background-color: #B6B6B6;")

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
        self.total_label_total.setFont(self.font2)

        # Label para "Subtotal"
        self.total_label_total_value = QLabel(self.total)
        self.total_label_total_value.setStyleSheet("color: black;")
        self.total_label_total_value.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.total_label_total_value.setFont(self.font2)
        
        # Añadir widgets a "Total" (Layout -> Total)
        self.total_layout.addWidget(self.total_label_total)
        self.total_layout.addWidget(self.total_label_total_value)

        # Añadir widgets al layout general
        self.layout_vertical.addWidget(self.line)
        self.layout_vertical.addWidget(self.total)
       
    def layout_button(self):

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
        self.button_label_terminar.setFont(self.font)


        # Label para "Cancelar" (Layout -> Button -> Cancelar)
        self.button_label_subtotal = QLabel("D: Cancelar", self)
        self.button_label_subtotal.setStyleSheet("color: white;")
        self.button_label_subtotal.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.button_label_subtotal.setStyleSheet("background-color: #898989; border-radius: 5px;")
        self.button_label_subtotal.setFont(self.font)

                                                 
        # Añadir widgets a "Button" (Layout -> Header)
        self.layout_buttons.addWidget(self.button_label_terminar)
        self.layout_buttons.addWidget(self.button_label_subtotal)

        # Añadir widgets al layout general
        self.layout_vertical.addWidget(self.buttons)

    def MatrixKeyPressEvent(self, key):
        if key == "*":
            current_row = self.table_content.currentRow()
            if current_row > 0:
                self.table_content.selectRow(current_row - 1)
        elif key == "#":
            current_row = self.table_content.currentRow()
            if current_row < self.table_content.rowCount() - 1:
                self.table_content.selectRow(current_row + 1)
        elif key == "A":
            current_row = self.table_content.currentRow()
            if current_row >= 0:
                self.table_content.removeRow(current_row)
                del self.product_list[current_row]
                self.mostrar_elementos(self.product_list)
                if current_row < len(self.product_list):
                    self.table_content.selectRow(current_row)
                elif len(self.product_list) > 0:
                    self.table_content.selectRow(len(self.product_list) - 1)
        elif key == "B":
            #self.hide()
            return "VProduct"
        elif key == "C":
            print("Lista de elementos:", self.product_list)
            
            return "VConfirm"
        elif key == "D":
            self.product_list.clear()
            self.table_content.setRowCount(0)
            #self.hide()
            return "VProduct"
        return "VProductList"
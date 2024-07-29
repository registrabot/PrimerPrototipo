## VChooseProduct.py

import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime

class ResizeImage(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.p = QPixmap()

    def setPixmap(self, p):
        self.p = p
        self.update()

    def setRoundedPixmap(self, pixmap, radius):
        size = pixmap.size()
        rounded = QPixmap(size)
        rounded.fill(Qt.transparent)

        # Use QPainter to draw the rounded pixmap
        painter = QPainter(rounded)
        painter.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        rect = QRectF(0, 0, size.width(), size.height())
        path.addRoundedRect(rect, radius, radius)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()

        self.setPixmap(rounded)

    def paintEvent(self, event):
        if not self.p.isNull():
            painter = QPainter(self)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)
            painter.drawPixmap(self.rect(), self.p)


class VElegirProducto(QDialog):

    def __init__(self, productos_info=None,  parent=None):
        super().__init__(parent, Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setFixedSize(400, 240)  # Tamaño del diálogo
        self.setModal(True)
        self.setStyleSheet("background-color: white; ")
        self.font = QFont('Tahoma', 12)

        self.roudend_borders()
        self.setup_ui()

        if productos_info is not None:
            self.create_product_block(productos_info)
        else:
            print("No se han proporcionado productos_info.")

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

    def setup_ui(self):
        self.central_wgt = QFrame(self)
        self.central_wgt.setGeometry(10, 10, 380, 220)
        self.central_wgt.setStyleSheet("background-color: white;")
        self.layoutVC = QVBoxLayout(self.central_wgt)
        self.layoutVC.setAlignment(Qt.AlignVCenter)
        self.layoutVC.setSpacing(14)
        self.layoutVC.setContentsMargins(0, 0, 0, 0)

        self.H1 = QFont("Tahoma", 21)
        self.H2 = QFont("Tahoma", 12, QFont.Bold)
        self.H3 = QFont("Tahoma", 10)
        self.H4 = QFont("Tahoma", 9)
        self.H5 = QFont("Tahoma", 19, QFont.Bold)
        self.H6 = QFont("Tahoma", 14)
        self.H7 = QFont("Tahoma", 16, QFont.Bold)

    def create_product_block(self, productos_info):

        self.clearLayout(self.layoutVC)

        self._productsBlock_wgt = QLabel(self.central_wgt)
        self._productsBlock_wgt.setFixedHeight(226)
        self._productsBlockHC = QHBoxLayout(self._productsBlock_wgt)
        self._productsBlockHC.setSpacing(10)
        self._productsBlockHC.setContentsMargins(0, 0, 0, 0)

        self.product_info = []
        select_option = 1

        for index, row in productos_info.iterrows():
            image_path = row['path_image']  # Ruta de la imagen desde los datos
            label_num = f"{select_option}:"     # Número de etiqueta, por ejemplo '1:', '2:', etc.
            label_text = row['nombre_producto']  # Nombre del producto desde los datos
            select_option +=1
        
            self.product_info.append({
                'image_path': image_path,
                'label_num': label_num,
                'label_text': label_text
            })

        print(self.product_info)
        for info in self.product_info:
            self.create_product(self._productsBlockHC, info['image_path'], info['label_num'], info['label_text'])

        self.layoutVC.addWidget(self._productsBlock_wgt)

    def create_product(self, parent_layout, image_path, label_num, label_text):
        product_block_wgt = QLabel(self._productsBlock_wgt)
        product_block_VC = QVBoxLayout(product_block_wgt)
        product_block_VC.setSpacing(22)
        product_block_VC.setContentsMargins(0, 0, 0, 0)

        product_image_wgt = ResizeImage(product_block_wgt)
        product_image_wgt.setFixedHeight(159)
        if os.path.exists(image_path):
            product_image_wgt.setRoundedPixmap(QPixmap(image_path), 70)
        else:
            print(f"Image not found: {image_path}")

        product_label_wgt = QLabel(product_block_wgt)
        product_label_wgt.setStyleSheet("background-color: #F3F3F3; border-radius: 10px; color: #6C6C6C;")
        product_label_HC = QHBoxLayout(product_label_wgt)
        product_label_HC.setContentsMargins(0, 0, 0, 0)
        product_label_HC.setSpacing(0)

        product_label_num_wgt = QLabel(label_num, product_label_wgt)
        #product_label_num_wgt.setFixedWidth(40)
        product_label_num_wgt.setAlignment( Qt.AlignVCenter)
        product_label_num_wgt.setStyleSheet("background-color: #F3F3F3; color: #FF8811;")
        product_label_num_wgt.setFont(self.H3)
        
        product_label_text_wgt = QLabel(label_text, product_label_wgt)
        product_label_text_wgt.setAlignment(Qt.AlignVCenter)
        product_label_text_wgt.setStyleSheet("background-color: #F3F3F3; color: #6C6C6C;")
        product_label_text_wgt.setFont(self.H3)

        product_label_HC.addWidget(product_label_num_wgt)
        product_label_HC.addWidget(product_label_text_wgt)

        product_block_VC.addWidget(product_image_wgt)
        product_block_VC.addWidget(product_label_wgt)

        parent_layout.addWidget(product_block_wgt)

    def clearLayout(self, layout):
        n=0
        if layout is not None:
            while layout.count()>n:
                item = layout.takeAt(n)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())


    def show_in_center(self, parent_geometry):
        self_geometry = self.geometry()
        x = parent_geometry.x() + (parent_geometry.width() - self_geometry.width()) // 2
        y = parent_geometry.y() + (parent_geometry.height() - self_geometry.height()) // 2
        self.move(x, y)
        self.show()
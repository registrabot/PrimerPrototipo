## VDWalletClass.py

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Esta clase ResizeImage se mantiene igual
class ResizeImage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.p = QPixmap()

    def setPixmap(self, p):
        self.p = p
        self.update()

    def setRoundedPixmap(self, pixmap, radius):
        size = pixmap.size()
        rounded = QPixmap(size)
        rounded.fill(Qt.transparent)

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


class VDWallet(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent, Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setFixedSize(400, 240)
        self.setModal(True)
        self.setStyleSheet("background-color: white; ")

        # Remove close, minimize, and maximize buttons
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.FramelessWindowHint)

        # Create a rounded rectangle mask using QPixmap and QBitmap
        radius = 15
        mask = QBitmap(self.size())
        mask.fill(Qt.white)
        painter = QPainter(mask)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(Qt.black)
        painter.drawRoundedRect(self.rect(), radius, radius)
        painter.end()
        self.setMask(mask)

        # Font - Style
        self.H7 = QFont("Tahoma", 12)

        self.layoutVC = QVBoxLayout(self)
        self.layoutVC.setContentsMargins(54, 15, 54, 15)  # Adjust margins

        self._chooseWallet_label = QLabel('Elegir Billetera Digital', self)
        self._chooseWallet_label.setFont(self.H7)
        self._chooseWallet_label.setStyleSheet("background-color: white; color: #6C6C6C;")
        self._chooseWallet_label.setAlignment(Qt.AlignCenter)
        self._chooseWallet_label.setFixedHeight(40)

        # Block Wallet Images
        self._walletImageBlock_wgt = QLabel(self)
        self._walletImageBlock_wgt.setStyleSheet("background-color: white; color: black;")
        self._walletImageBlockHC = QHBoxLayout(self._walletImageBlock_wgt)

        self._walletImage1 = ResizeImage(self._walletImageBlock_wgt)
        self._walletImage1.setRoundedPixmap(QPixmap('view_module/images/yape-icono.png'), 20)
        self._walletImage1.setFixedSize(83, 83)
        self._walletImage1.setStyleSheet("background-color: #F3F3F3; border-radius: 20px;")

        self._walletImage2 = ResizeImage(self._walletImageBlock_wgt)
        self._walletImage2.setRoundedPixmap(QPixmap('view_module/images/plin-logo.png'), 20)
        self._walletImage2.setFixedSize(83, 83)
        self._walletImage2.setStyleSheet("background-color: #F3F3F3; border-radius: 20px;")

        self._walletImageBlockHC.addWidget(self._walletImage1)
        self._walletImageBlockHC.addWidget(self._walletImage2)

        self._walletImageBlock_wgt.setLayout(self._walletImageBlockHC)

        # Block Wallet Labels
        self._walletLabelBlock_wgt = QLabel(self)
        self._walletLabelBlock_wgt.setStyleSheet("background-color: white; border-radius: 30px; color: black;")
        self._walletLabelBlock_wgt.setFixedHeight(45)
        self._walletLabelBlockHC = QHBoxLayout(self._walletLabelBlock_wgt)
        self._walletLabelBlockHC.setSpacing(20)
        self._walletLabelBlockHC.setContentsMargins(0, 0, 0, 0)

        self._walletLabel1 = QLabel('1: Yape', self._walletLabelBlock_wgt)
        self._walletLabel1.setFont(self.H7)
        self._walletLabel1.setStyleSheet("background-color: #FF8811; color: white; border-radius: 10px;")
        self._walletLabel1.setAlignment(Qt.AlignCenter)

        self._walletLabel2 = QLabel('2: Plin', self._walletLabelBlock_wgt)
        self._walletLabel2.setFont(self.H7)
        self._walletLabel2.setStyleSheet("background-color: #FF8811; color: white; border-radius: 10px;")
        self._walletLabel2.setAlignment(Qt.AlignCenter)

        self._walletLabelBlockHC.addWidget(self._walletLabel1)
        self._walletLabelBlockHC.addWidget(self._walletLabel2)

        self.layoutVC.addWidget(self._chooseWallet_label)
        self.layoutVC.addWidget(self._walletImageBlock_wgt)
        self.layoutVC.addWidget(self._walletLabelBlock_wgt)

        self.setLayout(self.layoutVC)

    def show_in_center(self, parent_geometry):
        self_geometry = self.geometry()
        x = parent_geometry.x() + (parent_geometry.width() - self_geometry.width()) // 2
        y = parent_geometry.y() + (parent_geometry.height() - self_geometry.height()) // 2
        self.move(x, y)
        self.show()
    
    def MatrixKeyPressEvent(self, key):
        if key == "1":
            self.hide() 
            return "VTotal", "yape"
                
        elif key == "2":
            self.hide() 
            return "VTotal", "plin"
        

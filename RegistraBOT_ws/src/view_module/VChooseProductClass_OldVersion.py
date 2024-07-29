## VChooseProduct.py

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


class VElegirProducto(QMainWindow):
    def __init__(self):
        super().__init__()

        ## ======================================================
        ##              SELECT PRODUCT WINDOW
        ## =====================================================
        # HC  : Horizontal Container
        # VC  : Vertical Container
        # wgt : Widget

        self.setWindowTitle("Ventana Elegir Producto")
        self.setFixedSize(480, 320)
        self.setStyleSheet("background-color: white;")

        # Central widget
        self.central_wgt = QLabel(self)
        self.central_wgt.setGeometry(10,10,460,300)
        self.layoutVC = QVBoxLayout(self.central_wgt)
        self.layoutVC.setSpacing(14)
        self.layoutVC.setContentsMargins(0, 0, 0, 0)

        # Font - Style
        self.H1 = QFont("Tahoma", 21)
        self.H2 = QFont("Tahoma", 12, QFont.Bold)
        self.H3 = QFont("Tahoma", 11)
        self.H4 = QFont("Tahoma", 9)
        self.H5 = QFont("Tahoma", 19, QFont.Bold)
        self.H6 = QFont("Tahoma", 14)
        self.H7 = QFont("Tahoma", 16, QFont.Bold)

        ## =================================================
        ##              NAVBAR BLOCK
        ## =================================================
        # HC  : Horizontal Container
        # VC  : Vertical Container
        # wgt : Widget

        # Navigation Bar
        self._navBar_wgt = QLabel(self.central_wgt)
        self._navBar_wgt.setFixedHeight(45)
        self._navBar_wgt.setStyleSheet("background-color: #FF8811; border-radius: 10px;")
        self._navBarHC = QHBoxLayout(self._navBar_wgt)
        self._navBarHC.setContentsMargins(15, 0, 15, 0)

        # Date Label
        self._date = datetime.now()
        self._formatted_date = self._date.strftime("%d/%m/%Y")
        self._dateLabel = QLabel(self._formatted_date, self._navBar_wgt)
        self._dateLabel.setFont(self.H6)
        self._dateLabel.setStyleSheet("background-color: #FF8811; color: white;")
        self._dateLabel.setFixedSize(120, 45)

        # Time Label
        self._time = QLabel('', self._navBar_wgt)
        self._time.setFont(self.H6)
        self._time.setStyleSheet("background-color: #FF8811; color: white;")
        self._time.setFixedSize(120, 45)
        self.update_clock()

        # Box: Car - List - Item
        self._carListItem_wgt = QLabel(self._navBar_wgt)
        self._carListItemHC = QHBoxLayout(self._carListItem_wgt)
        self._carListItemHC.setContentsMargins(0, 0, 0, 0)

        # CarShop Image
        
        self._carShopImage = QPixmap('view_module/images/Cart.png')
        self._carShop = QLabel(self._carListItem_wgt)
        self._carShop.setPixmap(self._carShopImage)
        self._carShop.setStyleSheet("background-color: #FF8811;")

        # List Label
        self._buyList = QLabel('Lista de Compra:', self._carListItem_wgt)
        self._buyList.setFont(self.H6)
        self._buyList.setStyleSheet("background-color: #FF8811; color: white;")

        # Item Label
        self._item = QLabel(self._carListItem_wgt)
        self._item.setFixedSize(30, 30)
        self._item.setStyleSheet("background-color: white; border-radius: 15px;")

        # Add Widget in Car - List - Item Box
        self._carListItemHC.addWidget(self._carShop)
        self._carListItemHC.addWidget(self._buyList)
        self._carListItemHC.addWidget(self._item)

        # Add Widget in NavBar Box
        self._navBarHC.addWidget(self._dateLabel)
        self._navBarHC.addWidget(self._time)
        self._navBarHC.addWidget(self._carListItem_wgt)

        # Add Widget in VerticalLayout
        self.layoutVC.addWidget(self._navBar_wgt)
    
    ## =================================================
    ##             CHOOSE PRODUCT BLOCK
    ## =================================================
    # HC  : Horizontal Container
    # VC  : Vertical Container
    # wgt : Widget

        # Products Blocks
        self._productsBlock_wgt = QLabel(self.central_wgt)
        self._productsBlock_wgt.setFixedHeight(226)
        self._productsBlockHC = QHBoxLayout(self._productsBlock_wgt)
        self._productsBlockHC.setSpacing(20)
        self._productsBlockHC.setContentsMargins(0, 0, 0, 0)

        # Product 1
        self._productBlock1_wgt = QLabel(self._productsBlock_wgt)
        self._productBlock1VC = QVBoxLayout(self._productBlock1_wgt)
        self._productBlock1VC.setSpacing(22)
        self._productBlock1VC.setContentsMargins(0, 0, 0, 0)

        self._product1Image_wgt = ResizeImage(self._productBlock1_wgt)
        self._product1Image_wgt.setFixedHeight(159)
        self._product1Image_wgt.setRoundedPixmap(QPixmap('view_module/images/lenteja.png'), 70)

        self._product1Label_wgt = QLabel(self._productBlock1_wgt)
        self._product1Label_wgt.setStyleSheet("background-color: #F3F3F3; border-radius: 10px; color: #6C6C6C;")
        self._product1LabelHC = QHBoxLayout(self._product1Label_wgt)
        self._product1LabelHC.setContentsMargins(0, 0, 0, 0)
        self._product1LabelHC.setSpacing(0)

        self._product1LabelNum_wgt = QLabel('1:',self._product1Label_wgt)
        self._product1LabelNum_wgt.setFixedWidth(40)
        self._product1LabelNum_wgt.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self._product1LabelNum_wgt.setStyleSheet("background-color: #F3F3F3; color: #FF8811;")
        self._product1LabelText_wgt = QLabel('Lentejas',self._product1Label_wgt)
        self._product1LabelText_wgt.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self._product1LabelText_wgt.setStyleSheet("background-color: #F3F3F3; color: #6C6C6C; padding: 5px;")

        self._product1LabelHC.addWidget(self._product1LabelNum_wgt)
        self._product1LabelHC.addWidget(self._product1LabelText_wgt)

        # Adding widgets in Product Block  1
        self._productBlock1VC.addWidget(self._product1Image_wgt)
        self._productBlock1VC.addWidget(self._product1Label_wgt)

        # Product 2
        self._productBlock2_wgt = QLabel(self._productsBlock_wgt)
        self._productBlock2VC = QVBoxLayout(self._productBlock2_wgt)
        self._productBlock2VC.setSpacing(22)
        self._productBlock2VC.setContentsMargins(0, 0, 0, 0)

        self._product2Image_wgt = ResizeImage(self._productBlock2_wgt)
        self._product2Image_wgt.setFixedHeight(159)
        self._product2Image_wgt.setFixedHeight(159)
        self._product2Image_wgt.setRoundedPixmap(QPixmap('view_module/images/frejoles.png'), 70)

        self._product2Label_wgt = QLabel(self._productBlock2_wgt)
        self._product2Label_wgt.setStyleSheet("background-color: #F3F3F3; border-radius: 10px; color: #6C6C6C;")
        self._product2LabelHC = QHBoxLayout(self._product2Label_wgt)
        self._product2LabelHC.setContentsMargins(0, 0, 0, 0)
        self._product2LabelHC.setSpacing(0)

        self._product2LabelNum_wgt = QLabel('2:',self._product2Label_wgt)
        self._product2LabelNum_wgt.setFixedWidth(40)
        self._product2LabelNum_wgt.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self._product2LabelNum_wgt.setStyleSheet("background-color: #F3F3F3; color: #FF8811;")
        self._product2LabelText_wgt = QLabel('Frejol',self._product2Label_wgt)
        self._product2LabelText_wgt.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self._product2LabelText_wgt.setStyleSheet("background-color: #F3F3F3; color: #6C6C6C; padding: 5px;")

        self._product2LabelHC.addWidget(self._product2LabelNum_wgt)
        self._product2LabelHC.addWidget(self._product2LabelText_wgt)

        # Adding widgets in Product Block 2
        self._productBlock2VC.addWidget(self._product2Image_wgt)
        self._productBlock2VC.addWidget(self._product2Label_wgt)

        # Product 3
        self._productBlock3_wgt = QLabel(self._productsBlock_wgt)
        self._productBlock3VC = QVBoxLayout(self._productBlock3_wgt)
        self._productBlock3VC.setSpacing(22)
        self._productBlock3VC.setContentsMargins(0, 0, 0, 0)

        self._product3Image_wgt = ResizeImage(self._productBlock3_wgt)
        self._product3Image_wgt.setFixedHeight(159)
        self._product3Image_wgt.setFixedHeight(159)
        self._product3Image_wgt.setRoundedPixmap(QPixmap('view_module/images/arverja.png'), 70)

        self._product3Label_wgt = QLabel(self._productBlock3_wgt)
        self._product3Label_wgt.setStyleSheet("background-color: #F3F3F3; border-radius: 10px; color: #6C6C6C;")
        self._product3LabelHC = QHBoxLayout(self._product3Label_wgt)
        self._product3LabelHC.setContentsMargins(0, 0, 0, 0)
        self._product3LabelHC.setSpacing(0)

        self._product3LabelNum_wgt = QLabel('3:',self._product3Label_wgt)
        self._product3LabelNum_wgt.setFixedWidth(40)
        self._product3LabelNum_wgt.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self._product3LabelNum_wgt.setStyleSheet("background-color: #F3F3F3; color: #FF8811;")
        self._product3LabelText_wgt = QLabel('Arveja',self._product3Label_wgt)
        self._product3LabelText_wgt.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self._product3LabelText_wgt.setStyleSheet("background-color: #F3F3F3; color: #6C6C6C; padding: 5px;")

        self._product3LabelHC.addWidget(self._product3LabelNum_wgt)
        self._product3LabelHC.addWidget(self._product3LabelText_wgt)

        # Adding widgets in Product Block 3
        self._productBlock3VC.addWidget(self._product3Image_wgt)
        self._productBlock3VC.addWidget(self._product3Label_wgt)


        # Adding widgets in Product Block
        self._productsBlockHC.addWidget(self._productBlock1_wgt)
        self._productsBlockHC.addWidget(self._productBlock2_wgt)
        self._productsBlockHC.addWidget(self._productBlock3_wgt)

        # Add Widget in VerticalLayout
        self.layoutVC.addWidget(self._productsBlock_wgt)


    def update_clock(self):
        now = datetime.now().strftime("%H:%M:%S")
        self._time.setText(now)
        QTimer.singleShot(1000, self.update_clock)
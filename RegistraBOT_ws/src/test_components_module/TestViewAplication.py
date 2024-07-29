import sys
from PyQt5.QtWidgets import QApplication
from view_module.VProducto import VProducto
from view_module.VElegirProducto import VElegirProducto
from view_module.VListaCompras import VListaCompras

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VListaCompras()
    window.show()
    sys.exit(app.exec_())

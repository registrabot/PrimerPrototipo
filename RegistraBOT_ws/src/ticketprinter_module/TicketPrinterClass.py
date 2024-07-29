import os
import sys
import time
from tabulate import tabulate
print('Original sys.path:', sys.path)
sys.path.append('/home/pato/rb_workspace/PrimerPrototipo/RegistraBOT_ws/src/ticketprinter_module/Python-Thermal-Printer')
print('Updated sys.path:', sys.path)
from Adafruit_Thermal import *

class TicketPrinter:
    def __init__(self):
        self.printer = Adafruit_Thermal("/dev/ttyS0", 9600, timeout=5)
        self.lista_productos = []
        self.precio_suma_total = 0.0
    
    def agregar_producto(self, nombre, cantidad, precio):
        # Limitar el nombre del producto a 20 caracteres
        nombre_truncado = nombre[:9]
        self.lista_productos.append([nombre_truncado, cantidad, precio])
        self.precio_suma_total += cantidad * precio

    def imprimir_ticket(self):
        lista_imprimir = []
        
        ticket_text = ""
        ticket_text += "LA TIENDA DE ROSITA\n"
        ticket_text += "dir.: Jr. Medrano Silva 165, Barranco\n"
        ticket_text += "telef.: +999 999 999\n"
        ticket_text += "RUC: 205938290028\n"
        ticket_text += "FECHA Y HORA: " + time.strftime("%x") + " " + time.strftime("%X") + "\n"
        ticket_text += "PRODUCTOS:\n"
        
        for producto in self.lista_productos:
            datos_imprimir = [producto[0], producto[1], producto[2]]
            lista_imprimir.append(datos_imprimir)
        
        table = tabulate(lista_imprimir, headers=['Producto', 'QTY', 'Precio'], tablefmt="simple")
        ticket_text += table + "\n"
        
        ticket_text += "TOTAL A PAGAR: " + str(self.precio_suma_total) + "\n"
        ticket_text += "GRACIAS POR TU COMPRA\n"
        
        # Imprimir en terminal
        #print(ticket_text)
        
        # Imprimir en impresora física (comentado para pruebas)
        self.printer.println(ticket_text)
        self.printer.feed(3)  # Avanza 3 líneas para asegurarse de que el ticket se corte correctamente

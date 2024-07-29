from ticketprinter_module.TicketPrinterClass import TicketPrinter

# Crear una instancia de TicketPrinter
#printer = TicketPrinter("/dev/ttyUSB0", 9600, timeout=5)
printer = TicketPrinter()
# Agregar productos de ejemplo
printer.agregar_producto("001", "Manzana", "fruta", 2, "kg", 3.50)
printer.agregar_producto("002", "Pan", "alimento", 1, "unidad", 0.50)
printer.agregar_producto("002", "HOLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", "alimento", 1, "unidad", 0.50)

# Imprimir el ticket en el terminal
printer.imprimir_ticket()

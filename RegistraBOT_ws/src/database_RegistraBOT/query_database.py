import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('BD_RegistraBOT.db')
cursor = conn.cursor()

# SKUS
sku = ['GR-VR-BS-GRA-000-001','GR-VR-BS-GRA-000-002','GR-VR-BS-GRA-000-003']
# Consultar datos
#cursor.execute('SELECT * FROM tb_catalogo_productos WHERE sku = ''GR-VR-BS-GRA-000-005''')
#cursor.execute('SELECT * FROM tb_catalogo_productos WHERE sku = ?', ('GR-VR-BS-GRA-000-005',))
#query = 'SELECT * FROM tb_catalogo_productos WHERE sku IN ({})'.format(','.join('?' * len(sku)))

query = 'SELECT * FROM tb_registro_ventas'
#cursor.execute(query, sku)
cursor.execute(query)
# Obtener todos los resultados
tb_catalogo_productos = cursor.fetchall()

for productos in tb_catalogo_productos:
    print(productos)

# Cerrar la conexión
conn.close()
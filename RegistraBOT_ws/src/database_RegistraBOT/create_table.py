import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('BD_RegistraBOT.db')
cursor = conn.cursor()


## =================================================
##       CREATE TABLE tb_catalogo_productos
## =================================================
# Crear la tabla con la nueva columna insert_date
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tb_catalogo_productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sku TEXT NOT NULL,
        categoria_producto TEXT NOT NULL,
        subcategoria_producto TEXT NOT NULL,
        tipo_envase TEXT NOT NULL,
        marca TEXT NOT NULL,
        tamaño REAL,
        nombre_producto TEXT NOT NULL,
        unidad_medida TEXT,
        empresa_fabricante TEXT,
        path_image TEXT NOT NULL,
        insert_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

## =================================================
##       CREATE TABLE tb_registro_ventas
## =================================================
# Crear la tabla con la nueva columna insert_date
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tb_registro_ventas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_venta INTEGER  NOT NULL,
        id_bodega TEXT NOT NULL,
        sku TEXT NOT NULL,
        peso NUMERIC NOT NULL,
        cantidad INTEGER NOT NULL,
        precio_unitario NUMERIC NOT NULL,       
        precio_total NUMERIC NOT NULL,
        medio_pago TEXT NOT NULL,
        estado_venta TEXT NOT NULL,
        insert_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

conn.commit()
conn.close()

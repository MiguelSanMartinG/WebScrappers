from origins import UnderArmourScanner
import psycopg2

conexion = psycopg2.connect(
    host="localhost",
    port="5432",# Dirección del servidor
    database="scrapp",     # Nombre de la base de datos
    user="postgres",      # Usuario de PostgreSQL
    password="mysecretpassword"  # Contraseña del usuario
)

# Checa si un producto existe en la base de datos y devuelve su id si es asi si no devuelve None
def consultar_producto_pornombre(producto):
    cursor = conexion.cursor()
    try:
        consulta = "select id_producto from productos where nombre = %s;"
        cursor.execute(consulta, [producto.get_titulo()])
        id = cursor.fetchone()
        return id
    except Exception as e:
        print("Error en la consulta: ", e)
        conexion.rollback()
    finally:
        cursor.close()

# Guarda un producto, si no existe lo guarda y devuelve la ID.
def guardar_producto(producto):
    cursor = conexion.cursor()
    try:
        id = consultar_producto_pornombre(producto)
        # print(resultado)
        if id:
            print("Producto no guardado porque ya existente." + producto.get_titulo())
            return id[0]
        else:
            # Insertar el producto si no existe
            insertar_producto = """
             INSERT INTO productos (nombre, tipo)
             VALUES (%s, %s) RETURNING id_producto;
             """
            cursor.execute(insertar_producto, (producto.get_titulo(), producto.get_tipo()))
            id = cursor.fetchone()
            conexion.commit()
            print("Producto guardado correctamente.")
            # id = consultar_producto_pornombre(producto)
            return id[0]

    except Exception as e:
        print("Error en la consulta: ", e)
        conexion.rollback()
    finally:
        cursor.close()


def generar_consulta(lista):
    cursor = conexion.cursor()
    try:
        fecha = lista[0].date()
        resultados = str(lista[1])
        consulta = """
        INSERT INTO consultas(fecha_consulta,resultados) 
        VALUES (%s, %s) RETURNING id_consulta;
        """
        cursor.execute(consulta, (fecha,resultados))
        id = cursor.fetchone()
        conexion.commit()
        return id[0]
    except Exception as e:
        print("Error en la consulta: ", e)
        conexion.rollback()
    finally:
        cursor.close()

def hacer_historico_producto(id_consulta,id_producto):
    cursor = conexion.cursor()
    try:
        consulta = """
        INSERT INTO historicos_productos (id_producto, id_consulta) 
        VALUES (%s, %s) RETURNING id_historico; 
        """
        cursor.execute(consulta, (id_producto, id_consulta))
        id_historico = cursor.fetchone()
        conexion.commit()
        print("Historico guardado correctamente. " +str(id_historico[0]))
        return id_historico[0]
    except Exception as e:
        print("Error en la consulta: ", e)
        conexion.rollback()
    finally:
        cursor.close()


lista = UnderArmourScanner.getProducts('hombre', '/tenis/beisbol/')

id_consulta = generar_consulta(lista)

print(id_consulta)
# Eliminamos los 2 lugares de la lista
lista = lista[2:]

for item in lista:
    # print(item)
    id_producto = guardar_producto(item)
    id_historico = hacer_historico_producto(id_consulta,id_producto)
    print(id_historico)

conexion.close()

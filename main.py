from datetime import date
from operator import truediv

from entities import Producto
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
def get_idConsulta_with_Sku(producto):
    cursor = conexion.cursor()
    try:
        # Revisar si hoy ya se registro
        id_producto = """
        select id_producto from productos 
        where sku=%s
        """
        cursor.execute(id_producto, (producto.sku,))
        id = cursor.fetchone()
        return id[0]


    except Exception as e:
        print("Error en la consulta: 32 ", e)
        conexion.rollback()
    finally:
        cursor.close()

# Guarda un producto, si no existe lo guarda y devuelve la ID.
def guardar_producto(producto, categoria):
    cursor = conexion.cursor()
    try:
            insertar_producto = """
             INSERT INTO productos (nombre, tipo, enlace, imagen, categoria, sku)
             VALUES (%s, %s, %s, %s, %s, %s)
             """
            print(producto.get_titulo(), producto.get_tipo(), producto.get_enlace(), producto.imagen, categoria, str(producto.sku))
            cursor.execute(insertar_producto, (producto.get_titulo(), producto.get_tipo(), producto.get_enlace(), producto.imagen, categoria, str(producto.sku)))

            # id = cursor.fetchone()
            conexion.commit()
    except Exception as e:
        print("Error en la consulta: 54" , e)
        conexion.rollback()
    finally:
        print("Producto guardado correctamente.")
        cursor.close()

def createConsulta(lista):
    cursor = conexion.cursor()
    try:
        fecha = lista[0].date()
        print(fecha)
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
        print("Error en la consulta: 72 ", e)
        conexion.rollback()
    finally:
        cursor.close()

def hacer_historico_producto(id_consulta,id_producto, item:Producto):
    cursor = conexion.cursor()
    try:
        precio= item.get_precio()
        descuento= item.get_descuento()
        precio_descuento = item.get_precio_desc()
        consulta = """
        INSERT INTO historicos_productos (id_producto, id_consulta, precio_original,precio_descuento, descuento) 
        VALUES (%s, %s, %s, %s, %s) RETURNING id_historico; 
        """
        cursor.execute(consulta, (id_producto, id_consulta,precio, precio_descuento, descuento))
        id_historico = cursor.fetchone()
        conexion.commit()
        print("Historico guardado correctamente. " +str(id_historico[0]))
        return id_historico[0]
    except Exception as e:
        print("Error en la consulta: 93", e)
        conexion.rollback()
    finally:
        cursor.close()
def check_producto_is_saved(producto):
    cursor = conexion.cursor()
    try:
            consulta = "select count(*) from productos where sku = %s"
            cursor.execute(consulta, (str(producto.sku),))
            count = cursor.fetchone()[0]
            if count > 0:
                print("Producto existente.")
                return True
            else:
                # print("Producto no existente")
                return False

    except Exception as e:
        print("Error en la consulta: linea 111 main", e)
        conexion.rollback()
    finally:
        cursor.close()
def check_if_is_scannedToday(item):
    cursor = conexion.cursor()
    today = date.today()
    try:
        consultar_ultima_fecha = """
                select fecha_consulta from historicos_productos h
                join public.consultas c on h.id_consulta = c.id_consulta
                join public.productos p on p.id_producto = h.id_producto
                where fecha_consulta=%s and p.sku=%s"""
        cursor.execute(consultar_ultima_fecha, (today, item.sku))
        ultima_fecha = cursor.fetchone()
        if ultima_fecha:
            print("El producto necesita esperar 24 antes de volver a checarse.")
            return False
        else:
            return True

    except Exception as e:
        print("Error en la consulta: 133 ", e)
        conexion.rollback()
    finally:
        cursor.close()



def comenzar_consulta(sexo, categoria):
    lista = UnderArmourScanner.getProducts(sexo, categoria)
    id_consulta = createConsulta(lista)
    lista = lista[2:] # Se borra la fecha y el número de resultados.

    for item in lista:
        id_producto = None
        valid = False
        existente = check_producto_is_saved(item)
        if existente:
            valid = check_if_is_scannedToday(item)
        else:
            guardar_producto(item, categoria)
            valid=True

        if valid:
            id_producto = get_idConsulta_with_Sku(item)
            id_historico = hacer_historico_producto(id_consulta, id_producto, item)
            print(id_historico)
        else:
            print("Registro no realizado")


comenzar_consulta('hombres', 'baselayer')

conexion.close()

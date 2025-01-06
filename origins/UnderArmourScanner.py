import math
from datetime import datetime

import requests

from bs4 import BeautifulSoup
from colorama import init
from entities.Producto import Producto

# Inicializa colorama (solo es necesario una vez)
init(autoreset=True)

list_productos = []
fecha_consulta = datetime.now()
resultados = '0'

def clean(texto):
    return texto.replace('\t', '').replace('\n', '').replace('\f', '')

def calcularResultados(sexo, categoria):
    URL_CONSULTA='https://www.underarmour.com.mx/es-mx/c/'+sexo+'/'+categoria+'/?page=1&sz=1'
    print('Buscando numero de productos para: '+categoria)
    busqueda = requests.get(URL_CONSULTA)
    resultados = BeautifulSoup(requests.get(URL_CONSULTA).content, 'html.parser').find('div',class_='b-plp_header-results_count').get('data-analytics-plp-count')
    print('Se encontro: '+ resultados.strip() +' resultados')
    return resultados.strip()

def sacarDescuento(precio_original, precio_descuento):
    descuento = ((precio_original - precio_descuento)/precio_original)*100
    descuento = math.floor(descuento)
    return str(descuento)

def getProducts(sexo, categoria):

    resultados = calcularResultados(sexo, categoria)
    URL_BASE = 'https://www.underarmour.com.mx/es-mx/c/' + sexo + categoria + '/?page=1&sz=' + resultados
    print('Trayendo datos...')
    pedido_obtenido = requests.get(URL_BASE).text
    # print(pedido_obtenido.status_code) <- ESTADO
    soup = BeautifulSoup(pedido_obtenido, 'html.parser')
    productos = soup.find_all('section', class_='b-products_grid-tile')
    list_productos.append(fecha_consulta)
    list_productos.append(resultados)

    for producto in productos:
        producto_obj = Producto()
        titulo = producto.find('a', class_='b-tile-name')
        producto_obj.set_titulo(clean(titulo.text).strip())
        producto_obj.set_enlace(producto.find('a', class_='b-tile-name').get('href'))
        # print(producto)

        producto_obj.imagen = producto.find('img').get('data-src')
        precio_tab = producto.find('div', class_='b-price')
        precios = precio_tab.find_all('span', class_='b-price-value')

        if len(precios) > 1:

            producto_obj.set_precio(precios[0].get('content'))

            if producto.find('span', class_='b-price-range_divider'):
                # print('Es de rangos')
                producto_obj.set_tipo('rango')
                producto_obj.set_precio_max(precios[1].get('content'))

            else:
                # print('Tiene descuentos')
                # print(Fore.RED + 'DESCUENTO DEL:' + sacarDescuento(float(precios[0].get('content')),
                #                                                    float(precios[1].get('content'))) + '%')
                producto_obj.set_descuento(sacarDescuento(float(precios[0].get('content')),float(precios[1].get('content'))))
                producto_obj.set_tipo('rebaja')
                producto_obj.set_precio_desc(precios[1].get('content'))

        else:
            producto_obj.set_tipo('single')
            if len(precios):
                producto_obj.set_precio(precios[0].get('content'))
            else:
                producto_obj.set_precio(0)

        # print(producto_obj)
        list_productos.append(producto_obj)

    return list_productos
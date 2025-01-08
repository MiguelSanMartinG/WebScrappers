from tkinter import Image


class Producto:
    
    def __init__(self, titulo=None, tipo=None, precio=None, precio_max=None, precio_desc=None, enlace=None, descuento=None, categoria=None,
                  sku=None, imagen=None):
        # Historico
        self._precio = precio
        self._precio_max = precio_max
        self._precio_desc = precio_desc
        self._tipo = tipo
        self._descuento = descuento
        # Producto
        self._titulo = titulo
        self._imagen = imagen
        self._enlace = enlace
        self._categoria = categoria
        self._sku = sku

    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self, value):
        self._categoria = value
    
    @property
    def sku(self):
        return self._sku 
    
    @sku.setter
    def sku(self, value):
        self._sku = value

    @property
    def imagen(self):
        return self._imagen
    
    @imagen.setter
    def imagen(self, value):
        self._imagen = value
    
    def get_descuento(self):
        return self._descuento

    def set_descuento(self, value):
        self._descuento = value

    def get_enlace(self):
        return self._enlace
    def set_enlace(self, enlace):
        self._enlace = enlace

    # Getter y Setter para 'titulo'
    def get_titulo(self):
        return self._titulo
    def set_titulo(self, titulo):
        self._titulo = titulo

    # Getter y Setter para 'tipo'
    def get_tipo(self):
        return self._tipo
    def set_tipo(self, tipo):
        self._tipo = tipo

    # Getter y Setter para 'precio'
    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        self._precio = precio

    # Getter y Setter para 'precio_max'
    def get_precio_max(self):
        return self._precio_max

    def set_precio_max(self, precio_max):
        self._precio_max = precio_max

    # Getter y Setter para 'precio_desc'
    def get_precio_desc(self):
        return self._precio_desc

    def set_precio_desc(self, precio_desc):
        self._precio_desc = precio_desc

    def __repr__(self):
        return (f"Producto(titulo='{self._titulo}', tipo='{self._tipo}', "
                f"precio={self._precio}, precio_max={self._precio_max}, precio_desc={self._precio_desc}, "
                f"enlace='{self._enlace}, descuento={self._descuento}, imagen={self._imagen} , sku={self._sku}, categoria={self._categoria}, )')")

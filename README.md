#  WebScraper para UNDERARMOUR.COM (Python + PostgreSQL)

Sistema de **web scraping automatizado** que consulta una tienda online UNDER ARMOUR, obtiene información de productos y almacena su histórico de precios en una base de datos PostgreSQL para analizar variaciones a lo largo del tiempo.

---
Este proyecto:

- 🔎 Accede automáticamente a una tienda online.
- 📦 Extrae información de productos por categoría.
- 💰 Guarda precio original, precio con descuento y porcentaje de descuento.
- 🗄️ Registra productos en base de datos si no existen.
- 📊 Genera un histórico diario para análisis de cambios de precio.
- 🚫 Evita duplicar registros del mismo producto el mismo día.

Está diseñado para análisis de tendencias, monitoreo de descuentos y seguimiento de estrategias de pricing.

---

## 🏗️ Arquitectura del Proyecto

El sistema está dividido en:

- `entities/Producto.py` → Modelo de datos del producto.
- `origins/UnderArmourScanner.py` → Lógica de scraping.
- `main.py` → Orquestación del flujo.
- PostgreSQL → Almacenamiento de datos históricos.

---

## 🗄️ Modelo de Base de Datos

### Tabla `productos`

| Campo | Descripción |
|-------|------------|
| id_producto | ID único |
| nombre | Nombre del producto |
| tipo | Tipo de producto |
| enlace | URL del producto |
| imagen | URL de imagen |
| categoria | Categoría |
| sku | Identificador único |

---

### Tabla `consultas`

| Campo | Descripción |
|-------|------------|
| id_consulta | ID de consulta |
| fecha_consulta | Fecha de ejecución |
| resultados | Número de resultados encontrados |

---

### Tabla `historicos_productos`

| Campo | Descripción |
|-------|------------|
| id_historico | ID histórico |
| id_producto | FK producto |
| id_consulta | FK consulta |
| precio_original | Precio normal |
| precio_descuento | Precio con descuento |
| descuento | Porcentaje de descuento |

---

## ⚙️ Instalación
### 1️ Clonar repositorio
Hay que poner usuario y contraseña de la base de datos. 
// TODO
A futuro añadir posibilidad de meterlo por comandos o texto

### 2 Clonar repositorio

```bash
git clone <tu-repositorio>
cd <tu-proyecto>
```
### 3 Hay que restaurar la base de datos, se encuentra el script en Scripts/init.sql INIT



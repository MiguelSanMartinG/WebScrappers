import re

def limpiar_y_ordenar_transacciones(texto):
    # 1. Unir todo en una sola línea
    texto = texto.replace('\n', ' ')

    # 2. Insertar salto de línea antes de cada transacción
    texto = re.sub(r'(?=\d{2}/\d{2}/\d{4} \d{2}/\d{2}/\d{4} USD)', r'\n', texto).strip()

    # 3. Convertir fechas a DD/MM/YYYY
    def convertir_fechas(match):
        mm1, dd1, yyyy1 = match.group(1).split('/')
        mm2, dd2, yyyy2 = match.group(2).split('/')
        return f"{dd1}/{mm1}/{yyyy1} {dd2}/{mm2}/{yyyy2} USD"

    texto = re.sub(r'(\d{2}/\d{2}/\d{4}) (\d{2}/\d{2}/\d{4}) USD', convertir_fechas, texto)

    # 4. Separar líneas por transacción
    lineas = texto.split('\n')

    # 5. Eliminar texto entre primer '-' y 'Principal.' o 'Program'
    lineas_limpias = []
    for linea in lineas:
        linea_limpia = re.sub(r'\s*-\s.*?(Principal\.|Program)', '', linea)
        lineas_limpias.append(linea_limpia.strip())

    # 6. Ordenar por símbolo (posición 4 normalmente)
    def extraer_ticker(linea):
        partes = linea.split()
        return partes[4] if len(partes) > 4 else ''

    lineas_ordenadas = sorted(lineas_limpias, key=extraer_ticker)

    # 7. Reemplazar espacios por tabulaciones
    lineas_con_tabs = [re.sub(r'\s+', '\t', linea) for linea in lineas_ordenadas]

    return '\n'.join(lineas_con_tabs)


# Puedes probar con este texto o agregar uno que incluya "Program"
texto_original = """
05/14/2025 05/15/2025 USD BUY VWO - VANGUARD INTL EQUITY INDEX FDS FTSE EMR MKT ETF - TRD VWO B 0.14606177 at 47.788
Principal.
0.14606177 47.788 (6.99)
05/14/2025 05/15/2025 USD BUY VHT - VANGUARD WORLD FD HEALTH CAR ETF - TRD VHT B 0.02894358 at 241.1588 Principal. 0.02894358 241.1588 (6.99)
05/14/2025 05/15/2025 USD BUY NVDA - NVIDIA CORPORATION COM - TRD NVDA B 0.10548682 at 132.3388 Principal. 0.10548682 132.3388 (13.99)
05/14/2025 05/15/2025 USD BUY AMZN - AMAZON COM INC COM - TRD AMZN B 0.06624628 at 210.7288 Principal. 0.06624628 210.7288 (13.99)
05/14/2025 05/15/2025 USD BUY VDC - VANGUARD WORLD FD CONSUM STP ETF - TRD VDC B 0.06469588 at 215.7788 Principal. 0.06469588 215.7788 (13.99)
05/14/2025 05/15/2025 USD BUY VOO - VANGUARD INDEX FDS S&P 500 ETF SHS - TRD VOO B 0.00531886 at 539.5888 Principal. 0.00531886 539.5888 (2.88)
05/20/2025 05/21/2025 USD BUY VOO - VANGUARD INDEX FDS S&P 500 ETF SHS - TRD VOO B 0.04720591 at 545.0588 Principal. 0.04720591 545.0588 (25.79)
05/20/2025 05/21/2025 USD BUY IAUM - ISHARES GOLD TR SHARES REPRESENT - TRD IAUM B 0.39347209 at 32.7088 Principal. 0.39347209 32.7088 (12.90)
05/20/2025 05/21/2025 USD BUY AMZN - AMAZON COM INC COM - TRD AMZN B 0.06326477 at 203.5888 Principal. 0.06326477 203.5888 (12.91)
05/27/2025 05/28/2025 USD BUY GOOG - ALPHABET INC CAP STK CL C - TRD GOOG B 0.29616829 at 173.7188 Principal. 0.29616829 173.7188 (51.57)
05/29/2025 05/30/2025 USD BUY IAUM - ISHARES GOLD TR SHARES REPRESENT - TRD IAUM B 0.42291752 at 33.0088 Principal. 0.42291752 33.0088 (13.99)
05/29/2025 05/30/2025 USD BUY VWO - VANGUARD INTL EQUITY INDEX FDS FTSE EMR MKT ETF - TRD VWO B 0.14695108 at 47.4988
Principal.
0.14695108 47.4988 (6.99)
05/29/2025 05/30/2025 USD BUY VPU - VANGUARD WORLD FD UTILITIES ETF - TRD VPU B 0.06551788 at 174.6088 Principal. 0.06551788 174.6088 (11.46)
05/29/2025 05/30/2025 USD BUY VDC - VANGUARD WORLD FD CONSUM STP ETF - TRD VDC B 0.07741948 at 221.7788 Principal. 0.07741948 221.7788 (17.21)
05/29/2025 05/30/2025 USD BUY AMZN - AMAZON COM INC COM - TRD AMZN B 0.04157816 at 206.5988 Principal. 0.04157816 206.5988 (8.61)
05/29/2025 05/30/2025 USD BUY GOOG - ALPHABET INC CAP STK CL C - TRD GOOG B 0.04953898 at 173.3988 Principal. 0.04953898 173.3988 (8.61)
"""

resultado = limpiar_y_ordenar_transacciones(texto_original)
print(resultado)

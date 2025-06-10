import re
from datetime import datetime

def formatear_fecha(fecha_str):
    return datetime.strptime(fecha_str, "%m/%d/%Y").strftime("%d/%m/%Y")

def analizar_operaciones(texto):
    operaciones = []
    lineas = texto.splitlines()

    buffer = ""
    for linea in lineas:
        linea = linea.strip()
        if linea:
            buffer += " " + linea

    # Agrupa bloques por fechas consecutivas (indican el inicio de una operación)
    bloques = re.findall(r"(\d{2}/\d{2}/\d{4} \d{2}/\d{2}/\d{4}.*?)(?=\d{2}/\d{2}/\d{4} \d{2}/\d{2}/\d{4}|$)", buffer)

    for bloque in bloques:
        match = re.search(
            r"(?P<fecha1>\d{2}/\d{2}/\d{4}) (?P<fecha2>\d{2}/\d{2}/\d{4}) USD (?P<tipo>BUY|SELL|CDEP) (?P<simbolo>[A-Z]+)[\s\S]*?(?P<cantidad>\d+\.\d+)\s+(?P<precio>\d+\.\d+)\s+\((?P<monto>\d+\.\d+)\)",
            bloque
        )
        if match:
            datos = match.groupdict()
            operaciones.append([
                formatear_fecha(datos["fecha1"]),
                formatear_fecha(datos["fecha2"]),
                datos["tipo"],
                datos["simbolo"],
                datos["cantidad"],
                datos["precio"],
                datos["monto"]
            ])

    return operaciones

# Ejemplo de uso
texto = """
05/14/2025 05/15/2025 USD BUY VWO - VANGUARD INTL EQUITY INDEX FDS FTSE EMR MKT ETF - TRD VWO B 0.14606177 at 47.788
Principal.
0.14606177 47.788 (6.99)
05/14/2025 05/15/2025 USD BUY VHT - VANGUARD WORLD FD HEALTH CAR ETF - TRD VHT B 0.02894358 at 241.1588 Principal. 0.02894358 241.1588 (6.99)
05/14/2025 05/15/2025 USD BUY NVDA - NVIDIA CORPORATION COM - TRD NVDA B 0.10548682 at 132.3388 Principal. 0.10548682 132.3388 (13.99)
05/14/2025 05/15/2025 USD BUY AMZN - AMAZON COM INC COM - TRD AMZN B 0.06624628 at 210.7288 Principal. 0.06624628 210.7288 (13.99)
05/14/2025 05/15/2025 USD BUY VDC - VANGUARD WORLD FD CONSUM STP ETF - TRD VDC B 0.06469588 at 215.7788 Principal. 0.06469588 215.7788 (13.99)
05/14/2025 05/15/2025 USD BUY VOO - VANGUARD INDEX FDS S&P 500 ETF SHS - TRD VOO B 0.00531886 at 539.5888 Principal. 0.00531886 539.5888 (2.88)
05/15/2025 05/15/2025 USD CDEP INSTANT_FUNDING - GMUF000625-1747231564911-DBY7I 64.85
05/20/2025 05/21/2025 USD BUY VOO - VANGUARD INDEX FDS S&P 500 ETF SHS - TRD VOO B 0.04720591 at 545.0588 Principal. 0.04720591 545.0588 (25.79)
05/20/2025 05/21/2025 USD BUY IAUM - ISHARES GOLD TR SHARES REPRESENT - TRD IAUM B 0.39347209 at 32.7088 Principal. 0.39347209 32.7088 (12.90)
05/20/2025 05/21/2025 USD BUY AMZN - AMAZON COM INC COM - TRD AMZN B 0.06326477 at 203.5888 Principal. 0.06326477 203.5888 (12.91)
05/21/2025 05/21/2025 USD CDEP INSTANT_FUNDING - GMUF000625-1747752954256-DEPQR 49.03
05/21/2025 05/21/2025 USD CDEP INSTANT_FUNDING - GMUF000625-1747753248275-D6GF2 2.58
05/27/2025 05/28/2025 USD BUY GOOG - ALPHABET INC CAP STK CL C - TRD GOOG B 0.29616829 at 173.7188 Principal. 0.29616829 173.7188 (51.57)
05/28/2025 05/28/2025 USD CDEP INSTANT_FUNDING - GMUF000625-1748355354179-DRFVT 51.57
05/29/2025 05/30/2025 USD BUY IAUM - ISHARES GOLD TR SHARES REPRESENT - TRD IAUM B 0.42291752 at 33.0088 Principal. 0.42291752 33.0088 (13.99)
05/29/2025 05/30/2025 USD BUY VWO - VANGUARD INTL EQUITY INDEX FDS FTSE EMR MKT ETF - TRD VWO B 0.14695108 at 47.4988
Principal.
0.14695108 47.4988 (6.99)
05/29/2025 05/30/2025 USD BUY VPU - VANGUARD WORLD FD UTILITIES ETF - TRD VPU B 0.06551788 at 174.6088 Principal. 0.06551788 174.6088 (11.46)
05/29/2025 05/30/2025 USD BUY VDC - VANGUARD WORLD FD CONSUM STP ETF - TRD VDC B 0.07741948 at 221.7788 Principal. 0.07741948 221.7788 (17.21)
05/29/2025 05/30/2025 USD BUY AMZN - AMAZON COM INC COM - TRD AMZN B 0.04157816 at 206.5988 Principal. 0.04157816 206.5988 (8.61)
05/29/2025 05/30/2025 USD BUY GOOG - ALPHABET INC CAP STK CL C - TRD GOOG B 0.04953898 at 173.3988 Principal. 0.04953898 173.3988 (8.61)
05/30/2025 05/30/2025 USD CDEP INSTANT_FUNDING - GMUF000625-1748528456380-DCWVV 66.87
05/15/2025 05/15/2025 USD SELL DWBDS - DW Bank Sweep (FDIC INSURED DEPOSIT NOT COVERED BY SIPC) - Credit Sweep Program -0.97 1.00 0.97
05/21/2025 05/21/2025 USD BUY DWBDS - DW Bank Sweep (FDIC INSURED DEPOSIT NOT COVERED BY SIPC) - Debit Sweep Program 0.01 1.00 (0.01)
05/28/2025 05/28/2025 USD SELL DWBDS - DW Bank Sweep (FDIC INSURED DEPOSIT NOT COVERED BY SIPC) - Credit Sweep Program -0.01 1.00 0.01
05/28/2025 05/28/2025 USD BUY DWBDS - DW Bank Sweep (FDIC INSURED DEPOSIT NOT COVERED BY SIPC) - Debit Sweep Program 0.01 1.00 (0.01)
05/30/2025 05/30/2025 USD SELL DWBDS - DW Bank Sweep (FDIC INSURED DEPOSIT NOT COVERED BY SIPC) - Credit Sweep Program -0.01 1.00 0.01
05/30/2025 05/30/2025 USD BUY DWBDS - DW Bank Sweep (FDIC INSURED DEPOSIT NOT COVERED BY SIPC) - Debit Sweep Program 0.01 1.00 (0.01)
"""

resultado = analizar_operaciones(texto)

# Mostrar resultado
for op in resultado:
    print("\n".join(op))
    print("------")

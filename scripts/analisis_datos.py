import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Rutas relativas para que funcione en Google Colab y en cualquier entorno.
BASE_DIR = Path(__file__).resolve().parent.parent
DATOS_PATH = BASE_DIR / "datos" / "sales_sample_2024.csv"
RESULTADOS_DIR = BASE_DIR / "resultados"

RESULTADOS_DIR.mkdir(exist_ok=True)

# Lectura del dataset.
df = pd.read_csv(DATOS_PATH)

# Normalización básica de nombres de columnas.
df.columns = df.columns.str.strip().str.lower()

print("Columnas detectadas:", df.columns.tolist())
print(df.head())

# Detección de columna de fecha.
if "sales_date" in df.columns:
    columna_fecha = "sales_date"
elif "fecha" in df.columns:
    columna_fecha = "fecha"
elif "date" in df.columns:
    columna_fecha = "date"
else:
    raise ValueError("No se encontró una columna de fecha válida.")

df[columna_fecha] = pd.to_datetime(df[columna_fecha])

# Detección de columna de ventas.
if "cantidad" in df.columns and "precio" in df.columns:
    df["total_venta"] = df["cantidad"] * df["precio"]
elif "sales_amount" in df.columns:
    df["total_venta"] = df["sales_amount"]
elif "amount" in df.columns:
    df["total_venta"] = df["amount"]
elif "sales" in df.columns:
    df["total_venta"] = df["sales"]
else:
    raise ValueError("No se encontró una columna de ventas válida como sales_amount, amount, sales o cantidad/precio.")

# Indicadores principales.
ventas_totales = df["total_venta"].sum()
venta_promedio = df["total_venta"].mean()
venta_maxima = df["total_venta"].max()
venta_minima = df["total_venta"].min()

# Si hay producto, calcula producto más vendido.
if "producto" in df.columns and "cantidad" in df.columns:
    producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()
else:
    producto_mas_vendido = "No disponible en el dataset"

# Agrupación mensual.
df["mes"] = df[columna_fecha].dt.to_period("M").astype(str)
ventas_por_mes = df.groupby("mes")["total_venta"].sum().reset_index()

# Exportación de resultados.
resumen = pd.DataFrame({
    "indicador": [
        "Ventas totales",
        "Venta promedio",
        "Venta máxima",
        "Venta mínima",
        "Producto más vendido"
    ],
    "valor": [
        ventas_totales,
        venta_promedio,
        venta_maxima,
        venta_minima,
        producto_mas_vendido
    ]
})

resumen.to_csv(RESULTADOS_DIR / "resumen_ventas.csv", index=False)
ventas_por_mes.to_csv(RESULTADOS_DIR / "ventas_por_mes.csv", index=False)

# Gráfico de evolución mensual de ventas.
plt.figure(figsize=(8, 5))
plt.plot(ventas_por_mes["mes"], ventas_por_mes["total_venta"], marker="o")
plt.title("Evolución mensual de ventas")
plt.xlabel("Mes")
plt.ylabel("Total de ventas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(RESULTADOS_DIR / "grafico_ventas_mensuales.png")

print("Análisis finalizado correctamente.")
print("Ventas totales:", ventas_totales)
print("Venta promedio:", venta_promedio)
print("Venta máxima:", venta_maxima)
print("Venta mínima:", venta_minima)
print("Producto más vendido:", producto_mas_vendido)

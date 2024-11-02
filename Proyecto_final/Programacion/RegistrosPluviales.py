import os
import random
import pandas as pd
import matplotlib.pyplot as plt

# Ruta para guardar archivos
path = os.path.dirname(os.path.abspath(__file__)) + "/datosAnalizados/"
os.makedirs(path, exist_ok=True)  # Crear carpeta si no existe

def crear_registros_pluviales(anio):
    """Genera registros pluviales aleatorios para un año específico."""
    meses = []
    for mes in range(12):
        dias = 31 if mes in [0, 2, 4, 6, 7, 9, 11] else 30 if mes != 1 else random.choice([28, 29])
        mes_datos = [random.randint(0, 20) for _ in range(dias)]
        meses.append(mes_datos)

    df = pd.DataFrame(meses).T
    df.columns = [f'Mes {i + 1}' for i in range(12)]
    return df

def guardar_datos_csv(df, anio):
    """Guarda el DataFrame en un archivo CSV."""
    df.to_csv(os.path.join(path, f'registroPluvial{anio}.csv'), index=False)

def cargar_datos_csv(anio):
    """Carga los datos de lluvia desde un archivo CSV."""
    try:
        return pd.read_csv(os.path.join(path, f'registroPluvial{anio}.csv'))
    except FileNotFoundError:
        return None

def mostrar_estadisticas_anuales(df):
    """Muestra la precipitación máxima, mínima y promedio del año."""
    max_lluvia = df.max().max()
    min_lluvia = df.min().min()
    prom_lluvia = df.mean().mean()
    print(f"Máxima precipitación: {max_lluvia} mm")
    print(f"Mínima precipitación: {min_lluvia} mm")
    print(f"Promedio de precipitación: {prom_lluvia:.2f} mm")

def crear_graficos_anuales(df, anio):
    """Crea gráficos para visualizar los datos de lluvia anuales."""
    suma_anual = df.sum()

    # Gráfico de barras
    plt.figure(figsize=(10, 6))
    suma_anual.plot(kind='bar', color='blue')
    plt.title(f'Lluvias Anuales en {anio}')
    plt.xlabel('Mes')
    plt.ylabel('Lluvia (mm)')
    plt.xticks(ticks=range(12), labels=[f'Mes {i + 1}' for i in range(12)], rotation=0)
    plt.savefig(os.path.join(path, f'grafico_barras_{anio}.png'))
    plt.show()

    # Gráfico de dispersión
    for mes in range(12):
        plt.scatter([mes + 1] * len(df.index), df.index + 1, label=f'Mes {mes + 1}', 
                    alpha=0.5, s=df.iloc[:, mes] * 2)

    plt.ylabel('Día (1-31)')
    plt.xlabel('Mes')
    plt.xticks(rotation=45, ha='right')
    plt.title('Gráfico de Dispersión de Lluvias')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.savefig(os.path.join(path, f'grafico_dispersion_{anio}.png'))
    plt.show()

    # Gráfico circular
    plt.figure(figsize=(8, 8))
    plt.pie(suma_anual, labels=[f'Mes {i + 1}' for i in range(12)], autopct='%1.1f%%', startangle=90)
    plt.title('Distribución de Lluvias por Mes')
    plt.axis('equal')
    plt.savefig(os.path.join(path, f'grafico_circular_{anio}.png'))
    plt.show()

    # Gráfico de líneas para la tendencia de lluvias
    plt.figure(figsize=(10, 6))
    suma_anual.plot(kind='line', marker='o', color='green')
    plt.title(f'Tendencia de Lluvias en {anio}')
    plt.xlabel('Mes')
    plt.ylabel('Lluvia (mm)')
    plt.xticks(ticks=range(12), labels=[f'Mes {i + 1}' for i in range(12)], rotation=0)
    plt.grid()
    plt.savefig(os.path.join(path, f'grafico_lineas_{anio}.png'))
    plt.show()

def mostrar_registros_mes(df, mes):
    """Muestra los registros de lluvia para un mes específico."""
    print(f"Registros pluviales para el mes {mes + 1}:")
    print(df.iloc[:, mes])

def mostrar_estadisticas_mes(df, mes):
    """Muestra estadísticas de lluvia para un mes específico."""
    max_lluvia = df.iloc[:, mes].max()
    min_lluvia = df.iloc[:, mes].min()
    prom_lluvia = df.iloc[:, mes].mean()
    print(f"Máxima precipitación en el mes {mes + 1}: {max_lluvia} mm")
    print(f"Mínima precipitación en el mes {mes + 1}: {min_lluvia} mm")
    print(f"Promedio de precipitación en el mes {mes + 1}: {prom_lluvia:.2f} mm")

    # Gráfico circular para los días del mes
    dias = len(df.iloc[:, mes])
    plt.figure(figsize=(8, 8))
    plt.pie(df.iloc[:, mes], labels=[f'Día {i + 1}' for i in range(dias)], autopct='%1.1f%%', startangle=90)
    plt.title(f'Distribución de Lluvias en el Mes {mes + 1}')
    plt.axis('equal')
    plt.savefig(os.path.join(path, f'grafico_circular_mes_{mes + 1}.png'))
    plt.show()

def main():
    """Función principal para ejecutar el programa."""
    print('*' * 50, '\n Menú')
    print('*' * 50)

    while True:
        anio = input("Ingrese el año para cargar los registros pluviales: ")
        df = cargar_datos_csv(anio)

        if df is None:
            print(f"No se encontraron registros para el año {anio}. Generando datos aleatorios...")
            df = crear_registros_pluviales(anio)
            guardar_datos_csv(df, anio)
            print(f"Datos aleatorios generados y guardados en registroPluvial{anio}.csv.")
        else:
            print(f"Registros pluviales del año {anio} cargados.")

        # Mostrar estadísticas anuales
        mostrar_estadisticas_anuales(df)

        # Crear gráficos anuales
        crear_graficos_anuales(df, anio)

        # Solicitar mes y validar entrada
        while True:
            try:
                mes_elegido = int(input("Seleccione un mes (1-12): ")) - 1
                if 0 <= mes_elegido < 12:
                    mostrar_registros_mes(df, mes_elegido)
                    mostrar_estadisticas_mes(df, mes_elegido)
                    break
                else:
                    print("Mes inválido. Intente nuevamente.")
            except ValueError:
                print("Entrada inválida. Por favor, intente de nuevo.")

        if input("¿Desea consultar otro año? (s/n): ").lower() != 's':
            break

if __name__ == "__main__":
    main()
import os #utilizar OS por recomendacion de mis compañeros
import random
import pandas as pd
import matplotlib.pyplot as plt

def crear_registros_pluviales(anio):
    """Genera registros pluviales aleatorios para un año específico."""
    meses = []  # Lista para almacenar los datos de lluvia de cada mes
    for mes in range(12):  # Iterar sobre los 12 meses
        # Determinar el número de días en el mes:
        # 31 días para meses con 31 días, 30 para los que tienen 30, y 28/29 para febrero
        dias = 31 if mes in [0, 2, 4, 6, 7, 9, 11] else 30 if mes != 1 else random.choice([28, 29])
        
        # Generar datos aleatorios de lluvia para cada día del mes (0 a 20 mm)
        mes_datos = [random.randint(0, 20) for _ in range(dias)]
        meses.append(mes_datos)  # Agregar los datos del mes a la lista

    # Crear un DataFrame a partir de los datos
    df = pd.DataFrame(meses).T  # Transponer para que los meses sean columnas
    df.columns = [f'Mes {i + 1}' for i in range(12)]  # Nombrar las columnas como 'Mes 1', 'Mes 2', etc.
    return df

def guardar_datos_csv(df, anio):
    """Guarda el DataFrame en un archivo CSV."""
    df.to_csv(f'registroPluvial{anio}.csv', index=False)  # Guardar sin incluir el índice

def cargar_datos_csv(anio):
    """Carga los datos de lluvia desde un archivo CSV."""
    try:
        return pd.read_csv(f'registroPluvial{anio}.csv')  # Leer el archivo CSV
    except FileNotFoundError:
        return None  # Si el archivo no existe, devolver None

def mostrar_registros_mes(df, mes):
    """Muestra los registros de lluvia para un mes específico."""
    print(f"Registros pluviales para el mes {mes + 1}:")  # Mostrar el mes
    print(df.iloc[:, mes])  # Imprimir los datos del mes seleccionado

def crear_graficos(df, anio):
    """Crea gráficos para visualizar los datos de lluvia."""
    suma_anual = df.sum()  # Sumar las lluvias de cada mes para obtener totales anuales
    meses_nombres = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
                     'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']  # Nombres de los meses

    # Gráfico de barras sobre lluvias anuales
    plt.figure(figsize=(10, 6))  # Configurar el tamaño de la figura
    suma_anual.plot(kind='bar', color='blue')  # Crear gráfico de barras
    plt.title(f'Lluvias Anuales en {anio}')  # Título del gráfico
    plt.xlabel('Mes')  # Etiqueta del eje X
    plt.ylabel('Lluvia (mm)')  # Etiqueta del eje Y
    plt.xticks(ticks=range(12), labels=meses_nombres, rotation=0)  # Etiquetas de los meses
    plt.show()  # Mostrar el gráfico

    # Gráfico de dispersión para visualizar la lluvia por día en cada mes
    for mes in range(12):
        # Crear un gráfico de dispersión para cada mes
        plt.scatter([meses_nombres[mes]] * len(df.index), df.index + 1, 
                    label=f'{meses_nombres[mes]}', alpha=0.5, 
                    s=df.iloc[:, mes] * 2)  # Tamaño proporcional a la lluvia

    plt.ylabel('Día (1-31)')  # Etiqueta del eje Y
    plt.xlabel('Mes')  # Etiqueta del eje X
    plt.xticks(rotation=45, ha='right')  # Rotar etiquetas de los meses
    plt.title('Gráfico de Dispersión de Lluvias')  # Título del gráfico
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Leyenda
    plt.tight_layout()  # Ajustar diseño
    plt.show()  # Mostrar el gráfico

    # Gráfico circular para la distribución de lluvias por mes
    plt.figure(figsize=(8, 8))  # Configurar tamaño
    plt.pie(suma_anual, labels=meses_nombres, autopct='%1.1f%%', startangle=90)  # Gráfico circular
    plt.title('Distribución de Lluvias por Mes')  # Título
    plt.axis('equal')  # Para que el gráfico sea un círculo
    plt.show()  # Mostrar gráfico

def main():
    """Función principal para ejecutar el programa."""
    print('*' * 50, '\n Menú')  # Separador en la consola
    print('*' * 50)

    while True:
        # Solicitar el año al usuario
        anio = input("Ingrese el año para cargar los registros pluviales: ")
        df = cargar_datos_csv(anio)  # Cargar datos desde el CSV

        if df is None:  # Si no hay datos, generar nuevos
            print(f"No se encontraron registros para el año {anio}. Generando datos aleatorios...")
            df = crear_registros_pluviales(anio)  # Generar datos aleatorios
            guardar_datos_csv(df, anio)  # Guardar en CSV
            print(f"Datos aleatorios generados y guardados en registroPluvial{anio}.csv.")
        else:
            print(f"Registros pluviales del año {anio} cargados.")  # Confirmación de carga

        # Solicitar mes y validar entrada
        while True:
            try:
                mes_elegido = int(input("Seleccione un mes (1-12): ")) - 1  # Ajustar índice a 0
                if 0 <= mes_elegido < 12:  # Validar entrada
                    mostrar_registros_mes(df, mes_elegido)  # Mostrar datos del mes elegido
                    break  # Salir del bucle si la entrada es válida
                else:
                    print("Mes inválido. Intente nuevamente.")
            except ValueError:
                print("Entrada inválida. Por favor, intente de nuevo.")

        if input("¿Desea consultar otro año? (s/n): ").lower() != 's':  # Preguntar si desea continuar
            break  # Salir del bucle principal

    # Llamar a la función de gráficos al final
    crear_graficos(df, anio)  # Graficar datos al final del programa

if __name__ == "__main__":
    main()  # Ejecutar la función principal
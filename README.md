TSUNDOKU: Sistema Integral de Gestión de Librerías
Institución: Instituto Superior Politécnico de Córdoba
Autores: Nicolás Menón, Noelia Soto, Federico Leyria

Tabla de Contenidos
Descripción del Proyecto
Justificación
Objetivos del Proyecto
Objetivo General
Objetivos Específicos
Estructura del Proyecto
Archivos Principales
Archivos de Bases de Datos y Consultas
Archivos Complementarios
Documentación del Proyecto
Requisitos
Instalación
Cómo Ejecutar y Probar el Programa
Inconvenientes y Soluciones
Descripción del Proyecto
TSUNDOKU es un sistema integral para la gestión de librerías, diseñado para simplificar el registro y administración de libros, usuarios y actividades. La lógica de negocio se desarrolla en Python, y los datos se gestionan con MySQL. El proyecto se ha dividido en varias etapas, que incluyen planificación, desarrollo, pruebas de usabilidad e integración, y una presentación final.

Justificación
Este sistema responde a la necesidad de gestionar librerías de forma accesible, especialmente para pequeños negocios y usuarios sin experiencia técnica. TSUNDOKU facilita la administración de inventarios y usuarios, optimizando la gestión de recursos literarios y el acceso al conocimiento mediante una interfaz intuitiva y funcional.

Objetivos del Proyecto
Objetivo General
Desarrollar un sistema de gestión de librerías que permita el registro y control de libros y usuarios, accesible y fácil de usar para personas sin experiencia técnica.

Objetivos Específicos
Desarrollar un sistema de registro de libros y usuarios en Python y MySQL.
Implementar módulos de control de acceso y autenticación para proteger la seguridad y privacidad de los datos.
Realizar pruebas de usabilidad e integración, corrigiendo errores para asegurar una experiencia de usuario óptima.
Estructura del Proyecto
Archivos Principales
main.py: Archivo principal que gestiona la interfaz de usuario, incluyendo bienvenida, inicio de sesión, registro de usuarios, verificación de captchas y registro de actividades en archivos de texto.
menu2.py: Gestiona las opciones del menú principal y la navegación en la aplicación.
captcha.py: Genera captchas basados en operaciones matemáticas aleatorias para validar que el usuario no sea un bot.
aritmetica.py: Contiene funciones para operaciones aritméticas básicas (suma, resta, multiplicación, división) y cálculos de suma y promedio.
acceso.py: Gestiona el acceso y la autenticación de usuarios, definiendo la clase Acceso, que almacena información de cada sesión.
tiempo.py: Registra la fecha y hora actuales, proporcionando un registro temporal de actividades.
usuario.py: Gestiona la creación, actualización, eliminación y búsqueda de usuarios, incluyendo verificación captcha para evitar registros automatizados.
Archivos de Bases de Datos y Consultas
Queries.sql: Consultas SQL para la gestión de datos en la base de datos.
libreria.sql: Script SQL para crear y poblar la base de datos de la librería.
Archivos Complementarios
Programacion/: Carpeta con scripts y archivos relacionados con la programación del sistema.
datosAnalizados/: Carpeta para almacenar datos procesados y analizados.
RegistrosPluviales.py: Script para gestionar registros pluviales dentro del sistema.
backend.py: Módulo backend que soporta la lógica de negocio del sistema.
conexionbd.py: Script para gestionar la conexión a la base de datos MySQL.
gestor_usuarios.py: Módulo de gestión de usuarios (CRUD).
logs.txt: Archivo de registro de actividades del sistema.
usuarios.ispc: Archivo con datos de usuarios en un formato específico.
accesos.ispc: Archivo para registrar accesos de usuarios.
registroPluvial2023.csv: Archivo CSV con datos de registros pluviales de 2023.
Documentación del Proyecto
Estructura del Proyecto Final.pdf: Documento que describe la estructura, funcionalidad y organización del proyecto TSUNDOKU.
Requisitos
Para el correcto funcionamiento de TSUNDOKU, es necesario contar con las siguientes herramientas:

Visual Studio Code: Editor de código para facilitar la edición y ejecución de scripts en Python.
MySQL: Sistema de gestión de base de datos para almacenar la información de la librería.
MySQL Workbench: Herramienta gráfica para la administración de bases de datos.
Instalación
Clona el repositorio de TSUNDOKU en tu máquina local:
bash
Copiar código
git clone https://github.com/tu_usuario/tsundoku.git
Ejecuta los scripts libreria.sql y Queries.sql para crear y poblar la base de datos en MySQL.
Abre el archivo main.py en Visual Studio Code.
Ejecuta main.py y sigue las instrucciones en pantalla para iniciar la aplicación.
Cómo Ejecutar y Probar el Programa
Inicia la aplicación abriendo main.py en Visual Studio Code y ejecutando el script.
El sistema solicitará un nombre de usuario y contraseña para iniciar sesión.
Una vez dentro, el menú principal permitirá gestionar el inventario de la librería y administrar usuarios.
Inconvenientes y Soluciones
Durante el desarrollo de TSUNDOKU, surgieron algunos inconvenientes, como problemas de conexión a la base de datos y dificultades en la verificación de captchas. Estos problemas se solucionaron configurando adecuadamente MySQL y revisando las funciones de generación y validación de captchas, lo que mejoró la estabilidad del sistema.

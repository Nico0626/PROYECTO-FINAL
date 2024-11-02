TSUNDOKU
TSUNDOKU esta diseñado para gestionar una librería, permitiendo a los usuarios interactuar con el sistema sin necesidad de conocimientos previos en programación.
Archivos del Proyecto
main.py: Archivo principal que gestiona la interfaz de usuario, incluyendo la bienvenida, el inicio de sesión, el registro de usuarios, la verificación de captchas y el registro de actividades en archivos de texto.

menu2.py: Maneja las opciones del menú principal y la navegación en la aplicación.

captcha.py: Genera captchas basados en operaciones matemáticas aleatorias y valida que el usuario no sea un bot.

aritmetica.py: Define las funciones básicas para operaciones aritméticas como sumar, restar, multiplicar y dividir, así como cálculos de suma y promedio sobre múltiples números.

acceso.py: Gestiona el acceso de los usuarios y la autenticación en la aplicación. Define la clase Acceso, que almacena información sobre cada sesión de acceso.

tiempo.py: Genera un registro temporal, muestra la fecha y hora actuales en formato año/mes/día y la hora en formato hora:minuto.

usuario.py: Gestiona la creación, actualización, eliminación y búsqueda de usuarios. También incorpora un captcha para verificar que el usuario no sea un bot al crear nuevas cuentas.

Requisitos
Para el correcto funcionamiento de TSUNDOKU, es necesario instalar:

Visual Studio Code: Un editor de código que facilita la edición y ejecución de scripts Python.
MySQL: Para gestionar la base de datos que almacena la información de la librería.
MySQL Workbench: Herramienta para visualizar y manejar bases de datos de manera gráfica.
Instalación
Clona el repositorio de TSUNDOKU en tu máquina local.
Ejecuta los scripts SQL proporcionados para crear y poblar la base de datos.
Abre el archivo main.py en Visual Studio Code.
Ejecuta main.py y sigue las instrucciones en pantalla.
Cómo ejecutar y probar este programa
Para ejecutar la aplicación, abre main.py en Visual Studio Code y corre el script.
El sistema te pedirá un nombre de usuario y contraseña para acceder.
Después de iniciar sesión, se mostrará un menú principal que te permitirá gestionar la librería.
Inconvenientes y Soluciones
Durante el desarrollo de TSUNDOKU, se encontraron algunos inconvenientes, como problemas con la conexión a la base de datos y la verificación de captchas. Sin embargo, se lograron superar (?) implementando una configuración adecuada de MySQL y revisando las funciones de generación y validación de captchas.

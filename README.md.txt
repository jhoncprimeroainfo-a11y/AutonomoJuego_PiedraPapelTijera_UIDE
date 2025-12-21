#PROYECTO INTEGRADOR: El Impacto de las Nuevas Tecnologías en la Sociedad #"Simulador de Decisiones Algorítmicas: Visualización del Futuro"
#Ficha Técnica Académica

Autor: Jhon Cabezas
Institución: UIDE
Asignatura: Lógica de Programación
Fecha de Entrega: 21 de Diciembre de 2025
Evaluación: Contacto con el Docente (Semana 8)
#1. DESCRIPCIÓN DEL PROBLEMA Y PROPÓSITO Contexto: Vivimos en una sociedad mediada por "cajas negras" tecnológicas. Interactuamos diariamente con algoritmos (redes sociales, IAs, fintech) sin comprender la lógica probabilística que los rige.

Propósito del Proyecto: Este software no es un simple juego; es una herramienta de alfabetización digital gamificada. Su objetivo es permitir al usuario visualizar el futuro de la interacción humano-máquina, enfrentando su intuición biológica contra la probabilidad matemática de un algoritmo en un entorno controlado.

A través de la persistencia de datos (Big Data a escala), el sistema analiza si el ser humano puede aprender patrones o si la máquina domina la toma de decisiones a largo plazo.

#2. INTEGRACIÓN CURRICULAR (Semanas 1 - 8) Este proyecto es el resultado de la aplicación práctica de todo el sílabo de la materia:

#UNIDAD 1: Resolución de Problemas y Entorno (Semanas 1-2)

Entorno de Desarrollo: Configuración profesional usando VS Code y control de versiones con Git/GitHub.
Análisis: Previo a la codificación, se estructuró la solución utilizando lógica algorítmica para resolver el problema de la "toma de decisiones bajo incertidumbre".
#UNIDAD 2: Manejo de Datos y Algoritmos (Semanas 3-4)

Tipos de Datos: Uso estricto de tipado dinámico en Python (Enteros para lógica, Strings para UI, Booleanos para estados).
Operadores: Implementación de contadores acumulativos (+=) y comparadores lógicos para determinar victorias y derrotas.
#UNIDAD 3: Lógica de Programación (Semanas 5-6)

Condicionales Complejos: Se aplicaron estructuras IF/ELIF/ELSE con operadores lógicos (AND, OR) para modelar las reglas del sistema extendido ("Big Bang Theory"), demostrando capacidad de manejar múltiples condiciones de verdad.
Bucles (Loops):
Transición del bucle while True (consola) al mainloop() (eventos gráficos).
Uso de bucles for para la generación dinámica de elementos en la interfaz.
#UNIDAD 4: Estructura de Datos y Funciones (Semanas 7-8) Esta es la capa más avanzada del software, implementando los temas finales:

TUPLAS (Datos Inmutables):
Implementadas en CONFIG_VENTANA y COLORES. Se eligieron tuplas para garantizar que la configuración estética y dimensional del software no sea alterada durante la ejecución.
LISTAS (Datos Mutables y Ordenados):
Utilizadas en rango_opciones = [1, 2, 3...]. Permiten la escalabilidad del sistema; si se desea agregar más armas al juego, solo se modifica la lista y la interfaz se reconstruye sola.
DICCIONARIOS (Estructuras Clave-Valor):
self.mapa_entidades: Relaciona la lógica numérica del backend con la representación semántica (Emojis) del frontend.
Persistencia JSON: El historial de datos se manipula como un diccionario de Python antes de ser serializado al disco.
FUNCIONES (Modularidad):
Funciones con Retorno: determinar_ganador_logica(u, pc) recibe parámetros de entrada y retorna un valor booleano (True/False), desacoplando la lógica matemática de la interfaz visual.
Funciones de Procedimiento: guardar_datos_json() ejecuta acciones de E/S sin retorno.
#3. EVOLUCIÓN TÉCNICA DEL PROYECTO El proyecto sufrió una transformación significativa para cumplir con los estándares de "Nuevas Tecnologías":

De CLI a GUI: Se migró de una interfaz de línea de comandos (texto plano) a una Interfaz Gráfica de Usuario (Tkinter). Esto simula la evolución real del software moderno, priorizando la Experiencia de Usuario (UX).
De Volátil a Persistente: Se implementó un motor de base de datos local (JSON). A diferencia del prototipo inicial donde los datos se perdían al cerrar, la versión final mantiene un registro histórico ("Memory"), permitiendo análisis estadísticos a largo plazo.
#4. INSTRUCCIONES DE USO

Clonar el repositorio: Descargue los archivos en su equipo local.
Ejecutar: Abra la terminal y corra python proyecto_integrador.py.
Nueva Simulación: Seleccione el modo (Clásico o Extendido) y compita contra el algoritmo.
Ver Análisis: Acceda al botón "MEMORIA DEL SISTEMA" para visualizar las métricas de eficiencia (Intuición vs Probabilidad).
#5. CONCLUSIÓN El Simulador de Decisiones cumple con el objetivo académico de integrar las 4 unidades de estudio. A nivel social, demuestra que la tecnología, cuando se visualiza correctamente, deja de ser una "caja negra" y se convierte en una herramienta medible y comprensible.
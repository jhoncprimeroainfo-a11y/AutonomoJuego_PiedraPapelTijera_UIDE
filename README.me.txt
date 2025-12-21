# ⚡ PROYECTO INTEGRADOR: "ROCK, PAPER, SCISSORS, LIZARD, SPOCK"
### El Impacto de las Nuevas Tecnologías en la Sociedad (Gamificación)

---

## 📋 Ficha Técnica
* **Autor:** Jhon Cabezas
* **Materia:** Lógica de Programación
* **Evaluación:** Contacto con el Docente (Semana 8)
* **Tema:** Gamificación de Algoritmos y Lógica Computacional.

---

## 1. DESCRIPCIÓN Y PROPÓSITO CREATIVO
**¿El problema?** La lógica de programación suele enseñarse de forma abstracta y aburrida.
**¿La solución?** Este proyecto utiliza el concepto de **Gamificación** para visualizar algoritmos complejos. 

Inspirado en la serie *The Big Bang Theory*, este software implementa las reglas extendidas del juego "Piedra, Papel, Tijera, Lagarto, Spock". El propósito es demostrar cómo la **tecnología** puede modelar reglas lógicas complejas (5 variables interactuando entre sí) y analizar la interacción entre la intuición humana y el azar informático.

---

## 2. INTEGRACIÓN CURRICULAR (Semanas 1 - 8)
El código integra explícitamente todos los temas del sílabo:

### 🟢 Unidades 1 y 2: Fundamentos
* **Entorno:** Desarrollo en VS Code gestionado con Git/GitHub.
* **Algoritmos:** Se diseñó un flujo lógico capaz de manejar 5 condiciones de victoria sin errores.

### 🟠 Unidad 3: Lógica de Control
* **Condicionales Complejos:** Uso de `AND` y `OR` para programar las reglas de Sheldon Cooper (ej: *Tijera corta papel AND Tijera decapita lagarto*).
* **Bucles:** Implementación de bucles de eventos (`mainloop`) para la interfaz gráfica.

### 🟣 Unidad 4: Estructuras de Datos (El Nivel Experto)
Aquí reside la potencia del software:
1.  **TUPLAS (Inmutabilidad):** Usadas en `CONFIG_JUEGO` y `COLORES` para definir la estética fija del programa.
2.  **LISTAS (Dinámismo):** Usadas para generar los botones de juego dinámicamente (`[1,2,3,4,5]`), permitiendo escalar el juego fácilmente.
3.  **DICCIONARIOS (Mapeo):** Usados para conectar la lógica numérica con los "Assets" del juego (Emojis y Nombres) y para gestionar la base de datos.
4.  **FUNCIONES Y PERSISTENCIA:** * Modularización con funciones que retornan valores (`logica_victoria`).
    * **Persistencia JSON:** El juego guarda un historial permanente de "Sheldon vs Jugador", simulando una base de datos real.

---

## 3. IMPACTO TECNOLÓGICO
Este proyecto demuestra la evolución del software:
1.  **Evolución de Interfaz:** Migración de una consola de texto lineal a una **Interfaz Gráfica (GUI)** moderna orientada a eventos.
2.  **Persistencia de Datos:** Implementación de almacenamiento en **JSON**, demostrando cómo las aplicaciones modernas retienen la información del usuario (Big Data).

---

## 4. INSTRUCCIONES
1.  Clonar el repositorio.
2.  Ejecutar `proyecto_integrador.py`.
3.  Elegir "Reglas Big Bang Theory".
4.  ¡Intentar vencer a la CPU!

---
*"Bazinga!"*
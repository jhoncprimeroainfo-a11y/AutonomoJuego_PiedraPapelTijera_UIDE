import tkinter as tk
from tkinter import messagebox
import random
import json
import os

# ======================================================
# TEMA: TUPLAS (Datos Inmutables)
# ======================================================
CONFIG_JUEGO = ("650x750", "Simulador: Humano vs Robo-Sheldon")
# Paleta de colores "Tech/Geek"
COLORES = ("#2c3e50", "#ecf0f1", "#f39c12", "#e74c3c", "#2ecc71") 
# Indices: 0:Fondo, 1:Texto, 2:Amarillo, 3:Rojo, 4:Verde

ARCHIVO_DB = "historial_robo_sheldon.json"

class JuegoBigBang:
    def __init__(self, root):
        self.root = root
        # Desempaquetado de Tupla
        geom, titulo = CONFIG_JUEGO 
        self.root.title(titulo)
        self.root.geometry(geom)
        self.root.configure(bg=COLORES[0])

        # Cargar historial (Persistencia)
        self.datos = self.cargar_datos()

        # Variables de estado
        self.version = 1
        self.modo = 1
        self.meta = 1
        self.v_ronda = 0
        self.d_ronda = 0

        # ======================================================
        # TEMA: DICCIONARIOS (Mapeo de Datos)
        # ======================================================
        self.mapa_assets = {
            1: "Piedra 🗿", 2: "Papel 📄", 3: "Tijera ✂️", 
            4: "Lagarto 🦎", 5: "Spock 🖖"
        }
        
        self.mostrar_menu()

    # ======================================================
    # TEMA: FUNCIONES (Modularidad - Unidad)
    # ======================================================
    def cargar_datos(self):
        """Función con RETORNO: Recupera datos del JSON"""
        base = {"victorias_robo": 0, "victorias_humano": 0, "partidas": 0}
        if not os.path.exists(ARCHIVO_DB):
            return base
        try:
            with open(ARCHIVO_DB, "r") as f:
                return json.load(f)
        except:
            return base

    def guardar_datos(self):
        """Función de PROCEDIMIENTO: Escribe en el JSON"""
        try:
            with open(ARCHIVO_DB, "w") as f:
                json.dump(self.datos, f, indent=4)
        except Exception as e:
            print(f"Error guardando: {e}")

    def limpiar_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # --- VISTA: MENÚ PRINCIPAL ---
    def mostrar_menu(self):
        self.limpiar_frame()
        
        # Título Impactante
        tk.Label(self.root, text="⚡ BAZINGA! ⚡", font=("Comic Sans MS", 26, "bold"), bg=COLORES[0], fg=COLORES[2]).pack(pady=(50, 10))
        tk.Label(self.root, text="VS. ROBO-SHELDON v3.0", font=("Arial", 14, "bold"), bg=COLORES[0], fg="white").pack()

        # Estadísticas rápidas
        stats = f"Simulaciones Totales: {self.datos['partidas']}"
        tk.Label(self.root, text=stats, font=("Consolas", 10), bg="#34495e", fg="#bdc3c7", padx=15, pady=5).pack(pady=20)

        estilo_btn = {"font": ("Arial", 12, "bold"), "width": 25, "pady": 10, "cursor": "hand2"}
        
        tk.Button(self.root, text="🤖 INICIAR DESAFÍO", command=self.configurar, bg="#3498db", fg="white", **estilo_btn).pack(pady=10)
        tk.Button(self.root, text="💾 MEMORIA DEL SISTEMA", command=self.ver_stats, bg="#9b59b6", fg="white", **estilo_btn).pack(pady=10)
        tk.Button(self.root, text="❌ CERRAR SISTEMA", command=self.root.quit, bg="#c0392b", fg="white", **estilo_btn).pack(pady=10)

    # --- VISTA: ESTADÍSTICAS ---
    def ver_stats(self):
        self.limpiar_frame()
        v_h = self.datos['victorias_humano']
        v_robo = self.datos['victorias_robo']
        total = self.datos['partidas']

        tk.Label(self.root, text="📊 ANÁLISIS DE RENDIMIENTO", font=("Arial", 18, "bold"), bg=COLORES[0], fg="white").pack(pady=30)
        
        resumen = (f"Eventos Procesados: {total}\n\n"
                   f"🧠 Intuición Humana: {v_h}\n"
                   f"🤖 Algoritmo Cooper: {v_robo}")
        
        tk.Label(self.root, text=resumen, font=("Courier", 16, "bold"), bg="#34495e", fg="#ecf0f1", padx=30, pady=30).pack()
        tk.Button(self.root, text="⏪ Volver al Menú", command=self.mostrar_menu, font=("Arial", 12), bg="#95a5a6", fg="white").pack(pady=30)

    # --- VISTA: CONFIGURACIÓN ---
    def configurar(self):
        self.limpiar_frame()
        tk.Label(self.root, text="⚙️ PARÁMETROS DEL DUELO", font=("Arial", 18, "bold"), bg=COLORES[0], fg="white").pack(pady=30)

        self.var_version = tk.IntVar(value=2)
        self.var_modo = tk.IntVar(value=1)

        # Selección de Versión
        tk.Label(self.root, text="Nivel de Complejidad Lógica:", font=("Arial", 12), bg=COLORES[0], fg=COLORES[2]).pack(pady=(10,5))
        tk.Radiobutton(self.root, text="Clásico (3 Variables)", variable=self.var_version, value=1, bg=COLORES[0], fg="white", selectcolor=COLORES[0], font=("Arial", 11)).pack()
        tk.Radiobutton(self.root, text="Big Bang Theory (5 Variables)", variable=self.var_version, value=2, bg=COLORES[0], fg="white", selectcolor=COLORES[0], font=("Arial", 11)).pack()

        # Selección de Modo
        tk.Label(self.root, text="Tipo de Ejecución:", font=("Arial", 12), bg=COLORES[0], fg=COLORES[2]).pack(pady=(20,5))
        tk.Radiobutton(self.root, text="Muerte Súbita (1 Ronda)", variable=self.var_modo, value=1, bg=COLORES[0], fg="white", selectcolor=COLORES[0], font=("Arial", 11)).pack()
        tk.Radiobutton(self.root, text="Torneo (Mejor de 3)", variable=self.var_modo, value=2, bg=COLORES[0], fg="white", selectcolor=COLORES[0], font=("Arial", 11)).pack()

        tk.Button(self.root, text="⚡ EJECUTAR ⚡", command=self.iniciar_juego, bg=COLORES[4], fg="white", font=("Arial", 16, "bold"), width=20).pack(pady=40)

    # --- VISTA: JUEGO (Con Diseño 3 arriba / 2 abajo) ---
    def iniciar_juego(self):
        self.version = self.var_version.get()
        self.modo = self.var_modo.get()
        self.meta = 3 if self.modo == 2 else 1
        self.v_ronda = 0
        self.d_ronda = 0
        
        self.limpiar_frame()
        
        titulo = "🔥 PROTOCOLO EXTENDIDO" if self.version == 2 else "🗿 PROTOCOLO CLÁSICO"
        tk.Label(self.root, text=titulo, font=("Arial", 16, "bold"), bg=COLORES[0], fg=COLORES[2]).pack(pady=20)
        
        # Marcador
        self.lbl_score = tk.Label(self.root, text=f"Humano 0  -  0 Robo-Sheldon", font=("Arial", 20, "bold"), bg=COLORES[0], fg="white")
        self.lbl_score.pack(pady=10)
        
        # Estado
        self.lbl_feed = tk.Label(self.root, text="Esperando entrada de datos...", font=("Arial", 14), bg=COLORES[0], fg="#bdc3c7")
        self.lbl_feed.pack(pady=20)

        # ======================================================
        # TEMA: LISTAS (Generación Dinámica de Interfaz)
        # ======================================================
        
        if self.version == 1:
            # --- MODO CLÁSICO (3 en fila) ---
            frame_fila = tk.Frame(self.root, bg=COLORES[0])
            frame_fila.pack(pady=20)
            lista_opciones = [1, 2, 3]
            
            for n in lista_opciones:
                self.crear_boton(frame_fila, n)
                
        else:
            # --- MODO EXTENDIDO (Diseño 3 arriba / 2 abajo) ---
            
            # Fila Superior (Piedra, Papel, Tijera)
            frame_arriba = tk.Frame(self.root, bg=COLORES[0])
            frame_arriba.pack(pady=(20, 10)) # Un poco de espacio abajo
            
            lista_arriba = [1, 2, 3]
            for n in lista_arriba:
                self.crear_boton(frame_arriba, n)

            # Fila Inferior (Lagarto, Spock)
            frame_abajo = tk.Frame(self.root, bg=COLORES[0])
            frame_abajo.pack(pady=(0, 20))
            
            lista_abajo = [4, 5]
            for n in lista_abajo:
                self.crear_boton(frame_abajo, n)

    def crear_boton(self, frame_padre, numero_opcion):
        """Función auxiliar para crear botones idénticos"""
        tk.Button(frame_padre, 
                  text=self.mapa_assets[numero_opcion], 
                  font=("Arial", 14), 
                  cursor="hand2",
                  bg="#ecf0f1", # Fondo claro para el botón
                  command=lambda x=numero_opcion: self.procesar_jugada(x)
                 ).pack(side=tk.LEFT, padx=10, ipadx=10, ipady=5)

    def logica_victoria(self, u, pc):
        """Lógica de Sheldon Cooper: Retorna True/False/None"""
        if u == pc: return None
        gana = (
            (u == 1 and pc in (3, 4)) or (u == 2 and pc in (1, 5)) or
            (u == 3 and pc in (2, 4)) or (u == 4 and pc in (2, 5)) or
            (u == 5 and pc in (1, 3))
        )
        return gana

    def procesar_jugada(self, u):
        limite = 5 if self.version == 2 else 3
        pc = random.randint(1, limite)
        
        res = self.logica_victoria(u, pc)
        
        txt = f"Humano: {self.mapa_assets[u]}  vs  Robo-Sheldon: {self.mapa_assets[pc]}"

        if res is None:
            self.lbl_feed.config(text=f"{txt}\n😐 Sincronización Lógica (EMPATE)", fg=COLORES[2])
        elif res:
            self.lbl_feed.config(text=f"{txt}\n🎉 ¡Error en mi sistema! PUNTO PARA TI", fg=COLORES[4])
            self.v_ronda += 1
        else:
            self.lbl_feed.config(text=f"{txt}\n🤖 Calculando victoria... PUNTO PARA MÍ", fg=COLORES[3])
            self.d_ronda += 1
        
        self.lbl_score.config(text=f"Humano {self.v_ronda}  -  {self.d_ronda} Robo-Sheldon")

        if self.v_ronda == self.meta or self.d_ronda == self.meta:
            self.fin_partida()

    def fin_partida(self):
        if self.v_ronda > self.d_ronda:
            msg, titulo = "¡Bazinga! Mi algoritmo ha fallado. ¡Ganaste!", "VICTORIA HUMANA"
            self.datos['victorias_humano'] += 1
            icono = "info"
        else:
            msg, titulo = "Procesando... ¡Soy superior! ¡Bazinga!", "VICTORIA ALGORITMO"
            self.datos['victorias_robo'] += 1
            icono = "warning"
        
        self.datos['partidas'] += 1
        self.guardar_datos()
        
        messagebox.showinfo(titulo, msg, icon=icono)
        self.mostrar_menu()

if __name__ == "__main__":
    ventana = tk.Tk()
    app = JuegoBigBang(ventana)
    ventana.mainloop()
import random

def main():
    # Variables de persistencia
    victorias = 0
    derrotas = 0

    while True:
        print("\n" + "═"*40)
        print("     🎮 MENÚ PRINCIPAL DEL JUEGO 🎮")
        print("═"*40)
        print("1️⃣  Jugar")
        print("2️⃣  Ver Estadísticas")
        print("3️⃣  Salir")
        
        try:
            opcion = int(input("\n👉 Elige una opción (1-3): "))
        except ValueError:
            print("❌ Error: Debes ingresar un número.")
            continue

        if opcion == 3:
            print("\n👋 ¡Gracias por jugar! Cerrando sistema...")
            break

        if opcion == 2:
            print("\n📊 --- TUS ESTADÍSTICAS ---")
            print(f"🏆 Victorias: {victorias}")
            print(f"💀 Derrotas:  {derrotas}")
            input("\nPresiona ENTER para volver al menú...")
            continue

        # --- CONFIGURACIÓN DE PARTIDA ---
        print("\n🪚 SELECCIONA LA VERSIÓN")
        print("1. Clásica (🗿 📄 ✂️)")
        print("2. Extendida (🗿 📄 ✂️ 🦎 🖖)")
        
        try:
            version = int(input("👉 Elige versión (1 o 2): "))
        except ValueError:
            version = 1

        print("\n🪚  SELECCIONA EL MODO")
        print("1. Partida Rápida (Muerte súbita)")
        print("2. Mejor de 3 (El primero en llegar a 3)")
        
        try:
            modo = int(input("👉 Elige modo (1 o 2): "))
        except ValueError:
            modo = 1

        # Lógica del mejor de 3
        meta = 3 if modo == 2 else 1
        v_ronda = 0
        d_ronda = 0

        # Diccionario para convertir texto a número
        # Esto permite que el usuario escriba la palabra y el código entienda el número
        mapa_input = {
            "piedra": 1, "papel": 2, "tijera": 3, "lagarto": 4, "spock": 5
        }
        
        # Diccionario inverso para mostrar emojis según el número
        mapa_emojis = {
            1: "Piedra 🗿", 2: "Papel 📄", 3: "Tijera ✂️", 
            4: "Lagarto 🦎", 5: "Spock 🖖"
        }

        # =======================================================
        # RAMA 1: VERSIÓN EXTENDIDA
        # =======================================================
        if version == 2:
            print("\n🔥 ¡MODO EXTENDIDO INICIADO! 🔥")
            while v_ronda < meta and d_ronda < meta:
                print("\nOpciones: Piedra, Papel, Tijera, Lagarto, Spock")
                
                entrada = input("👉 Escribe tu jugada: ").lower().strip()
                
                # Validamos si lo que escribió existe en nuestro mapa
                if entrada not in mapa_input:
                    print("❌ Opción no válida. Revisa la ortografía.")
                    continue
                
                # Convertimos el texto a número
                jugador = mapa_input[entrada]

                pc = random.randint(1, 5)
                print(f"🤖 PC eligió: {mapa_emojis[pc]}")

                if jugador == pc:
                    print("😐 ¡Empate!")
                    continue

                # lógica Reglas del juego (Sheldon Cooper)
                gana = (
                    (jugador == 1 and pc in (3, 4)) or
                    (jugador == 2 and pc in (1, 5)) or
                    (jugador == 3 and pc in (2, 4)) or
                    (jugador == 4 and pc in (2, 5)) or
                    (jugador == 5 and pc in (1, 3))
                )

                if gana:
                    print("🎉 ¡Ganaste la ronda!")
                    v_ronda += 1
                else:
                    print("💀 Perdiste la ronda")
                    d_ronda += 1
                
                if modo == 2:
                    print(f"   Marcador: Tú {v_ronda} - {d_ronda} PC")

        # =======================================================
        # RAMA 2: VERSIÓN CLÁSICA
        # =======================================================
        else:
            print("\n🕹️ ¡MODO CLÁSICO INICIADO! 🕹️")
            while v_ronda < meta and d_ronda < meta:
                print("\nOpciones: Piedra, Papel, Tijera")
                
                entrada = input("👉 Escribe tu jugada: ").lower().strip()
                
                # Validamos solo las 3 opciones clásicas
                if entrada not in ["piedra", "papel", "tijera"]:
                    print("❌ Opción no válida en modo clásico.")
                    continue
                
                jugador = mapa_input[entrada] # Convertimos a número

                pc = random.randint(1, 3)
                print(f"🤖 PC eligió: {mapa_emojis[pc]}")

                if jugador == pc:
                    print("😐 ¡Empate!")
                    continue

                # lógica original clásica - Reglas
                gana = (
                    (jugador == 1 and pc == 3) or
                    (jugador == 2 and pc == 1) or
                    (jugador == 3 and pc == 2)
                )

                if gana:
                    print("🎉 ¡Ganaste la ronda!")
                    v_ronda += 1
                else:
                    print("💀 Perdiste la ronda")
                    d_ronda += 1
                
                if modo == 2:
                    print(f"   Marcador: Tú {v_ronda} - {d_ronda} PC")

        # Fin de partida
        if v_ronda > d_ronda:
            print("\n🏆 ¡FELICIDADES! GANASTE LA PARTIDA 🏆")
            victorias += 1
        else:
            print("\n💀 FIN DEL JUEGO. LA PC GANA 💀")
            derrotas += 1

if __name__ == "__main__":
    main()
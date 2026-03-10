import random
class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        reglas = {
            "piedra": "tijera",
            "tijera": "papel",
            "papel": "piedra"
        }

        if jugador1 == jugador2:
            return "empate"
        elif reglas[jugador1] == jugador2:
            return "jugador1"
        else:
            return "jugador2"

    def adivinar_numero_pista(self, numero_secreto, intento):
        if numero_secreto == intento:
            return "correcto"
        elif numero_secreto > intento:
            return "muy bajo"
        else:
            return "muy alto"
    
    def ta_te_ti_ganador(self, tablero):
                
        for i in range(len(tablero)):
            if tablero[i,0]==tablero[i,1]==tablero[i,2] and tablero[i,0] != " ":
                return tablero[i,0]
            if tablero[0,i]==tablero[1,i]==tablero[2,i] and tablero[0,i] != " ":
                return tablero[0,i]
        
        if tablero[0,0]==tablero[1,1]==tablero[2,2] and tablero[0,0] != " ":
            return tablero[0,0]
        
        if tablero[0,2]==tablero[1,1]==tablero[2,0] and tablero[0,2] != " ":
            return tablero[0,2]

        for j in range(len(tablero)):
            for k in range(len(tablero)):
                if tablero[j,k] == " ":
                    return "continua"

        return "empate"
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        combinacion = [random.choice(colores_disponibles) for _ in range(longitud)]
        return combinacion
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.
        sssss
        Args:
            desde_fila (int): Fila inicial (0-7)
            desde_col (int): Columna inicial (0-7)
            hasta_fila (int): Fila destino (0-7)
            hasta_col (int): Columna destino (0-7)
            tablero (list): Matriz 8x8 representando el tablero
            sssss
        Returns:
            bool: True si el movimiento es válido, False si no
            
        Reglas:
            - La torre se mueve horizontal o verticalmente
            - No puede saltar sobre otras piezas
        """
        pass
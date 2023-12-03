from enum import Enum

class GameState(Enum):
    RUNNING = 1
    WON = 2
    LOST = 3
    
    def print(self):
        match self:
            case GameState.RUNNING:
                print("Juego en curso")
            case GameState.WON:
                print("Felicitaciones!! Ganaste la partida")
            case GameState.LOST:
                print("Perdiste, no te quedan intentos")
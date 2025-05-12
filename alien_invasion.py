import sys
import pygame

class AlienInvasion:
    """Clase general para gestionar los recursos y el comportamiento del juego."""

    def __init__(self):
        """Inicializa el juego y crea resursos."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1100, 700))
        pygame.display.set_caption("Alien invasion")

    def run_game (self):
        """Inicia el bucle principal para el juego."""
        while True:
            # Busca eventos de teclado y raton.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Hace visible la ultima pantalla dibujada.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # hace una instancia del juego y lo ejecuta.
    ai = AlienInvasion()
    ai.run_game()

        
import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Clase general para gestionar los recursos y el comportamiento del juego."""

    def __init__(self):
        """Inicializa el juego y crea resursos."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien invasion")

        self.ship = Ship(self)

        # Configura el color de fondo.
        self.bg_color = (230, 230, 230)

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
            # Redibujar la pantalla en cada paso por el bucle
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            
if __name__ == '__main__':
    # hace una instancia del juego y lo ejecuta.
    ai = AlienInvasion()
    ai.run_game()

        
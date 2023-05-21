import sys

import  pygame

class Ship:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500,500))
        self.bg_color = (230,230,230)

        pygame.display.set_caption("Alien Invasion")

    def blitme(self):
        while True:
            for event in  pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.image = pygame.image.load('images/ship.bmp')

            self.screen.blit(self.image,(225,450))
            pygame.display.flip()

ss = Ship()
ss.blitme()
import pygame


def main():
    pygame.init()
    screen = pygame.
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()

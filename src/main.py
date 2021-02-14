import pygame
import pygame.display
import pygame.time
# import pygame.


class World:
    def __init__(self) -> None:
        self.resources = []

    def insert(self, resource):
        self.resources.insert(resource)


class Component:
    def __init__(self) -> None:
        pass


class Entity:
    def __init__(self) -> None:
        self.id = None
        self.components = []

    def register(self, component: Component):
        self.components.insert(Component)


class System:
    def __init__(self) -> None:


def main():
    pygame.init()
    screen = pygame.display.set_mode((960, 604))
    pygame.display.set_caption("Nekromass")
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()

import pygame

pygame.init()

width, hight = 800, 600
Fps = 120

pygame.display.set_caption("Legand of Ninja Frog")
window = pygame.display.set_mode((width, hight))

def main(window):
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(Fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)
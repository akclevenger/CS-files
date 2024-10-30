import pygame

def main():
    pygame.init()

    
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Discoball")

   
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill("papayawhip")

    
    discoball = pygame.image.load("Disco-ball.png")
    discoball = discoball.convert_alpha()
    discoball = pygame.transform.scale(discoball, (100, 100))

   
    discoball_x = 0
    discoball_y = 200

    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:

        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False


        discoball_y += 5
        if discoball_y > screen.get_height():
            discoball_y = 0

        screen.blit(background, (0, 0))
        screen.blit(discoball, (discoball_x, discoball_y))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
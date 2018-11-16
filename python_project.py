import pygame
Screen_height = 640
Screen_width = 800
Display = (Screen_width, Screen_height)
Background_color = "004400"
def play_window():
    pygame.init()
    screen = pygame.display.set_mode(Display)
    pygame.display.set_caption('Космический бой')
    space_surf = pygame.image.load('space.jpg')
    space_rect = space_surf.get_rect(bottomright=(800, 640))
    screen.blit(space_surf, space_rect)

    pygame.display.update()

    while 1:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
 
        pygame.time.delay(20)
    
    
def main():
    play_window()


main()

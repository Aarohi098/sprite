import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Smart Traffic Signal Simulator")

WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)

BOUNDARY_HIT_EVENT = pygame.USEREVENT + 1
LIGHT_CHANGE_EVENT = pygame.USEREVENT + 2


class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 60
        self.height = 30
        self.image = pygame.Surface((self.width, self.height))
        
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.image.fill(self.color)
        
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = SCREEN_HEIGHT // 2
        
        self.base_velocity = 6

    def change_color(self):
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.image.fill(self.color)

    def update(self, light_status):
        if light_status == GREEN:
            current_velocity = self.base_velocity
        elif light_status == ORANGE:
            current_velocity = self.base_velocity // 2
        else:
            current_velocity = 0

        self.rect.x += current_velocity
        
        if self.rect.left >= SCREEN_WIDTH:
            pygame.event.post(pygame.event.Event(BOUNDARY_HIT_EVENT))
            self.rect.right = 0


car = Car()
car_group = pygame.sprite.Group()
car_group.add(car)

traffic_light_color = GREEN

pygame.time.set_timer(LIGHT_CHANGE_EVENT, 2000)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == BOUNDARY_HIT_EVENT:
            car.change_color()

        elif event.type == LIGHT_CHANGE_EVENT:
            if traffic_light_color == GREEN:
                traffic_light_color = ORANGE
            elif traffic_light_color == ORANGE:
                traffic_light_color = RED
            else:
                traffic_light_color = GREEN

    car_group.update(traffic_light_color)

    screen.fill(WHITE)
    
    pygame.draw.rect(screen, GRAY, (0, (SCREEN_HEIGHT // 2) - 20, SCREEN_WIDTH, 70))
    pygame.draw.circle(screen, traffic_light_color, (SCREEN_WIDTH // 2, 100), 30)
    
    car_group.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


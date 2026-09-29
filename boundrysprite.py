import pygame
import random

#instalise pygame
pygame.init()

#custom event IDS for colour change events
SPRITE_COLOUR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOUR_CHANGE_EVENT = pygame.USEREVENT + 2

#define basic colours using pygame.colour
#background colours
BLUE = pygame.Colour('blue')
LIGHT_BLUE = pygame.Colour('lightblue')
DARK_BLUE = pygame.Colour('darkblue')

#sprite colours
YELLOW = pygame.Colour('yellow')
MAGENTA = pygame.Colour('magenta')
ORANGE = pygame.Colour('orange')
WHITE = pygame.Colour('white')

#Sprite class representing the moving object
class Sprite(pygame.sprite.Sprite):
    
    #constructor method
    def __init__(self, colour, height, width):
        
        #class to the parent class sprite constructor
        super().__init__()
        
        #create sprites surface with dimensions and colour
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        
        #get the sprites rect using its position and size
        self.rect = self.image.get_rect()
        
        #set initial velocity with random direction
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
        
#method to update the sprite's position
def update(self):
    #move sprite by its velocity
    self.rect.move_ip(self.velocity)
    
    #flag to track if the sprite hits the boundary
    boundary_hit = False
    
    #check for collision with left or right boundaries and reverse direction
    if self.rect.left <= 0  or self.rect.right >= 500:
        self.velocity[0] = -self.velocity[1]
        boundary_hit = True
        
    #if boundary was hit, post event to change colours
    if boundary_hit:
        pygame.event.post(pygame.event.Event(SPRITE.COLOUR.CHANGE.EVENT))
        pygame.event.post(pygame.event.Event(BACKGROUND.COLOUR.CHANGE.EVENT))
    
#method to change sprite's colour
def change_colour(self):
    self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))
    
#method to change backgroundcolour
def change_background_colour():
    global bg_colour
    bg_colour = random.choice([BLUE, LIGHT_BLUE, DARK_BLUE])
    
# create a group to hold the sprite
all_sprites_list = pygame.sprite.Group()

#instantiate the sprite
sp1 = Sprite(WHITE, 20, 30)

#randomly postion the sprite
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)

#add sprite to the group
all_sprites_list.add(sp1)

#create the game window
screen = pygame.display.set_mode((500, 400))

#set window title
screen = pygame.display.caption("Boundary Sprite")

#set initial bg colour
bg_clour = BLUE

#apply bg colour
screen.fill(bg.colour)

#game loop control flag
exit = False

#create clock object to control frame rate
clock = pygame.time.Clock()

# main game loop
while not exit:
    
    #event handling loop
    for event in pygame.event.get():
        #if the window's close button is clicked, exit the game
        if event.type == pygame.QUIT:
            exit = True
            
        elif event.type == SPRITE_COLOUR_CHANGE_EVENT:
            sp1.change_colour()
            
        elif event.type == BACKGROUND_COLOUR_CHANGE_EVENT:
            change_background_colour()
            
all_sprites_list.update()

screen.fill(bg.colour)

all_sprites_list
    
    
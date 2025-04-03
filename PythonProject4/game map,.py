import pygame
import random


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI-Based Farm Game")


GREEN = (34, 177, 76)
BROWN = (139, 69, 19)
WHITE = (255, 255, 255)


clock = pygame.time.Clock()
FPS = 30


player_img = pygame.image.load("C:/Users/fkoc8/PycharmProjects/PythonProject4/png/player.png")
player_img = pygame.transform.scale(player_img, (50, 50))

player_water_img = pygame.image.load("C:/Users/fkoc8/PycharmProjects/PythonProject4/png/w.png")
player_water_img = pygame.transform.scale(player_water_img, (50, 50))


plant_img = pygame.image.load("C:/Users/fkoc8/PycharmProjects/PythonProject4/png/plant.png")
plant_img = pygame.transform.scale(plant_img, (30, 30))


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.has_water = False

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed


        if keys[pygame.K_SPACE]:
            self.has_water = True

    def draw(self, screen):
        if self.has_water:
            screen.blit(player_water_img, (self.x, self.y))
        else:
            screen.blit(player_img, (self.x, self.y))



class Plant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 30
        self.grow_time = random.randint(100, 200)
        self.timer = 0

    def grow(self, fast=False):
        if fast:
            self.timer += 550
        else:
            self.timer += 1

        if self.timer > self.grow_time and self.size < 60:
            self.size += 5
            self.timer = 0

    def draw(self, screen):

        scaled_plant_img = pygame.transform.scale(plant_img, (self.size, self.size))
        screen.blit(scaled_plant_img, (self.x, self.y))



player = Player(WIDTH // 2, HEIGHT // 2)


plants = [Plant(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)) for _ in range(5)]


running = True
while running:
    screen.fill(BROWN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)


    for plant in plants:
        if player.has_water and abs(player.x - plant.x) < 40 and abs(player.y - plant.y) < 40:
            plant.grow(fast=True)
            player.has_water = False
        else:
            plant.grow()

        plant.draw(screen)

    player.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

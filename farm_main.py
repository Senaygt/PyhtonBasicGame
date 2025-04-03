import pygame

pygame.init()
window = pygame.display.set_mode((800, 500))

game = True
milk = 0
egg2 = 0
ses = pygame.mixer.Sound('henses.wav')
ses.set_volume(0.3)
font = pygame.font.SysFont("consolas", 20)
yazi = font.render(f"Milk:+{milk}", True, (0, 0, 0))
yazi2 = font.render(f"Egg:+{egg2}", True, (0, 0, 0))

barn = pygame.image.load('barn.png')
barn_x = 150
barn_y = 310
barn_rect = pygame.Rect(barn_x, barn_y, 64, 64)

tr = pygame.image.load('transport.png')
tr_x = 300
tr_y = 310

hen = pygame.image.load('hen.png')
hen_x = 750
hen_y = 430
hen_hız = 0.1
yon = 1

farmer = pygame.image.load('farmer (1).png')
farmer_x = 300
farmer_y = 400
hiz = 1

egg = pygame.image.load("farmer.png")

stand = pygame.image.load('stand.png')

cow = pygame.image.load('cow.png')
cow_x = 100
cow_y = 360
cow_hiz = 0.2
cow_yon = -1

land = pygame.image.load('land.png')
land_k = [(5, 435), (70, 435), (135, 435), (200, 435), (265, 435), (330, 435), (395, 435), (460, 435), (525, 435),
          (590, 435), (655, 435), (720, 435), (5, 390), (70, 390), (135, 390), (200, 390), (265, 390), (330, 390),
          (395, 390), (460, 390), (525, 390), (590, 390), (655, 390), (720, 390)]

back_sound = pygame.mixer.music.load('farm.wav')
pygame.mixer.music.play(-1)

while game:
    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            game = False
    for x, y in land_k:
        window.blit(land, (x, y))

    window.blit(barn, (barn_x, barn_y))
    window.blit(tr, (tr_x, tr_y))
    window.blit(cow, (cow_x, cow_y))
    window.blit(farmer, (farmer_x, farmer_y))
    window.blit(hen, (hen_x, hen_y))
    window.blit(stand, (700, 350))
    window.blit(yazi, (50, 0))
    window.blit(yazi2, (50, 20))

    tuslar = pygame.key.get_pressed()
    if tuslar[pygame.K_LEFT]:
        farmer_x -= hiz
    if tuslar[pygame.K_RIGHT]:
        farmer_x += hiz
    if tuslar[pygame.K_UP]:
        farmer_y -= hiz
    if tuslar[pygame.K_DOWN]:
        farmer_y += hiz

    hen_x += hen_hız * yon
    if (hen_x > 790):
        yon = -1
    elif (hen_x < 10):
        yon = 1

    farmer_rect = pygame.Rect(farmer_x, farmer_y, 32, 32)
    hen_rect = pygame.Rect(hen_x, hen_y, 32, 32)
    cow_rect = pygame.Rect(cow_x, cow_y, 32, 32)

    if farmer_rect.colliderect(hen_rect) & tuslar[pygame.K_SPACE] and not space_pressed:
        egg2 += 1
        space_pressed = True
        yazi2 = font.render(f"Egg:+{egg2}", True, (0, 0, 0))
        ses.play()

    if farmer_rect.colliderect(hen_rect) & tuslar[pygame.K_SPACE]:
        window.blit(egg, (hen_x + 50, hen_y - 100))
    if farmer_rect.colliderect(cow_rect) & tuslar[pygame.K_SPACE] and not space_pressed:
        milk += 1
        space_pressed = True
        yazi = font.render(f"Milk:+{milk}", True, (0, 0, 0))
    if farmer_rect.colliderect(cow_rect) & tuslar[pygame.K_SPACE]:
        window.blit(pygame.image.load('milk-tank.png'), (cow_x + 50, cow_y - 50))

    if not tuslar[pygame.K_SPACE]:
        space_pressed = False

    if farmer_rect.colliderect(barn_rect) & tuslar[pygame.K_SPACE]:
        window.blit(pygame.image.load('peasant.png'), (barn_x, barn_y - 50))

    cow_x += cow_hiz * cow_yon
    if (cow_x > 790):
        cow_yon = -1
    elif (cow_x < 10):
        cow_yon = 1
    pygame.display.update()
    window.fill((50, 180, 50))

pygame.quit()

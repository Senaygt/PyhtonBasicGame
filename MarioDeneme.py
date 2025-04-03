import pygame
pygame.init()
pencere=pygame.display.set_mode((790,500))
game=True


ses=pygame.mixer.Sound('mario2.flac')
ses.set_volume(0.3)
wall=pygame.image.load("wall.png")
wall_k=[(5,435),(70,435),(135,435),(200,435),(265,435),(330,435),(395,435),(460,435),(525,435),(590,435),(655,435),(720,435)]

mark=pygame.image.load("mark.png")
mark_x=350;
mark_y=270;

mantar=pygame.image.load("mushroom.png")
mantar_x=700
mantar_y=370
mantar_hiz=0.2
mantar_yon=-1

mario=pygame.image.load("person.png")
mario_x=0
mario_y=370
hiz=0.8
font=pygame.font.SysFont("consolas",64)
yazi=font.render("Hello Game",True,(100,200,150))
yazi_k=yazi.get_rect()
yazi_k.topleft=(200,170)

yercekimi = 1
ziplama_gucu = -15
karakter_hizi_y = 0
havada = False


pygame.mixer.music.load("mario.mp3")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)
while game:
    for etkinlik in pygame.event.get():
        if etkinlik.type==pygame.QUIT:
            game=False
    for x, y in wall_k:
        pencere.blit(wall, (x, y))
    pencere.blit(mario,(mario_x,mario_y))
    pencere.blit(mantar,(mantar_x,mantar_y))
    pencere.blit(mark,(mark_x,mark_y))
    tuslar = pygame.key.get_pressed()
    if tuslar[pygame.K_LEFT]:
        mario_x -= hiz  # Sola git
    if tuslar[pygame.K_RIGHT]:
        mario_x += hiz  # Sağa git
    if tuslar[pygame.K_SPACE] and not havada:
        karakter_hizi_y = ziplama_gucu
        havada = True


    karakter_hizi_y += yercekimi
    mario_y += karakter_hizi_y
    if mario_x<=0:
        mario_x=0
    elif mario_x>=780:
        mario_x=760
    if mario_y >= 370:
        mario_y = 370
        havada = False
    mario_rect=pygame.Rect((mario_x,mario_y,64,64));
    mark_rect=pygame.Rect((mark_x,mark_y,64,64))
    mantar_ract=pygame.Rect(mantar_x,mantar_y,64,64)

    if mario_rect.colliderect(mark_rect):
        pencere.blit(yazi, yazi_k)



    mantar_x += mantar_hiz * mantar_yon
    if mantar_x>=790:
        mantar_yon=-1
    elif mantar_x<=50:
        mantar_yon=1

    if mario_rect.colliderect(mantar_ract):
        print('You got caught')
        ses.play()

    pygame.display.update()
    pencere.fill((50, 180, 50))



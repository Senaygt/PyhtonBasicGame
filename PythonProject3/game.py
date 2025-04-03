import pygame
import random

# Pygame başlat
pygame.init()

# Ekran boyutları
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Uçan Kuş Oyunu")

# Renkler
WHITE = (255, 255, 255)

# Arka plan yükleme
background = pygame.image.load("C:/Users/fkoc8/PycharmProjects/PythonProject3/png/back.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Karakter görselleri yükleme
bird_img = pygame.image.load("C:/Users/fkoc8/PycharmProjects/PythonProject3/png/bird.png")
bird_img = pygame.transform.scale(bird_img, (80, 80))

caterpillar_img = pygame.image.load("C:/Users/fkoc8/PycharmProjects/PythonProject3/png/tırtıl.png")
caterpillar_img = pygame.transform.scale(caterpillar_img, (40, 40))

cat_img = pygame.image.load("C:/Users/fkoc8/PycharmProjects/PythonProject3/png/cat.png")
cat_img = pygame.transform.scale(cat_img, (120, 120))

# Oyuncu ayarları
player_x = 100
player_y = HEIGHT // 2
player_speed = 5

tirtil_x = random.randint(200, WIDTH - 80)
tirtil_y = random.randint(80, HEIGHT - 80)

kedi_x = random.randint(200, WIDTH - 80)
kedi_y = random.randint(80, HEIGHT - 80)

score = 0
font = pygame.font.Font(None, 36)

# Oyun döngüsü
running = True
while running:
    pygame.time.delay(30)

    # Olayları kontrol et
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tuşları kontrol et
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - 80:
        player_y += player_speed
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 80:
        player_x += player_speed

    # Çarpışma kontrolü
    player_rect = pygame.Rect(player_x, player_y, 80, 80)
    tirtil_rect = pygame.Rect(tirtil_x, tirtil_y, 40, 40)
    kedi_rect = pygame.Rect(kedi_x, kedi_y, 100, 100)

    if player_rect.colliderect(tirtil_rect):
        score += 1
        tirtil_x = random.randint(200, WIDTH - 80)
        tirtil_y = random.randint(80, HEIGHT - 80)

    if player_rect.colliderect(kedi_rect):
        print("Oyun Bitti! Skor:", score)
        running = False

    # Ekranı güncelle
    screen.blit(background, (0, 0))
    screen.blit(bird_img, (player_x, player_y))
    screen.blit(caterpillar_img, (tirtil_x, tirtil_y))
    screen.blit(cat_img, (kedi_x, kedi_y))

    score_text = font.render(f"Skor: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()



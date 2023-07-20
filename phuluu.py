import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Thiết lập kích thước cửa sổ game và tên game
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Adventure Game')

# Tải hình ảnh và chuyển đổi sang định dạng Pygame
player_image = pygame.image.load('player.png')
player_image = pygame.transform.scale(player_image, (50, 50))
coin_image = pygame.image.load('coin.png')
coin_image = pygame.transform.scale(coin_image, (30, 30))
obstacle_image = pygame.image.load('obstacle.png')
obstacle_image = pygame.transform.scale(obstacle_image, (50, 50))

# Định nghĩa các biến cho game
player_x = 50
player_y = window_height // 2
player_speed = 5
player_rect = player_image.get_rect(topleft=(player_x, player_y))

coin_list = []
for i in range(5):
    coin_x = random.randint(100, window_width - 100)
    coin_y = random.randint(100, window_height - 100)
    coin_rect = coin_image.get_rect(topleft=(coin_x, coin_y))
    coin_list.append(coin_rect)

obstacle_list = []
for i in range(5):
    obstacle_x = random.randint(100, window_width - 100)
    obstacle_y = random.randint(100, window_height - 100)
    obstacle_rect = obstacle_image.get_rect(topleft=(obstacle_x, obstacle_y))
    obstacle_list.append(obstacle_rect)

score = 0
font = pygame.font.SysFont(None, 40)

# Vòng lặp chính của game
running = True
while running:
    # Xử lý các sự kiện trong game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Xử lý phím di chuyển của nhân vật
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < window_height - player_rect.height:
        player_y += player_speed
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < window_width - player_rect.width:
        player_x += player_speed

    # Cập nhật vị trí của nhân vật
    player_rect.topleft = (player_x, player_y)

    # Kiểm tra va chạm giữa nhân vật và tiền xu
    for coin_rect in coin_list:
        if player_rect.colliderect(coin_rect):
            coin_list.remove(coin_rect)
            score += 10

    # Kiểm tra va chạm giữa nhân vật và chướng ngại vật
    for obstacle_rect in obstacle_list:
        if player_rect.colliderect(obstacle_rect):
            running = False

    # Vẽ các đối tượng lên màn hình game
    window.fill((255, 255, 255))
    window.blit(player_image, player_rect)
    for coin_rect in coin_list:
        window.blit(coin_image, coin_rect)
    for obstacle_rect in obstacle_list:
        window.blit(obstacle_image, obstacle_rect)

    # Hiển thị điểm số lên màn hình game
    score_text = font.render('Score: ' + str(score), True, (0, 0, 0))
    window.blit(score_text, (10, 10))

    # Cập nhật màn hình game
    pygame.display.update()

# Kết thúc Pygame
pygame.quit()
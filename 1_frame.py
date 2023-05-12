import pygame

# 초기화
pygame.init()
screen_width = 1200 # 가로 크기
screen_height = 780 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 배경이미지 불러오기
background = pygame.image.load("game_background.png")

# 새로운 화면을 위한 Surface 객체 생성
sub_screen_width = 850
sub_screen_height = 530
sub_screen = pygame.Surface((sub_screen_width, sub_screen_height))

# 새로운 화면에 그리기
sub_screen.fill((255, 255, 255))  # 예시로 흰색 배경 채우기
pygame.draw.circle(sub_screen, (255, 0, 0), (sub_screen_width // 2, sub_screen_height // 2), 50)  # 예시로 빨간 원 그리기

# 게임 루프
running = True # 게임이 실행중인가?
while running:
    # 이벤트 루프
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트인가?
            running = False # 게임이 더 이상 실행중이 아님
    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(sub_screen, (30, 30))  # 새로운 화면을 (30, 30) 위치에 그리기
    pygame.display.update() # while문이 계속 반복하면서 게임 화면을 계속 업데이트

# 게임 종료
pygame.quit()

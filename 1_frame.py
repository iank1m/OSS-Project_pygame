import pygame

# 초기화
pygame.init()
screen_width = 1200 # 가로 크기
screen_height = 780 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 배경이미지 불러오기
background = pygame.image.load("이미지 경로 복사")

# 게임 루프
running = True # 게임이 실행중인가?
while running:
    # 이벤트 루프
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트인가?
            running = False # 게임이 더 이상 실행중이 아님
    screen.blit(background, (0,0)) # background 그리기
    pygame.display.update() # while부분 계속 돌면서 게임 화면 계속 구현 

# 게임 종료
pygame.quit()

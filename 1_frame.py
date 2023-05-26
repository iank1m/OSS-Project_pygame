import pygame

# 초기화
pygame.init()
screen_width = 1200  # 가로 크기
screen_height = 780  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 시작 화면 띄우기
start_background = pygame.image.load("start_background_찐최종본.png")
game_background = pygame.image.load("game_background.png")

# 새로운 화면을 위한 Surface 객체 생성
sub_screen_width = 865
sub_screen_height = 520
sub_screen = pygame.Surface((sub_screen_width, sub_screen_height))

# 새로운 화면에 그리기
sub_screen.fill((0, 0, 0))  # 예시로 흰색 배경 채우기

# 페이드 효과에 사용할 Surface 객체 생성
fade_surface = pygame.Surface((screen_width, screen_height))
fade_surface.fill((0, 0, 0))  # 검은색 배경으로 채우기

#게임 시작 대기 화면 2초간 고정
screen.blit(start_background, (0,0))
pygame.display.update()
pygame.time.wait(2000)  # 2초 대기


# 페이드 효과 변수
fade_alpha = 0
fade_speed = 5

# 게임 시작 대기 화면
while fade_alpha < 255:
    fade_alpha += fade_speed
    fade_surface.set_alpha(fade_alpha)
    screen.blit(start_background, (0, 0))
    screen.blit(fade_surface, (0, 0))
    pygame.display.update()

# 게임 화면으로 전환
while fade_alpha > 0:
    fade_alpha -= fade_speed
    fade_surface.set_alpha(fade_alpha)
    screen.blit(game_background, (0, 0))
    screen.blit(fade_surface, (0, 0))
    pygame.display.update()

# 게임 루프
running = True  # 게임이 실행중인가?
while running:
    # 이벤트 루프
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트인가?
            running = False  # 게임이 더 이상 실행중이 아님

    screen.blit(game_background, (0, 0))  # 배경 그리기
    screen.blit(sub_screen, (25, 40))  # 새로운 화면을 (30, 30) 위치에 그리기
    pygame.display.update()  # while문이 계속 반복하면서 게임 화면을 계속 업데이트

# 게임 종료
pygame.quit()

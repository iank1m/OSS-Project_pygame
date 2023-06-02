# 점수 화면에 기록
score = 0
stagescore = 0
stagestair = 1000
def draw_score():
    # score 기록
    font_01 = pygame.font.SysFont("FixedSsy", 70, True, False)
    text_score = font_01.render("Score: " + str(score), True, BLUE)
    text_score_rect = text_score.get_rect(center=(screen_width/2 - 160, screen_height/2 - 30))
    screen.blit(text_score, text_score_rect)
    # level 기록
    text_level = font_01.render(f"level: {curr_level}", True, BLUE)
    text_level_rect = text_level.get_rect(center=(screen_width/2 - 160, screen_height/2 - 80))
    screen.blit(text_level, text_level_rect)
    
# 점수 증가 시키기
def increase_score(level):
    global score, stagescore

    # LEVEL 별 증가율을 위한 stair 값 설정
    if level < 4:
        score += 10         # level 1, 2, 3의 경우 한블록 당 10점 
    else:
        score = score + level + 10      # level이 증가하면 할 수록 한 블록당 점수 높게 측정

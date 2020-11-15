import pygame
import time
import random


pygame.init()

SCREEN_WIDTH,SCREEN_HEIGHT = 600,800
SQUARE_LENGTH = 200

BOARD_WIDTH = BOARD_HEIGHT = 600
FPS = 30
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


pygame.display.set_caption("Tic Tac Toe")

board = [[None for _ in range(3)] for _ in range(3)]

def draw_board():


    for y in range(0,SCREEN_HEIGHT,SQUARE_LENGTH):
        pygame.draw.line(screen,(0,0,0),(0,y),(BOARD_WIDTH,y))


    for x in range(0,BOARD_WIDTH,SQUARE_LENGTH):
        pygame.draw.line(screen,(0,0,0),(x,0),(x,BOARD_HEIGHT))

    

    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(screen,(0,0,0),(col * SQUARE_LENGTH,row * SQUARE_LENGTH),(col * SQUARE_LENGTH + SQUARE_LENGTH,row * SQUARE_LENGTH + SQUARE_LENGTH))
                pygame.draw.line(screen,(0,0,0),(col * SQUARE_LENGTH + SQUARE_LENGTH,row * SQUARE_LENGTH),(col * SQUARE_LENGTH,row * SQUARE_LENGTH + SQUARE_LENGTH))
            elif board[row][col] == 'O':
                pygame.draw.circle(screen,(0,0,0),(col * SQUARE_LENGTH + SQUARE_LENGTH//2,row * SQUARE_LENGTH + SQUARE_LENGTH//2),SQUARE_LENGTH//2,1)



def check_game_over():
    

    winner = None
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != None:
        winner = turn
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != None:
        winner = turn
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != None:
        winner = turn
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != None:
        winner = turn
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != None:
        winner = turn
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != None:
        winner = turn
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != None:
        winner = turn
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != None:
        winner = turn


    return winner










done = False



turn = random.choice(('X','O'))

font = pygame.font.SysFont("comicsansms",42)

turn_text = font.render(f"{turn}'s TURN",True,(0,0,0))

clock = pygame.time.Clock()



game_over = False
turns = 0
waiting = False
enter_text = font.render("Press ENTER to play again!",True,(0,0,0))
while not done:
    
    if waiting:
        current_time = time.time()
        if current_time - start_time >= 1:
            waiting = False
            turn_text = font.render(f"{turn}'s TURN",True,(0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done= True
        elif not game_over and not waiting and event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()

            if 0 <= x <= BOARD_WIDTH and 0 <= y <= BOARD_HEIGHT:

                row,col = y // SQUARE_LENGTH, x// SQUARE_LENGTH

                if board[row][col] == None:
                    turns += 1
                    board[row][col] = turn
                    
                    winner = check_game_over()

                    if winner:
                        game_over = True
                        turn_text = font.render(f"{winner} WINS!",True,(0,0,0))
                    else:
                        
                        if turns == 9:
                            turn_text = font.render(f"DRAW!",True,(0,0,0))
                            game_over = True
                        else:
                            if turn == 'X':
                                turn = 'O'
                            else:
                                turn = 'X'
                            turn_text = font.render(f"{turn}'s TURN",True,(0,0,0))
                else:
                    turn_text = font.render("INVALID MOVE!",True,(0,0,0))
                    waiting = True
                    start_time = time.time()

        elif game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                board = [[None for _ in range(3)] for _ in range(3)]
                turn = random.choice(('X','O'))
                turn_text = font.render(f"{turn}'s TURN",True,(0,0,0))
                game_over = False
                turns = 0




    screen.fill((255,255,255))
    draw_board()
    screen.blit(turn_text,(SCREEN_WIDTH // 2 - turn_text.get_width()//2,BOARD_HEIGHT + ((SCREEN_HEIGHT - BOARD_HEIGHT)//2 - turn_text.get_height()//2)))
    if game_over:
        screen.blit(enter_text,(SCREEN_WIDTH//2 - enter_text.get_width()//2,BOARD_HEIGHT + ((SCREEN_HEIGHT - BOARD_HEIGHT)//2 + turn_text.get_height()//2 + 10)))

    pygame.display.update()
    clock.tick(FPS)












from random import random, choice
import pygame
pygame.init()


def alive(b, x, y):
    m = len(b)
    n = len(b[0])
    # print(x,y,end=" ")
    if x >= 0 and x < m and y >= 0 and y < n:
        a = b[x][y]
        if a == 10 or a == 1:
            # print(1)
            return 1
        else:
            # print(0)
            return 0
    else:
        # print(0)
        return 0


def checkNeighbors(board, x, y):
    l = 0
    l += alive(board, x-1, y-1)
    l += alive(board, x-1, y)
    l += alive(board, x-1, y+1)
    l += alive(board, x+1, y-1)
    l += alive(board, x+1, y)
    l += alive(board, x+1, y+1)
    l += alive(board, x, y-1)
    l += alive(board, x, y+1)
    return l


def gameOfLife(board):
    if len(board) == 0 or len(board[0]) == 0:
        return
    m = len(board)
    n = len(board[0])
    for i in range(m):
        for j in range(n):
            l = checkNeighbors(board, i, j)
            if board[i][j] == 1:
                if l < 2:
                    board[i][j] = 10
                elif l > 3:
                    board[i][j] = 10
            else:
                if l == 3:
                    board[i][j] = 100
    for i in range(m):
        for j in range(n):
            if board[i][j] == 100 or board[i][j] == 1:
                board[i][j] = 1
            else:
                board[i][j] = 0
    return board


def randommatrix(m, n):
    a = [[choice([1, 0]) for i in range(n)] for i in range(m)]
    return a

def print_pixel(x, y, color):
    pygame.draw.rect(gameDisplay, color, [
                     x*pix_size, y*pix_size, pix_size, pix_size])


def game_loop():
    c = 0
    on = True
    global prev
    global b
    while on:
        c += 1
        c %= 10
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False
            if (pygame.mouse.get_pressed()[0]):
                x, y = pygame.mouse.get_pos()
                x //= pix_size
                y //= pix_size
                b[x][y] = 1
        gameDisplay.fill(white)
        for i in range(m):
            for j in range(n):
                if b[i][j]:
                    # col = (int(random()*256), int(random()*256), int(random()*256))
                    if not prev[i][j]:
                        col = (0, 0, 0)
                    else:
                        col = (0, 0, 0)
                    print_pixel(i, j, col)
                else:
                    print_pixel(i, j, white)
        prev = [x[:] for x in b]
        if c == 9:
            gameOfLife(b)
        pygame.display.update()
        clock.tick(30)


black = (0, 0, 0)
white = (255, 255, 255)
width = 800
height = 800
pix_size = 10
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game of Life')
clock = pygame.time.Clock()

m = 900//pix_size
n = height//pix_size

b = randommatrix(m, n)
prev = [x[:] for x in b]

game_loop()
pygame.quit()

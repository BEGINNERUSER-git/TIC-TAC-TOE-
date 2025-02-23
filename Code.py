import pygame as py


py.init()


display = py.display.set_mode((300, 300))
py.display.set_caption("Tic Tac Toe!")
icon = py.image.load('tic-tac-toe.png')  
py.display.set_icon(icon)


cell_size = 100


board = [[' ' for _ in range(3)] for _ in range(3)]


player_X = True  


def draw_grid():
    for x in range(1, 3):
        py.draw.line(display, (0, 0, 0), (x * 100, 0), (x * 100, 300), 2)
    for y in range(1, 3):
        py.draw.line(display, (0, 0, 0), (0, y * 100), (300, y * 100), 2)


def each_cell(x, y):
    col = x // cell_size
    row = y // cell_size
    return col, row


def mark_cell(col, row, mark):
    font = py.font.Font(None, 90) 
    text = font.render(mark, True, (255, 0, 0))  
    x_pos = col * cell_size + cell_size // 2 - text.get_width() // 2
    y_pos = row * cell_size + cell_size // 2 - text.get_height() // 2
    display.blit(text, (x_pos, y_pos))  


def winner():
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]
    
   
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    
    return None  


def display_text(text, x, y, font_size=32):
    font = py.font.Font(None, font_size)
    rendered_text = font.render(text, True, (0, 0, 0))
    display.blit(rendered_text, (x, y))


running = True
while running:
    display.fill((200, 200, 202))  

    
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.MOUSEBUTTONDOWN:
            x, y = py.mouse.get_pos()  
            col, row = each_cell(x, y) 
            
            
            if board[row][col] == ' ':
                if player_X:
                    board[row][col] = 'X'
                    player_X = False
                else:
                    board[row][col] = 'O'
                    player_X = True

   
    draw_grid()

  
    for x in range(3):
        for y in range(3):
            if board[x][y] != ' ':
                mark_cell(y, x, board[x][y]) 

    
    winner_mark = winner()
    if winner_mark:
        display_text(f"{winner_mark} Wins!", 70, 120, 48)
        

    elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        display_text("It's a Tie!", 100, 120, 48)
        

    if not winner_mark:
        current_player = "X" if player_X else "O"
        display_text(f"{current_player}'s Turn", 130, 20, 16)

    py.display.update()


 

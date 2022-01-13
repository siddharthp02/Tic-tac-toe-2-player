# **Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.**




from IPython.display import clear_output

def display_board(board):
    clear_output()
    
    print(f'   |   |   \n {board[7]} | {board[8]} | {board[9]} \n   |   |   \n-----------\n   |   |   \n {board[4]} | {board[5]} | {board[6]} \n   |   |   \n-----------\n   |   |   \n {board[1]} | {board[2]} | {board[3]} \n   |   |   \n')







# **Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using *while* loops to continually ask until you get a correct answer.**


# coulve instead done  while maker!=x or o instead rather than checking true or fals condition
def player_input():
    
    valid_choice = False
    
    while not valid_choice:
       
        player1=input('Does player1 want to be X or O?')
        player1=player1.upper()
        if player1=='X':
            player2='O'
            valid_choice=True
        elif player1=='O':
            player2='X'
            valid_choice=True
        
        else:
            continue
    return ['#',player1,player2]#couldve used tuple instead


# **Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.**

def place_marker(board, marker, position):
    
    
    board[position]=marker
# **Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won. **

def win_check(board, mark):
    
    if board[1]==board[2]==board[3]==mark or board[4]==board[5]==board[6]==mark or board[7]==board[8]==board[9]==mark or board[1]==board[4]==board[7]==mark or board[2]==board[5]==board[8]==mark or board[3]==board[6]==board[9]==mark or board[3]==board[5]==board[7]==mark or board[1]==board[5]==board[9]==mark:
        return True
    else:
        return False


# **Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.**


import random

def choose_first():
    first_player=random.randint(1,2)
    print( f'Player{first_player} will go first.')
    return first_player



# **Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.**



def space_check(board, position):
    if board[position]==' ':
        return True
    else:
        return False
    
    







# **Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.**



def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            
            return False
       
    
    return True


# **Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.**


def player_choice(board):
    
    in_range=False
    free_pos=False
    
    while not in_range or not free_pos:#ccoulve done while not in range or not space_check(position)
        position=input('Choose your next position: (1-9)')
        if position.isdigit():
            position=int(position)
            if position in range(1,10):
                in_range=True
            
                if space_check(board,position)==True:
                    free_pos=True
            
        
                else:
                    print('Not a free position')
                    pass
        
            else: 
                print('Not in range.')
                continue
            
            
        else:
            print('Not a digit')
        
            
       
    return position
           





# **Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.**



def replay():
    while True:
        
        ans=input('Would you like to play again? Enter Yes or No: ')
        if ans=='Yes' or ans=='yes':
            return True
        elif ans=='No' or ans=='no':
            return False
        else:
            print('invalid answer')


# **Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!**



print('Welcome to Tic Tac Toe!')


while True:
    markers=player_input()
    
    board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    game_on=False
    
    while not game_on:
        
        game_start=input('Are you ready to play? Enter Yes or No: ')
    
        if game_start=='Yes' or game_start=='yes':
            game_on=True
        elif game_start=='No' or game_start=='no':
            break
        else:
            print('Invalid answer')
    if not game_on:
        break
      

    
    while game_on:
        display_board(board)
        current_player=choose_first()
        
        
        while not full_board_check(board):
            
        
            if current_player==1:
            
                position=player_choice(board)
                place_marker(board,markers[1],position)
                display_board(board)
                
                if win_check(board,markers[1])==True:
                    print('Congratulations! Player1 wins!')
                    game_on=False
                    break
                    
                else:
                    current_player=2
            
            elif current_player==2:
                
                position=player_choice(board)
                place_marker(board,markers[2],position)
                display_board(board)
                
                if win_check(board,markers[2])==True:
                    print('Congratulations! Player2 wins!')
                    game_on=False
                    break
                    
                else:
                    current_player=1
                    
        if game_on==True:
            print('Game was a draw!')
            game_on=False
    if replay():
        game_on=True
    else:
        print('Thank you for playing!')
        break
                
                
                
            
            
            
            
            
        
        
    
        
        
      


# ## Good Job!

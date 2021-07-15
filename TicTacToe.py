
def welcome_players():
    
    player1 = ''
    #player2 = ''

    player1_name, player2_name = '',''

    player_dict = {} 
    
    # shows welcome screen
    print("\nWelcome to Tic Tac Toe!\n")

    while len(player1_name) <= 0:

        player1_name = input("Player 1, what is your name?: \n")

        if len(player1_name) <= 0:

            print("Sorry, that is not a valid name")

    player_dict.update({player1_name : ' '})

    while len(player2_name) <= 0:

        player2_name = input("Player 2, what is your name?: \n")

        if len(player2_name) <= 0:

            print("Sorry, that is not a valid name")

    player_dict.update({player2_name : ' '})

    # sets player1 as X or O
    while player1 not in ['X', 'O']:

        # allow the players to choose whether they are X or O
        player1 = input("{}, would you like to be X or O?:\n".format(player1_name))
    
        # check the player has chosen the correct input
        if player1 not in ['X', 'O']:
            print("Sorry, that is not a valid choice\n")

    
    # set player2 as the opposite of player1's choice
    if player1 == 'X':
        
        player_dict[player1_name] = 'X'
        player_dict[player2_name] = 'O'
    
    elif player1 == 'O':
        
        player_dict[player1_name] = 'O'
        player_dict[player2_name] = 'X'

    # says player1 will go first
    print("{} will go first!\n".format(player1_name))

    #print(player_dict)

    # asks if the players are ready (yes or no)
    #print("Are you ready to play? (Yes or No)\n")

    return player_dict, player1_name, player2_name

def display_board(choice_list):

    # shows the latest update of the board

    # use list to represent the locations of the X's and O's

    # print out board 
    print("\n")
    print("       |       |       ")
    print("   {0}   |   {1}   |   {2}  ".format(choice_list[6], choice_list[7], choice_list[8]))
    print("       |       |       ")
    print("-----------------------")
    print("       |       |       ")
    print("   {3}   |   {4}   |  {5}  ".format(*choice_list))
    print("       |       |       ")
    print("-----------------------")
    print("       |       |       ")
    print("   {0}   |   {1}   |  {2}  ".format(*choice_list))
    print("       |       |       ")
    print("\n")
    
def choose_position(player_name, choice_list):
    
    player_position = 'Not a valid choice'
    within_range = False

    # check the player input is a valid choice
    while player_position.isdigit() == False or within_range == False:

        # ask for user input for their position choice (1-9 inc.)
        player_position = input("{}, please choose your position (1-9): \n".format(player_name))

        if player_position.isdigit() == False:
            
            print("Sorry, that choice is invalid. Please try again.\n")
        
        elif player_position.isdigit() == True:

            if int(player_position) in range(1,10) and choice_list[int(player_position)-1] == ' ':
                within_range = True
            
            else:
                within_range = False
                print("Sorry, that choice is invalid. Please try again.\n")
            

    return int(player_position)

def place_player_choice(choice_list, player_position, player_icon):

    choice_list[player_position - 1] = player_icon

    return choice_list

def check_win(choice_list, players, player1, player2):
    
    is_win = False
    winning_player = ''

    # check to see if their are 3 in a row 

    if choice_list[0] == players[player1] and choice_list[1] == players[player1] and choice_list[2] == players[player1]:
        is_win = True
        winning_player = player1

    elif choice_list[3] == players[player1] and choice_list[4] == players[player1] and choice_list[5] == players[player1]:
        is_win = True
        winning_player = player1

    elif choice_list[6] == players[player1] and choice_list[7] == players[player1] and choice_list[8] == players[player1]:
        is_win = True
        winning_player = player1

    elif choice_list[0] == players[player1] and choice_list[3] == players[player1] and choice_list[6] == players[player1]:
        is_win = True
        winning_player = player1

    elif choice_list[1] == players[player1] and choice_list[4] == players[player1] and choice_list[7] == players[player1]:
        is_win = True
        winning_player = player1

    elif choice_list[2] == players[player1] and choice_list[5] == players[player1] and choice_list[8] == players[player1]:
        is_win = True
        winning_player = player1
        
    elif choice_list[6] == players[player1] and choice_list[4] == players[player1] and choice_list[2] == players[player1]:
        is_win = True
        winning_player = player1
      
    elif choice_list[8] == players[player1] and choice_list[4] == players[player1] and choice_list[0] == players[player1]:
        is_win = True
        winning_player = player1



    if choice_list[0] == players[player2] and choice_list[1] == players[player2] and choice_list[2] == players[player2]:
        is_win = True
        winning_player = player2

    elif choice_list[3] == players[player2] and choice_list[4] == players[player2] and choice_list[5] == players[player2]:
        is_win = True
        winning_player = player2

    elif choice_list[6] == players[player2] and choice_list[7] == players[player2] and choice_list[8] == players[player2]:
        is_win = True
        winning_player = player2

    elif choice_list[0] == players[player2] and choice_list[3] == players[player2] and choice_list[6] == players[player2]:
        is_win = True
        winning_player = player2

    elif choice_list[1] == players[player2] and choice_list[4] == players[player2] and choice_list[7] == players[player2]:
        is_win = True
        winning_player = player2

    elif choice_list[2] == players[player2] and choice_list[5] == players[player2] and choice_list[8] == players[player2]:
        is_win = True
        winning_player = player2
        
    elif choice_list[6] == players[player2] and choice_list[4] == players[player2] and choice_list[2] == players[player2]:
        is_win = True
        winning_player = player2
        
    elif choice_list[8] == players[player2] and choice_list[4] == players[player2] and choice_list[0] == players[player2]:
        is_win = True
        winning_player = player2


    return is_win, winning_player

def replay(play_active, choice_list):

    # if a draw or a win occurs, ask if the players would like to replay

    play_again_select = input("Would you like to play again? (Yes or No):\n")

    if play_again_select == 'Yes':
        play_active = True
        choice_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
    else:
        print("Thanks you for playing!")
        play_active = False

    return play_active, choice_list

def play_tic_tac_toe(): # the start game function

    play_active = True
    choice_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player_position = 0
    #player_dict = {'Player 1' : ' ', 'Player 2' : ' '}
    players = {}
    player1 = ''
    player2 = ''
    game_win = False
    turn_counter = 1
    

    while play_active:    

        players, player1, player2 = welcome_players()

        print("{0} is {1}\n".format(player1, players[player1]))
        print("{0} is {1}\n".format(player2, players[player2]))

        # print the board
        display_board(choice_list)

        while turn_counter < 10:

            print("TURN: {}\n".format(turn_counter))

            

            #*************************

            # PLAYER 1 TURN

            # ask Player 1 to choose a position
            player_position = choose_position(player1, choice_list)

            print("The position you chose is {}\n".format(player_position))

            choice_list = place_player_choice(choice_list, player_position, players[player1])

            display_board(choice_list)
            
            # Check Win   

            game_winner = check_win(choice_list, players, player1, player2)
            game_win = game_winner[0]

            if game_win == True:
                break

            if turn_counter >=9:
                break

            turn_counter += 1

            #************************

            # PLAYER 2 TURN

            print("TURN: {}\n".format(turn_counter))

            # ask Player 2 to choose a position
            player_position = choose_position(player2, choice_list)

            print("The position you chose is {}\n".format(player_position))

            choice_list = place_player_choice(choice_list, player_position, players[player2])

            display_board(choice_list)

            #*************************

            # Check win
            
            game_winner = check_win(choice_list, players, player1, player2)
            game_win = game_winner[0]

            if game_win:
                break

            if turn_counter >=9:
                break

            turn_counter += 1

        if turn_counter >= 9:
            
            print("The game is a draw!")

            # ask players if they would like to play again
            replay_parts = replay(play_active, choice_list)

            play_active = replay_parts[0]
            choice_list = replay_parts[1]
            turn_counter = 1
        
        elif game_win == True:

            print("Congratulations, {}! You are the winner!\n".format(game_winner[1]))

            # ask players if they would like to play again
            replay_parts = replay(play_active, choice_list)

            play_active = replay_parts[0]
            choice_list = replay_parts[1]
            turn_counter = 1

        # ~~debug statements~~
        #print(play_active)
        #print("The play active status is {}".format(play_active))
        #print("The reset list is {}".format(choice_list))


play_tic_tac_toe()

#FINISHED!
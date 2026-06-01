"""
"""
def gamestate(board):
    """
    param board: [str]
    return str
    """
    nb_x = sum(row.count("X") for row in board)
    nb_o = sum(row.count("O") for row in board)
    x_win = False
    o_win = False

 
    # Case O > X
    if nb_o > nb_x:
        raise ValueError("Wrong turn order: O started")

    if nb_x + nb_o > 9:
        print("Impossible board: game should have ended after the game was won")
        return "Impossible board: game should have ended after the game was won"

    # Case only XX
    if (nb_x >= 2 and nb_o == 0):
        print("Wrong turn order: X went twice")
        raise ValueError("Wrong turn order: X went twice")

        
    if nb_x >= 3 or nb_o >=3:
        lines = []

        # lignes
        lines.extend(board)

        # colonnes
        for col in range(3):
            lines.append(board[0][col] + board[1][col] + board[2][col])

        # diagonales
        lines.append(board[0][0] + board[1][1] + board[2][2])
        lines.append(board[0][2] + board[1][1] + board[2][0])
    
        if "XXX" in lines:
            x_win = True
    
        if "OOO" in lines:
            o_win = True

        # Draw
        if nb_x + nb_o == 9 and not x_win and not o_win:
            print("draw")
            return "draw"

    if x_win and o_win:
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )

    if x_win and nb_x != nb_o + 1:
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )

    if o_win and nb_x != nb_o:
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )

    if o_win or x_win:
        return "win"
    else:
        return "ongoing"

















    
    # # 1. Compter les pions
    # nb_x = sum(row.count('X') for row in board)
    # nb_o = sum(row.count('O') for row in board)

    # # 2. Vérifier si l'ordre des tours est respecté
    # # X commence, donc nb_x == nb_o OU nb_x == nb_o + 1
    # if not (nb_x == nb_o or nb_x == nb_o + 1):
    #     raise ValueError("Wrong turn order")

    # # 3. Définir les conditions de victoire
    # def check_win(p):
    #     # Lignes
    #     for row in board:
    #         if row[0] == row[1] == row[2] == p: return True
    #     # Colonnes
    #     for c in range(3):
    #         if board[0][c] == board[1][c] == board[2][c] == p: return True
    #     # Diagonales
    #     if board[0][0] == board[1][1] == board[2][2] == p: return True
    #     if board[0][2] == board[1][1] == board[2][0] == p: return True
    #     return False

    # win_x = check_win('X')
    # win_o = check_win('O')

    # # 4. Vérifier les cas invalides (Le jeu a continué après une victoire)
    # if win_x and win_o:
    #     raise ValueError("Continued playing after win")
    # if win_x and nb_x == nb_o: # X gagne, il doit avoir un pion de plus
    #     raise ValueError("Continued playing after win")
    # if win_o and nb_x > nb_o: # O gagne, ils doivent avoir le même nombre de pions
    #     raise ValueError("Continued playing after win")

    # # 5. Retourner l'état
    # if win_x or win_o:
    #     return "win"
    # if nb_x + nb_o == 9:
    #     return "draw"
    # return "ongoing"
    # nb_x = sum(row.count("X") for row in board)
    # nb_o = sum(row.count("O") for row in board)
    # if nb_o > nb_x:
    #     raise ValueError("Wrong turn order")

    # # lines
    # for row in board:
    #     if row[0] == row[1] == row[2] and row[0] != "":
    #         return "win"
    # # columns       
    # for col in range(3):
    #     if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
    #         return "win"
    # # diagonal
    # if board[0][0] == board[1][1] == board[2][2] and board[1][1] != "":
    #     return "win"
    # if board[0][2] == board[1][1] == board[2][0] and board[1][1] != "":  
    #     return "win"
    
    # if nb_x + nb_o == 9:
    #     return "draw"
        
    # return "ongoing"
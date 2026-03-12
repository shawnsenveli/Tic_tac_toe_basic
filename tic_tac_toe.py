
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

win_combination = [
    [(0,0), (0 ,1), (0,2) ],
    [(1,0), (1,1), (1,2)],
    [(2,0), (2,1), (2,2)],
    [(0,0), (1,0), (2,0)],
    [(0,1), (1,1), (2,1)],
    [(0,2), (1,2), (2,2)],
    [(0,0), (1,1), (2,2)],
    [(0,2), (1,1), (2,0)],
]

def print_board(board_temp):
    print("\n")
    print("   1   2   3")
    print("1 ", " | ".join(col for col in board_temp[0]))
    print("  ----------")
    print("2 ", " | ".join(col for col in board_temp[1]))
    print("  ----------")
    print("3 ", " | ".join(board_temp[2]))
    print("\n")




print_board(board)
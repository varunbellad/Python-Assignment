print("Varun Bellad, 1AY24AI096, Sec-O")
# ChessDictionaryValidator.py

def is_valid_chess_board(board):
    piece_counts = {
        'w': {'king': 0, 'pawn': 0},
        'b': {'king': 0, 'pawn': 0}
    }

    valid_positions = [f"{row}{col}" for row in range(1, 9) for col in 'abcdefgh']
    valid_pieces = {'king', 'queen', 'bishop', 'knight', 'rook', 'pawn'}

    for position, piece in board.items():
        # Validate board position
        if position not in valid_positions:
            print(f"Invalid position: {position}")
            return False

        # Validate piece format
        if len(piece) < 2 or piece[0] not in 'wb' or piece[1:] not in valid_pieces:
            print(f"Invalid piece: {piece}")
            return False

        color = piece[0]
        name = piece[1:]

        # Count kings and pawns
        if name == 'king':
            piece_counts[color]['king'] += 1
        elif name == 'pawn':
            piece_counts[color]['pawn'] += 1

    # Validate piece counts
    for color in 'wb':
        if piece_counts[color]['king'] != 1:
            print(f"{color} must have exactly one king.")
            return False
        if piece_counts[color]['pawn'] > 8:
            print(f"{color} has too many pawns.")
            return False

    return True

def main():
    # Example test board
    board = {
        '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen',
        '3e': 'wking', '2h': 'bpawn', '5g': 'wpawn', '4f': 'wpawn'
    }

    if is_valid_chess_board(board):
        print("The board is valid.")
    else:
        print("The board is invalid.")

if __name__ == "__main__":
    main()

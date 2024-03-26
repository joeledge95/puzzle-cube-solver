from structures.piece import Piece


class Cube:
    def __init__(self):
        # Array of 12 top pieces. [0] is top-front-left circling to [11] at top-left-front
        self.top_pieces = [Piece(top=True, position=i) for i in range(12)]

        # Array of 12 bottom pieces. [0] is bottom-front-left circling to [11] at bottom-left-front
        self.bottom_pieces = [Piece(top=False, position=i) for i in range(12)]

    def top_twist(self, n_shift_left):
        if n_shift_left < 1 or n_shift_left > 11:
            print('NO TWIST MADE: n_shift_right should be between 1 and 11')
            return

        self.top_pieces = self.top_pieces[n_shift_left:] + self.top_pieces[:n_shift_left]
        return

    def bottom_twist(self, n_shift_left):
        if n_shift_left < 1 or n_shift_left > 11:
            print('NO TWIST MADE: n_shift_right should be between 1 and 11')
            return

        self.bottom_pieces = self.bottom_pieces[n_shift_left:] + self.bottom_pieces[:n_shift_left]
        return

    def vertical_twist(self):
        temp_a_move_set = self.top_pieces[1:7]
        self.top_pieces[1:7] = self.bottom_pieces[1:7]
        self.bottom_pieces[1:7] = temp_a_move_set
        return

    def check_if_solved(self):
        # Top check
        for i, top_piece in enumerate(self.top_pieces):
            if (not top_piece.default_top) or (top_piece.default_position != i):
                return False

        # Bottom check
        for i, bottom_piece in enumerate(self.bottom_pieces):
            if bottom_piece.default_top or (bottom_piece.default_position != i):
                return False

        # If pass return true
        return True

    def set_new_orientation(self, top_pieces, bottom_pieces):
        if len(top_pieces) != 12 or len(bottom_pieces) != 12:
            print('Incorrect pieces set')
            return

        for i in range(12):
            # Check if ith top piece is there
            top_piece_found = False
            for top_piece in top_pieces:
                if top_piece.default_top and top_piece.default_position == i:
                    top_piece_found = True

            for bottom_piece in bottom_pieces:
                if (not bottom_piece.default_top) and bottom_piece.default_position == i:
                    top_piece_found = True

            if not top_piece_found:
                print('Incorrect pieces set')
                return

            # Check if ith bottom piece is there
            bottom_piece_found = False
            for bottom_piece in bottom_pieces:
                if bottom_piece.default_top and bottom_piece.default_position == i:
                    bottom_piece_found = True

            for bottom_piece in bottom_pieces:
                if (not bottom_piece.default_top) and bottom_piece.default_position == i:
                    bottom_piece_found = True

            if not bottom_piece_found:
                print('Incorrect pieces set')
                return

        # Do something
        self.top_pieces = top_pieces
        self.bottom_pieces = bottom_pieces
        return

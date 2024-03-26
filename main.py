from structures.cube import Cube
from structures.piece import Piece

if __name__ == '__main__':
    # Create cube
    cube = Cube()
    print(cube.check_if_solved())
    cube.vertical_twist()
    print(cube.check_if_solved())
    cube.vertical_twist()
    print(cube.check_if_solved())
    cube.set_new_orientation(
        top_pieces=[
            Piece(True, i)
            for i in range(12)
        ],
        bottom_pieces=[
            Piece(False, j)
            for j in [6, 7, 0, 5, 1, 8, 4, 3, 2, 9, 10, 11]
        ]
    )
    pass

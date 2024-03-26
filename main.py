from structures.cube import Cube
from structures.piece import Piece
from solvers.brute_force_solver import BruteForceSolver

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
    solver = BruteForceSolver(cube)
    #solver = BruteForceSolver(Cube())  # With new cube
    #solver.solve(max_moves=100000000, verbose=True)

    unsolved = True
    while unsolved:
        if solver.solve(max_moves=20):
            print('Solution:')
            print(solver.solution)
            unsolved = False

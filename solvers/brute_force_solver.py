import random
import copy


class BruteForceSolver:
    def __init__(self, cube):
        self.cube = copy.deepcopy(cube)
        self.solution = []

    def solve(self, max_moves, verbose=False):
        self.solution = []
        cube = copy.deepcopy(self.cube)

        for i in range(max_moves):
            if i % 2 == 0:  # Only need to check even due to even no. x vertical moved needed to be solvable
                if cube.check_if_solved():
                    print(f'Solved in {i} moves!')
                    self.solution.append('SOLVED')
                    return True

            # Randomly move the cube
            random_int = random.randint(0, 2)

            if random_int == 0:
                n_shift_left = random.randint(1, 11)
                cube.top_twist(n_shift_left)
                self.solution.append(f'T{n_shift_left}')
            elif random_int == 1:
                n_shift_left = random.randint(1, 11)
                cube.bottom_twist(n_shift_left)
                self.solution.append(f'B{n_shift_left}')
            else:
                cube.vertical_twist()
                self.solution.append('V')

        if verbose:
            print(f'Unsolved after {max_moves} moves')
        self.solution.append('UNSOLVED')
        return False

        pass

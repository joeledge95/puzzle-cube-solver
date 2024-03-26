from structures.cube import Cube

if __name__ == '__main__':
    # Create cube
    cube = Cube()
    print(cube.check_if_solved())
    cube.vertical_twist()
    print(cube.check_if_solved())
    cube.vertical_twist()
    print(cube.check_if_solved())
    pass

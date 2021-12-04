import os

UP = 'up'
DOWN = 'down'
FORWARD = 'forward'


def get_final_position():
    current_x, current_y = 0, 0
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt'), 'r') as file:
        for line in file.readlines():
            [direction, inputStr] = line.strip().split(" ")
            input_int = int(inputStr)

            if direction == UP:
                current_y -= input_int
            elif direction == DOWN:
                current_y += input_int
            elif direction == FORWARD:
                current_x += input_int

    return current_x, current_y


if __name__ == '__main__':
    x, y = get_final_position()

    print('x:', x, 'y:', y)
    print('product:', x * y)

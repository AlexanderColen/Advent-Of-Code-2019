import itertools


def read_input():
    with open('input_day7', 'r') as f:
        data = [int(x) for x in f.readlines()[0].split(',')]

    return data


def run_intcode(intcode, start_input, second_input, feedback_mode=False):
    i = 0
    post_first_input = False
    print(intcode)

    while i < len(intcode):
        instruction = f'{intcode[i]:05}'

        opcode = int(instruction[slice(3, 5)])
        mode_first_parameter = int(instruction[slice(2, 3)])
        mode_second_parameter = int(instruction[slice(1, 2)])

        # Decide parameters.
        if opcode != 99:
            if mode_first_parameter == 0:
                first_param = int(intcode[intcode[i + 1]])
            else:
                first_param = int(intcode[i + 1])

            if opcode in [1, 2, 5, 6, 7, 8]:
                if mode_second_parameter == 0:
                    second_param = int(intcode[intcode[i + 2]])
                else:
                    second_param = int(intcode[i + 2])

        # Handle opcodes.
        if opcode == 1:
            # Addition
            intcode[intcode[i + 3]] = first_param + second_param
            i += 4
        elif opcode == 2:
            # Multiplication
            intcode[intcode[i + 3]] = first_param * second_param
            i += 4
        elif opcode == 3:
            # Input
            if not post_first_input:
                input_value = start_input
                post_first_input = True
            else:
                input_value = second_input
            intcode[intcode[i + 1]] = input_value
            i += 2
        elif opcode == 4:
            # Output
            if not feedback_mode:
                return first_param
            output = first_param
            return output, intcode
            i += 2
        elif opcode == 5:
            # Jump if true
            if first_param != 0:
                i = second_param
            else:
                i += 3
        elif opcode == 6:
            # Jump if false
            if first_param == 0:
                i = second_param
            else:
                i += 3
        elif opcode == 7:
            # Less than
            if first_param < second_param:
                intcode[intcode[i + 3]] = 1
            else:
                intcode[intcode[i + 3]] = 0
            i += 4
        elif opcode == 8:
            # Equals
            if first_param == second_param:
                intcode[intcode[i + 3]] = 1
            else:
                intcode[intcode[i + 3]] = 0
            i += 4
        elif opcode == 99:
            # Abort
            if not feedback_mode:
                return intcode[0]

            return output
        else:
            print(f'INVALID: {instruction} - {i}')


def puzzle1():
    phase_settings = [0, 1, 2, 3, 4]
    second_setting = 0
    max_thruster = 0

    for combo in itertools.permutations(phase_settings):
        for c in combo:
            second_setting = run_intcode(intcode=read_input(),
                                         start_input=c,
                                         second_input=second_setting,
                                         feedback_mode=False)
        if second_setting > max_thruster:
            max_thruster = second_setting
        second_setting = 0

    return max_thruster


def puzzle2():
    phase_settings = [5, 6, 7, 8, 9]
    intcode = read_input()
    second_setting = 0
    max_thruster = 0

    for combo in itertools.permutations(phase_settings):
        for c in combo:
            second_setting, intcode = run_intcode(intcode=intcode,
                                                  start_input=c,
                                                  second_input=second_setting,
                                                  feedback_mode=True)
        if second_setting > max_thruster:
            max_thruster = second_setting
        second_setting = 0
        intcode = read_input()

    return max_thruster


if __name__ == '__main__':
    print(f'Puzzle 1 outcome: {puzzle1()}')
    print(f'Puzzle 2 outcome: {puzzle2()}')

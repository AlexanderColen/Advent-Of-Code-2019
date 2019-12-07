def read_input():
    with open('input_day5', 'r') as f:
        data = [int(x) for x in f.readlines()[0].split(',')]
        print(data)

    return data


def run_intcode(intcode):
    i = 0

    while i < len(intcode):
        instruction = f'{intcode[i]:05}'

        opcode = int(instruction[slice(3, 5)])
        mode_first_parameter = int(instruction[slice(2, 3)])
        mode_second_parameter = int(instruction[slice(1, 2)])
        mode_third_parameter = int(instruction[slice(0, 1)])
        # print(instruction, mode_third_parameter, mode_second_parameter, mode_first_parameter, opcode)

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
            intcode[intcode[i + 1]] = input('Please enter the parameter input:\n>>>')
            i += 2
        elif opcode == 4:
            # Output
            print(first_param)
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
            return intcode[0]
        else:
            print(f'INVALID: {instruction} - {i}')

    return None


def puzzle1():
    print('Running puzzle 1...')
    run_intcode(read_input())


def puzzle2():
    print('Running puzzle 2...')
    run_intcode(read_input())


if __name__ == '__main__':
    """
    test_input = [3, 0, 4, 0, 99]
    test_input = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    test_input = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
    test_input = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
    run_intcode(test_input)
    """

    puzzle1()
    puzzle2()

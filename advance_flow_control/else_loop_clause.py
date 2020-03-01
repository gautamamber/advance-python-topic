import operator
"""
Stack evaluate program using else loop clause
"""


def is_comment(item):
    """
    check if an item is comment or not
    :param item:
    :return:
    """
    return isinstance(item, str) and item.startswith("#")


def execute(program):
    """
    Execute a stack program
    :param program: Any stack where each item is a operand or operator, In this we are  also using comment
    start with # (hash) for documentation, skip comment
    :return:
    """
    # while loop to clear comment
    # False if program is empty
    while program:
        item = program.pop()
        if not is_comment(item):
            program.append(item)
            break
    else:
        print("Empty program")
        return

    # Evaluate the program
    pending = []
    while program:
        item = program.pop()
        if callable(item):
            try:
                result = item(*pending)
            except Exception as ex:
                print("error is ", ex)
                break
            program.append(result)
            pending.clear()
        else:
            pending.append(item)
    else:
        print("Program successful")
        print("Result is", pending)

    print("Finish !")


if __name__ == "__main__":
    program = list(reversed((
        "# A  stack program to add and",
        "# Multiply some constant",
        5,
        3,
        operator.add,
        7,
        operator.mul,
    )))
    # above statement is: (5+3)*7
    execute(program)

"""
Emulate switch statements instead of multiple if else
"""


def one():
    """
    month one
    :return:
    """
    return "January"


def two():
    """
    month two
    :return:
    """
    return "Feb"


def three():
    """
    month three
    :return:
    """
    return "March"


def convert_number_to_months(argument):
    switcher = {
        1: one,
        2: two,
        3: three
    }
    func = switcher.get(argument, "Invalid")
    print(func())


convert_number_to_months(2)

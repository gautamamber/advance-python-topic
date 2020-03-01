class Example(object):
    """
    Call __new__ first for creating instance of class
    and then __init__ for initialize the class
    """
    def __new__(cls, *args, **kwargs):
        """
        creating class instance
        :param args:
        :param kwargs:
        """
        print("Instance of class is creating")
        return super(Example, cls).__new__(cls)

    def __init__(self):
        """
        Initialize class
        """
        print("Class is initialize")


Example()

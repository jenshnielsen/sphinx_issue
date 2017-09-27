from mymodule.class_a import AClass


class B:
    """
    A Simple Class

    :param AClass a: small amount of info
    """
    def __init__(self, a: AClass) -> None:
        self.a = a

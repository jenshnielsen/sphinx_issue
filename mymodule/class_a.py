"""
This is a module doc string
"""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mymodule.class_b import B


class AClass:
    """
    A Simple Class

    :param 'B' my_b: small amount of info
    :param str test: small little info str
    """
    def __init__(self, my_b: 'B' = None, test: str = None) -> None:
        self.my_b = my_b
        self.test = test

    def method_1(self, variable_1):
        """

        :param variable_1: note
        :return: list
        """
        return variable_1 + self.my_b

    def method_2(self, variable_2):
        """

        :param variable_2: note
        :return: list
        """
        return variable_2 + self.my_b

from unittest import TestCase
from mymodule.class_a import AClass
from mymodule.class_b import B


class Test(TestCase):
    def test_can_create(self) -> None:
        a = AClass()
        b = B(a)

        self.assertIsInstance(a, AClass)
        self.assertIsInstance(b, B)

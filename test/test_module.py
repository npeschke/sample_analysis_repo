from unittest import TestCase
import analysis_package.module as module


class Test(TestCase):
    def test_hello_world(self):
        self.assertEqual("Hello World!", module.get_hello_world())

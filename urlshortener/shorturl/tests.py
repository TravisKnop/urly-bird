from django.test import TestCase

# Create your tests here.

class InputModelTests(TestCase):

    def initial_fail_test(self):
        """The initial models function should receive an input and print it"""
        self.fail("YES!")

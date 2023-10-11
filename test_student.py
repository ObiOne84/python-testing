import unittest
from student import Student


class TestStudent(unittest.TestCase):

    # below are class methods, that run at the start
    # and at the end of the test, we must pass cls
    # parameter and use @classmethod decorator
    # if we want to populate database with data, we can
    # use setUpClass and tearDownClass methods
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    # setUp and tearDown methods must be define using camel case
    # otherwise won't run, setUp must be defined first
    # both run before and after each method
    def setUp(self):
        print('setup')
        self.student = Student('John', 'Doe')

    def tearDown(self):
        print('tearDown')

    def test_full_name(self):
        # once we craete setUp we can remove repetetive code
        # student = Student('John', 'Doe')
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Doe')

    # here we add new test, to check, if the alert_method returns
    # true or false for student.naughtly_list
    # fails at the starts, as we don't have method defined yet
    def test_alert_santa(self):
        # student = Student('John', 'Doe')
        print('test_alert_santa')
        self.student.alert_santa()

        self.assertTrue(self.student.naughtly_list)

    def test_email(self):
        # student = Student('John', 'Doe')
        print('test_email')
        self.assertEqual(self.student.email, 'john.doe@email.com')


if __name__ == '__main__':
    unittest.main()

import unittest
from student import Student


class TestStudent(unittest.TestCase):
    def test_full_name(self):
        student = Student('John', 'Doe')

        self.assertEqual(student.full_name, 'John Doe')

    # here we add new test, to check, if the alert_method returns
    # true or false for student.naughtly_list
    # fails at the starts, as we don't have method defined yet
    def test_alert_santa(self):
        student = Student('John', 'Doe')
        student.alert_santa()

        self.assertTrue(student.naughtly_list)

    def test_email(self):
        student = Student('John', 'Doe')

        self.assertEqual(student.email, 'john.doe@email.com')


if __name__ == '__main__':
    unittest.main()

from datetime import date, timedelta
import requests


class Student:
    """
    A Student class as base for method testing
    """

    def __init__(self, first_name, last_name):
        # _first_name; underscore at the start means
        # read only
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughtly_list = False

    # the poperty decorator to highlight that this is
    # get data method only (read only)
    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    def alert_santa(self):
        self.naughtly_list = True

    @property
    def email(self):
        return f"{self._first_name}.{self._last_name}@email.com".lower()

    def apply_extension(self, num):
        self.end_date = self.end_date + timedelta(days=num)

    def course_schedule(self):
        response = requests.get(
            f"http://company.com/course-schedule/{self._last_name}/{self._first_name}")
    
        if response.ok:
            return response.text
        else:
            return "Something went wrong with the request!"

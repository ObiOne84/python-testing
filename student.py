from datetime import date, timedelta


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

    def fule_name(self):
        return f"{self._first_name} {self._last_name}"
import time
from log_management import Log_Management


class Time_Management(Log_Management):
    def __init__(self, special_times: list, verbose: bool = False) -> None:
        self.special_times: list = special_times
        self._verbose = verbose

        Log_Management.__init__(self)

    def check_time(self, given_time: str, time_format: str = "%H:%M") -> bool:
        """
        This method accomplishes if given time is equal to computer's time and returns boolean value.
        True/False

        :param time_format: This argument needs to be in like "%H:%M:%S".
        :param given_time: must have given like that  format. H:M (H: hour, M: minute)
        :return: boolean value
        """
        if given_time == time.strftime(time_format) or time.strftime(time_format) in self.special_times:
            self.log(f"Time ({time.strftime(time_format)}) checked and this is time in given times.", self.INFO)
            return True

        return False

    def now(self, time_format: str = "%H:%M") -> str:
        """
        This method accomplishes that get computer time and format as wanted and return as string.

        :param time_format: This argument needs to be in like "%H:%M:%S".
        :return: Computer time at this moment and formatted as time format.
        """
        if self._verbose:
            print(time.strftime(time_format))

        return time.strftime(time_format)

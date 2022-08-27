import time
import os
from tkinter import messagebox


class Log_Management:
    INFO = 0
    ERROR = 1

    def __init__(self, log_path: str = "auto_save_logs.txt", time_format: str = "%H:%M:%S",
                 verbose: bool = True) -> None:

        self._log_path = log_path
        self._time_format = time_format
        self._levels = {
            0: "[INFO]",
            1: "[ERROR]",
        }
        self._verbose = verbose
        self._codec = "utf-8"

        self.INFO = 0
        self.ERROR = 1

        read_method: str = "a"

        if not os.path.exists(self._log_path):
            read_method = "w"

        with open(log_path, read_method, encoding=self._codec) as log:
            log.write(f"{time.strftime(self._time_format)} [INFO]: Auto Save opened.\n")

            if verbose:
                print(f"{time.strftime(self._time_format)} [INFO]: Auto Save opened.\n")

    def log(self, argument: str, level: int) -> bool:
        """
        This function performs the logging process after what has done. Argument parameter is explanation of
        what has done in program.

        :param argument: This parameter is definition what has done in program.
        :param level: This parameter demonstrate level of argument.
        :return: If logging process is successful return boolean value to represent that process's success.True / False
        """

        try:
            with open(self._log_path, "a", encoding=self._codec) as log:
                log.write(f"{time.strftime(self._time_format)} {self._levels[level]}: {argument}\n")
                if self._verbose:
                    print(f"{time.strftime(self._time_format)} {self._levels[level]}: {argument}\n")

            return True

        except Exception as e:
            messagebox.showerror("Caught Exception", f"Auto Save program has raised error: {e} while trying to log the "
                                                     f"\"{argument}\" activity.")
            if self._verbose:
                print("Caught Exception", f"Auto Save program has raised error: {e} while trying to log the "
                                          f"\"{argument}\" activity.")

            return False

    def errors_in_logs(self) -> list:
        logs: str
        all_lines: list

        try:
            with open(self._log_path, "r", encoding=self._codec) as log:
                logs = log.read()

            all_lines = logs.split("\n")
            all_errors: list = [argument for argument in all_lines if self._levels[self.ERROR] in argument]

            if not all_errors:
                all_errors = ["Program runs"]

            if self._verbose:
                print(f"{self._levels[self.ERROR]}: all_errors in program:", all_errors)

            return all_errors

        except Exception as e:
            messagebox.showerror("Caught Exception", f"Auto Save program has raised error: {e} while trying to reading"
                                                     f"the logs and reporting the errors to developer.")

            if self._verbose:
                print("Caught Exception", f"Auto Save program has raised error: {e} while trying to reading"
                                          f"the logs and reporting the errors to developer.")

            return ["Caught Exception", f"Auto Save program has raised error: {e} while trying to reading"
                                        f"the logs and reporting the errors to developer."]

    def get_log_at_time(self, given_time: str) -> list:
        """
        This method accomplishes that to get all logs at given time and returns list of logs at the time.

        :param given_time: This argument needs to be in this format "%H", "%H:%M" and "%H:%M:%S"
        :return: Returns list with logs at the given time.
        """
        try:
            with open(self._log_path, "r", encoding=self._codec) as log:
                logs = log.read()

            all_lines: list = logs.split("\n")
            all_logs_at_time: list = [argument for argument in all_lines if given_time in argument]

            if self._verbose:
                print(f"All logs at time {given_time}", all_logs_at_time)

            return all_logs_at_time

        except Exception as e:
            self.log(f"Program can not reach the log at given time ({given_time})", level=1)

            if self._verbose:
                print("Caught Exception", f"Auto Save program has raised error: {e} while trying to "
                                          f"reach the log at given time ({given_time})")

            return ["Caught Exception", f"Auto Save program has raised error: {e} while trying to "
                                        f"reach the log at given time ({given_time})"]


if __name__ == "__main__":
    log = Log_Management()

    log.log("Log test for error", level=1)
    log.log("Log test for info", level=0)

    print(log.get_log_at_time("23:15"))
    print(log.errors_in_logs())

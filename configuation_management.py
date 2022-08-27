import os
import sys
from tkinter import messagebox
from log_management import Log_Management


class Configuration_Management(Log_Management):
    def __init__(self, configuration_file_path: str = "auto_save.config",
                 verbose: bool = False):
        Log_Management.__init__(self, verbose=verbose)
        self._configuration_file_path: str = configuration_file_path
        self._verbose = verbose

        if not os.path.exists(self._configuration_file_path):
            self.log("Configuration file is not found.", self.ERROR)
            self._create_configuration_file()
            messagebox.showerror("Configuration File", "Configuration file is not found. Configuratin file created."
                                                       "Please configurate the configuraiton "
                                                       "file. Program will shutdown in a while.")
            sys.exit(0)

    def _create_configuration_file(self):
        try:
            with open(self._configuration_file_path, "w", encoding=self._codec) as config:
                config.write("[SAVE_PATH]\n"
                             "[FOLDER_PATH]\n"
                             "[FILE_EXTENTIONS]\n"
                             "[NOT_WANTED_FILE_EXTENTIONS]\n"
                             "[SAVE_TIME]")

                if self._verbose:
                    print("[SAVE_PATH]\n"
                          "[FOLDER_PATH]\n"
                          "[FILE_EXTENTIONS]\n"
                          "[NOT_WANTED_FILE_EXTENTIONS]\n"
                          "[SAVE_TIME]")

        except Exception as e:
            messagebox.showerror("Configuration File", f"Configuration file can not be created. Raised error {e}.")

    def configurations(self) -> dict:
        configuration = {
            "[SAVE_PATH]": "",
            "[FOLDER_PATH]": "",
            "[FILE_EXTENTIONS]": "",
            "[NOT_WANTED_FILE_EXTENTIONS]": "",
            "[SAVE_TIME]": ""
        }

        try:
            with open(self._configuration_file_path, "r", encoding=self._codec) as config:
                config = config.read()

            self.log("Configuration file has read.", self.INFO)

            for statement in config.split("\n"):
                temp = statement.split("]")

                #if "PATH" in temp[0]:
                    #configuration[temp[0]] = temp[-2] + ":" + temp[-1]
                    #continue

                configuration[temp[0]+"]"] = temp[-1]

            return configuration

        except Exception as e:
            messagebox.showerror("Config File", "Configuration file can not read please ")
            self.log(f"Can't read the config file. Raised error {e}", self.ERROR)

            if self._verbose:
                print(f"Can't read the config file. Raised error {e}")

            return {}


if __name__ == "__main__":
    config = Configuration_Management()
    print(config.configurations())

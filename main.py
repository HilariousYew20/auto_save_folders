from file_management import File_Management
from configuation_management import Configuration_Management
from log_management import Log_Management
import time
import os


def main():
    file_stat = os.stat("auto_save_logs.txt")
    if file_stat.st_size > 20 * 1024:
        os.remove("auto_save_logs.txt")

    starting_time = time.time()
    config = Configuration_Management()
    configurations = config.configurations()

    save_path = configurations["[SAVE_PATH]"]
    folder_path = configurations["[FOLDER_PATH]"].split(",")
    file_extentions = configurations["[FILE_EXTENTIONS]"].replace(" ", "").split(",")
    not_wanted_file_extentions = configurations["[NOT_WANTED_FILE_EXTENTIONS]"].replace(" ", "").split(",")
    save_time = configurations["[SAVE_TIME]"].replace(" ", "")

    file = File_Management(
        folder_path=folder_path,
        save_folder_path=save_path,
        file_formats=file_extentions,
        not_wanted_file_extentions=not_wanted_file_extentions,
        verbose=False
    )

    file.copy_files()
    log = Log_Management()
    end_time = time.time()
    log.log(f"Auto Save program finished in {end_time - starting_time}. ", log.INFO)


if __name__ == "__main__":
    main()

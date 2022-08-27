import os
import shutil

from log_management import Log_Management


class File_Management(Log_Management):
    def __init__(self, folder_path: str, save_folder_path: str, file_path: str = "", file_formats=None,
                 not_wanted_file_extentions=None, verbose: bool = False):

        Log_Management.__init__(self)

        self._verbose = verbose
        self.paths: list = []
        self._real_paths: list = []
        self._save_paths: list = []

        self._save_folder_path = save_folder_path

        if not os.path.exists(self._save_folder_path):
            os.mkdir(self._save_folder_path)
            self.log(f"Created folder, '{save_folder_path}'.", self.INFO)

            if self._verbose:
                print(f"Created folder '{save_folder_path}'.")

        if file_formats is None:
            file_formats = ["*"]

        self._file_formats = file_formats

        if not_wanted_file_extentions is None:
            not_wanted_file_extentions = [""]

        self._not_wanted_file_extentions = not_wanted_file_extentions

        self._folder_path = folder_path
        self._file_path = file_path

    def get_paths(self) -> list:
        """
        This methods accomplish that get all file paths in wanted formats.

        :return: List with wanted file format file's path.
        """
        """  
        for file_extentions in self._file_formats:
            for _folder_path in self._folder_path:
                for file_paths in glob.glob(os.path.join(_folder_path, "*" + file_extentions)):
                    self.paths.append(file_paths)"""

        self._save_folder_path.replace("/", "\\")
        if not self._save_folder_path.endswith("\\"):
            self._save_folder_path += "\\"

        try:
            for _folder_path in self._folder_path:
                for root, dirs, files in os.walk(_folder_path):
                    for n in dirs:
                        if not os.path.exists(self._save_folder_path + os.path.join(root, n).split(_folder_path)[-1]):
                            os.mkdir(self._save_folder_path + os.path.join(root, n).split(_folder_path)[-1])

                            self.log(
                                f"Folder created at {self._save_folder_path + os.path.join(root, n).split(_folder_path)[-1]}",
                                self.INFO)

                            if self._verbose:
                                print("Folder created at",
                                      self._save_folder_path + os.path.join(root, n).split(_folder_path)[-1])

                    for name in files:
                        if "." + name.split(".")[-1] in self._not_wanted_file_extentions:
                            continue

                        elif "." + name.split(".")[-1] in self._file_formats:
                            self._save_paths.append(
                                self._save_folder_path + os.path.join(root, name).split(_folder_path)[-1])
                            self._real_paths.append(os.path.join(root, name))

                            if self._verbose:
                                print(self._save_folder_path + os.path.join(root, name).split(_folder_path)[-1])

                        if self._file_formats == ['']:
                            self._save_paths.append(
                                self._save_folder_path + os.path.join(root, name).split(_folder_path)[-1])
                            self._real_paths.append(os.path.join(root, name))

                            if self._verbose:
                                print(self._save_folder_path + os.path.join(root, name).split(_folder_path)[-1])

                            continue

            self.paths.append(self._real_paths)
            self.paths.append(self._save_paths)

            del self._real_paths
            del self._save_paths

            return self.paths

        except Exception as e:
            self.log(f"Auto save program got an error during locating files. Error: {e}", self.ERROR)

            if self._verbose:
                print(f"Auto save program got an error during locating files. Error: {e}")

    def copy_files(self) -> bool:
        """
        new method
        :return:
        """
        self.get_paths()
        save_path = ""

        try:
            real_path, save_path = self.paths
            for real_path, save_path in zip(real_path, save_path):
                shutil.copy(real_path, save_path)

                self.log(f"Copied file '{real_path}' to '{save_path}'", self.INFO)

                if self._verbose:
                    print(f"Copied file '{real_path}' to '{save_path}'")
            return True

        except Exception as e:
            self.log(f"During the copying file '{save_path}' program has got an error: '{e}'",
                     self.ERROR)

            if self._verbose:
                print(f"During the copying file '{save_path}' program has got an error: '{e}'")

            return False

    def _copy_files(self) -> bool:
        """
        old copy method
        """
        if not self.paths:
            self.get_paths()

        destination_path: str = "empty"
        try:
            for path in self.paths:
                destination_path = os.path.join(self._save_folder_path, path.split("\\")[-1])
                shutil.copy(path, destination_path)

                self.log(f"Copied file '{path}' to '{destination_path}'", Log_Management.INFO)

                if self._verbose:
                    print(f"Copied file '{path}' to '{destination_path}'")

            return True

        except Exception as e:
            self.log(f"During the copying file '{destination_path}' program has got an error: '{e}'",
                     self.ERROR)

            if self._verbose:
                print(f"During the copying file '{destination_path}' program has got an error: '{e}'")

            return False

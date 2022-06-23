"""Module for the organizer class"""

from os import path, listdir
import shutil

from directory import Directory
from file import File
from organizer_options import OrganizerOptions


class Organizer:
    """Class to organize files.

    Organizes the files in thier respective directories by creating a
    folder named by thier extensions.

    Attributes:
        directory: The directory in which the files will be organized.
    """
    directory: Directory
    files: list[File] = []
    options: OrganizerOptions

    def __init__(self, directory, options: OrganizerOptions = None) -> None:
        self.directory = directory
        self.options = options

        for file_path in listdir(directory.path):
            if path.isfile(path.join(directory.path, file_path)):
                file = File(path.abspath(file_path))
                self.files.append(file)

    def organize(self) -> None:
        """Organize the files provided"""
        for file in self.files:
            destination_directory = Directory(path=path.join(file.directory.path, file.extension))
            destination_directory.mkdir()
            shutil.move(file.path, path.join(destination_directory.path, file.name))

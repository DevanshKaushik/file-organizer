"""Module for file class"""

from dataclasses import dataclass, field
import os

from directory import Directory


@dataclass(frozen=True)
class File:
    """Class to store file details.

    Attributes:
        path: A string representing the path of the file.
        name: A string representing the name of the file with its extension.
            (auto generated from path)
        extension: A string representing the extension of the file.
            (auto generated from path)
        directory: A Directory object representing the directory in which the
            file is located.
            (auto generated from path)
    """
    path: str
    name: str = field(init=False)
    extension: str = field(init=False)
    directory: Directory = field(init=False)

    def __post_init__(self):
        head, tail = os.path.split(self.path)
        object.__setattr__(self, 'name', tail)
        object.__setattr__(self, 'extension', tail.split(".")[1])
        object.__setattr__(self, 'directory', Directory(path=head))

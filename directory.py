"""Module for directory class"""

from dataclasses import dataclass, field
import sys
import os


@dataclass(frozen=True, kw_only=True)
class Directory:
    """Class to store the directory details.

    Attributes:
        path: A string representing path of the directory.
            (default is system arguments if provided, or current
            working directory)
        name: A string representing the name of the directory.
        set_cwd: If true the directory will be set as current working
            directory.
            (default is False)
    """
    path: str = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    set_cwd: bool = field(default=False, repr=False)

    def __post_init__(self) -> None:
        if self.set_cwd:
            self.chdir()

    def mkdir(self) -> None:
        """Create new directory using path."""
        try:
            os.mkdir(self.path)
        except FileExistsError:
            print(f"Info: {self.path} already exists")

    def chdir(self) -> None:
        """Changes current working directory to this directory"""
        try:
            os.chdir(self.path)
        except FileNotFoundError:
            print(f"Error: f{self.path} does not exist")

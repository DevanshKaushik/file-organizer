"""Module for organizing files in a directory"""

from directory import Directory
from organizer import Organizer


def main() -> None:
    """Main function"""
    directory = Directory(set_cwd=True)
    organizer = Organizer(directory)
    organizer.organize()


if __name__ == "__main__":
    main()

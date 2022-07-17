# File Organizer

A python script to organize the os files in seperate directories according to their extensions names.

## Description

For a given directory, this script creates sub-directories with names taken from extension names of the files present in it.
Then it moves all the files to their respective directories according to their extensions.

The organizer script takes one optional argument:

`dir_path`: the path to the parent directory to organize the files from.

NOTE: If `dir_path` is not provided, then the script executes in the current working directory.

## Requirements

You need `python 3.5` or above to run this script.

## How to run?

You can run this script from command line using:

- On windows run:
```
file_organizer dir_path
```

- On unix based os run:
```
bash file_organizer.sh dir_path
```

or add executable permission

```
chmod u+x file_organizer.sh
./file_organizer.sh dir_path
```

You can use functions directly by executing the following code:
```python
from directory import Directory
from organizer import Organizer

directory = Directory(path="path_to_dir", set_cwd=True)
organizer = Organizer(directory)
organizer.organize()
```

## Contributing

Pull requests are always welcome. For major changes, please open an issue first to discuss what you would like to change.

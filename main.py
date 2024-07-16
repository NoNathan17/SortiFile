from pathlib import Path
import shutil
from datetime import datetime

def determine_file(directory: Path):
    for file in directory.iterdir():
        if file.is_file():
            sort_file(directory, file)

def sort_file(directory: Path, file: Path):
    file_suffix = file.suffix[1:] if file.suffix else 'no extension'

    new_folder = create_new_folder(directory, file_suffix)
    new_folder.mkdir(parents=True, exist_ok=True)
    shutil.move(str(file), str(new_folder))
                
def create_new_folder(directory: Path, suffix: str) -> Path:
    new_folder = directory / f"{suffix}s folder"

    return new_folder


if __name__ == "__main__":
    directory = Path(input('Enter directory path: ').strip())
    try:
        determine_file(directory)
        print('Files sorted successfully!')
    except FileNotFoundError:
        print('The directory given does not exist.')
    except Exception as e:
        print(f'An error has occurred: {e}')

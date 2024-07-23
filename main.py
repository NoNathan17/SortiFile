from pathlib import Path
import shutil
from datetime import datetime
import gui

def determine_file(directory: Path, sort_by: str):
    for file in directory.iterdir():
        if file.is_file():
            if sort_by == 'extension':
                sort_by_extension(directory, file)
            elif sort_by == 'date':
                sort_by_date(directory, file)

def sort_by_extension(directory: Path, file: Path):
    file_suffix = file.suffix[1:] if file.suffix else 'no extension'

    new_folder = create_new_extension_folder(directory, file_suffix)
    new_folder.mkdir(parents=True, exist_ok=True)
    shutil.move(str(file), str(new_folder))

def create_new_extension_folder(directory: Path, suffix: str) -> Path:
    new_folder = directory / f"{suffix}s folder"
    return new_folder

def sort_by_date(directory: Path, file: Path): 
    try:
        creation_time = datetime.fromtimestamp(file.stat().st_birthtime) 
    except AttributeError:
        creation_time = datetime.fromtimestamp(file.stat().st_ctime) 

    month = creation_time.strftime("%B")
    year = creation_time.strftime("%Y")

    new_folder = create_new_date_folder(directory, month, year)
    new_folder.mkdir(parents=True, exist_ok=True)
    shutil.move(str(file), str(new_folder))

def create_new_date_folder(directory: Path, month: str, year: str) -> Path:
    new_folder = directory / f"{month} {year}"
    return new_folder

if __name__ == "__main__":
    gui.root.mainloop()
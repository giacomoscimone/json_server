import os
import shutil
from typing import Any


def clean_up(location_path: str, logger: Any) -> None:
    file_list = os.listdir(location_path)

    for file_path in file_list:
        os.remove(location_path + file_path)
        logger.debug(f"removed file: {location_path + file_path}")


def create_save_location(save_location: str) -> None:
    os.makedirs(save_location, exist_ok=True)


def save_file(file, save_location: str) -> None:
    with open(save_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)

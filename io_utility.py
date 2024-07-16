import os
import shutil
from typing import Any
import logging

logger = logging.getLogger('my_logger')


def clean_up(location_path: str) -> None:
    file_list = os.listdir(location_path)
    for file_path in file_list:
        os.remove(location_path + file_path)
        logger.debug(f"removed file: {location_path + file_path}")


def create_save_location(save_location: str) -> None:
    logger.info("creazione cartella completata")

    os.makedirs(save_location, exist_ok=True)


def save_file(file, save_location: str) -> None:
    logger.info("salvataggio file completato")

    with open(save_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)

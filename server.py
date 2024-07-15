import sys
sys.path.append("C:/Users/Alternanza/Documents/GitHub/alternanza")
import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import shutil
import os
from io_utils import load_model
from io_utils import load_image
from image_utils import preproces_image
from predictor import predict
import logging



app = FastAPI()

original = 'C:/Users/Alternanza/Documents/GitHub/json_server'

MODEL_PATH = 'C:\\Users\\Alternanza\\Downloads\\keras_model.h5'

save_location = original + '/files/'

log_path = original + '/log/info.txt'

MODEL = load_model(MODEL_PATH)

# os.makedirs(log_path, exist_ok=True)

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(log_path)
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def clean_up(location_path: str) -> None:
    file_list = os.listdir(location_path)

    for file_path in file_list:
        os.remove(location_path + file_path)
        logger.debug(f"removed file: {location_path + file_path}")


def create_save_location(save_location: str) -> None:
    os.makedirs(save_location, exist_ok=True)


def save_file(file, save_location: str) -> None:
    with open(save_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)


@app.post("/upload-image/")
def upload_image(file: UploadFile = File(...)):
    img_path = save_location + file.filename
    create_save_location(save_location)
    logger.info("creazione cartella completata")
    save_file(file, img_path)
    logger.info("salvataggio file completato")

    original_image = load_image(img_path)
    logger.info("caricamento immagine completato")
    process_image = preproces_image(original_image)
    logger.info("processamento immagine completato")
    classe, confidence = predict(process_image, MODEL)
    logger.info("predizione completata")

    return JSONResponse(
        content={
            "filename": file.filename,
            "message": {"class": classe, "confidence": float(confidence)},
        }
    )


if __name__ == "__main__":
    clean_up(save_location)
    logger.info("pulizia cartella completata")

    uvicorn.run(app, host="0.0.0.0", port=8000)

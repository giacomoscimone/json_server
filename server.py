import sys


sys.path.append("C:/Users/Alternanza/Documents/GitHub/alternanza")


import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, FileResponse
from io_utils import load_model, load_image, save_image
from image_utils import preproces_image, grayscale
from predictor import predict
from logger_utils import setuplog
from io_utility import create_save_location, clean_up, save_file
from constant_endpoint import PATH_UPLOAD, PATH_GRAYSCALE
from constant_path import MODEL_PATH, save_location, log_path
import logging

app = FastAPI()

MODEL = load_model(MODEL_PATH)

logger = logging.getLogger('my_logger')


@app.post(PATH_UPLOAD)
def upload_image(file: UploadFile = File(...)):
    logger.info("chiamata endpoint: " + PATH_UPLOAD)

    img_path = save_location + file.filename
    create_save_location(save_location)
    save_file(file, img_path)

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


@app.post(PATH_GRAYSCALE)
def convert_grayscale(file: UploadFile = File(...)):

    img_path = save_location + file.filename
    create_save_location(save_location)
    save_file(file, img_path)

    img = load_image(img_path)
    logger.info("immagine caricata")

    img_gray = grayscale(img)
    logger.info("immagine processata")

    save_image(img_gray, img_path)
    logger.info("immagine processata salvata")

    return FileResponse(img_path)


if __name__ == "__main__":
    setuplog(log_path)
    clean_up(save_location)

    uvicorn.run(app, host="0.0.0.0", port=8000)

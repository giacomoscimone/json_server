import sys
sys.path.append("C:/Users/Alternanza/Documents/GitHub/alternanza")
import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import shutil
import os
from  io_utils import print_prediction

import main as M

app = FastAPI()


@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):

    file_location = "C:/Users/Alternanza/Documents/GitHub/json_server/files/"
    os.makedirs(file_location, exist_ok=True)
    path = file_location + file.filename
    print(path)
    with open(path, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    print("Immagine copiata")
    predicted_class, prediction = M.main(path)
    print("immagine processata")
    return JSONResponse(
        content={
                    "filename": file.filename,
                    "message":print_prediction(predicted_class,prediction)
                }
    )

@app.get("/")
async def hello():
    return "Ciao"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
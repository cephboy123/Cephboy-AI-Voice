import os
from fastapi import FastAPI, UploadFile, File
import subprocess

app = FastAPI()
API_KEY = os.getenv("AIzaSyD-d6JxU3cgilYUEROIkejX7xVGGdohMo4")

@app.post("/clean")
async def clean(file: UploadFile = File(...)):
    # Code pour enlever le bruit et la musique
    return {"message": "Traitement Cephboy AI en cours..."}
  

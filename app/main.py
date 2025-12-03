from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# On sert les fichiers statiques depuis le dossier "static"
app.mount("/", StaticFiles(directory="static", html=True), name="static")

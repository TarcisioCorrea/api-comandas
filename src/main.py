from fastapi import FastAPI
from settings import HOST, PORT, RELOAD
import uvicorn

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run('main:app', host=HOST, port=int(PORT), reload=RELOAD)
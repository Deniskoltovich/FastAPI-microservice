import os

import uvicorn
from fastapi import FastAPI

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host=os.environ.get('APP_HOST'), port=int(os.environ.get('APP_PORT')))
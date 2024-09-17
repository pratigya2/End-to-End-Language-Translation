from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
@app.get('/index', response_class = HTMLResponse)
def index(request:Request):
    return templates.TemplateResponse("index.html", {"request":request})

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='127.0.0.1')
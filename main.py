from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn


app = FastAPI() #objeto
templates = Jinja2Templates(directory="templates") #mapeando para a pasta templates
static = Jinja2Templates(directory="static")    #mapeando para a pasta static ~eu acho~

@app.get("/")  #rota raiz,devolve a página index.html
def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request}) #usando a forma de procesamento do Jinja, diferente do visto antes

if __name__ == "__main__":
 uvicorn.run("main:app", port=8000, reload=True)

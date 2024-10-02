from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn

from models.produto_model import Produto


app = FastAPI() #objeto fastapi
templates = Jinja2Templates(directory="templates") #mapeando para a pasta templates
static = Jinja2Templates(directory="static")    #mapeando para a pasta static ~eu acho~

@app.get("/")  #rota raiz,devolve a página index.html
def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request}) #usando a forma de procesamento do Jinja, diferente do visto antes

#rota para cadastro.html
@app.get("/cadastro")
def get_cadastro(request: Request):
   return templates.TemplateResponse("cadastro.html", {"request": request})

#rota para post cadastro -> página que vai entrar quando o cadastro for submetido/enviado
@app.post("/post_cadastro")
def post_cadastro(request: Request,
                 nome:str = Form(...),
                 descricao:str = Form(...),
                 estoque:str = Form(...),
                 preco:str = Form(...)):
   produto = Produto(None, nome, descricao, estoque, preco)
   produto = produto_repo.inserir(produto)  #ainda não tem a conexão
   return RedirectResponse("/", 303)

if __name__ == "__main__":
 uvicorn.run("main:app", port=8000, reload=True)

from flask import Flask , render_template, request
from math import sqrt

#variavel app
app = Flask(__name__) #instanciando a biblioteca flask, pegando o nome da aplicaçao(main.py)

"""
criar uma rota - url
@approute("/nome da página que quero acessar")
def index() :  index pode ser qualquer nome da página
    return "ok"

app.run(port=80) - porta para acessar
http: - localhost/...  

http://localhost:1024
porta 80 é padrao para web.

debug=True: se tiver que trocar alguma coisa o codigo, ele já carregar auto.

ctrl+j : abre o terminal dentro do visual studio e esconde ou fecha o terminal. o terminal fica rodando o servidor mesmo se fechado

render_templade: retorna a página, render é renderizar a pagina. templade é a página.

tem que criar a rota antes do app.run

python main.py
"""

@app.route("/")
def index():
    return "Olá, mundo!"

@app.route("/pagina1/<string:nome>") #estou esperando que a pessoa passe o nome como parametro do tipo string
def pagina1(nome):
    return render_template("pagina1.html", nomePessoa=nome)

@app.route("/pagina2")#rota para acessar a página
def pagina2():
    return render_template("pagina2.html")

@app.post("/bhaskara")#para receber os dados
def bhaskara():
    a = float(request.form.get("a"))
    b = float(request.form.get("b"))
    c = float(request.form.get("c"))
    
    delta = b**2 - 4 * a * c
    
    if delta >= 0:
        x1 = (-b + sqrt(delta)) / 2 * a
        x2 = (-b - sqrt(delta)) / 2 * a
        return f"<h1>X1 = {x1} e X2 = {x2}</h1>"
    else:
        return "<h1>Não tem soluções para a equação!</h1>"
    
app.run(port=80, debug=True)
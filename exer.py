import requests
from flask import Flask
import pandas as pd
import openpyxl



link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
requisicao = requests.get(link)
tabela = pd.read_excel("Vendas - Dez.xlsx")
app = Flask(__name__)

print(tabela.columns)

#@app.route("/") #decorator -> diz qual site vai rodar, por ter o "/" ira rodar no site padrão: http://127.0.0.1:5000
#def hello_world(): #função
#    return "<p>Hello, World!</p>"

#@app.route("/douglasgomes") #decorator -> diz qual site vai rodar, por ter o "/" ira rodar no site padrão: http://127.0.0.1:5000
#def douglasgomes(): #função
#    return "<p>Douglas Gomes site 2!</p>"

#tranformando em API:

#@app.route("/") #decorator -> diz qual site vai rodar, por ter o "/" ira rodar no site padrão: http://127.0.0.1:5000
#def hello_world(): #função
#    return {"Name": "Douglas"}

#@app.route("/douglasgomes") #decorator -> diz qual site vai rodar, por ter o "/" ira rodar no site padrão: http://127.0.0.1:5000
#def douglasgomes(): #função
#    return {"how old are you?": "27", "What city do you live in?": "Rio das Pedras"}


#Testando com banco de dados:
@app.route("/") #decorator -> diz qual site vai rodar, por ter o "/" ira rodar no site padrão: http://127.0.0.1:5000
def faturamento(): #função
    faturamento = float(tabela["Valor Final"].sum())
    return {"Faturamento": faturamento}

@app.route("/vendas/produtos") #decorator -> diz qual site vai rodar, por ter o "/" ira rodar no site padrão: http://127.0.0.1:5000
def vendas_produto(): #função
    tabela_vendas_produtos = tabela[["Produto", "Valor Final"]].groupby("Produto").sum()
    dic_tabela_vendas_produtos = tabela_vendas_produtos.to_dict()
    return dic_tabela_vendas_produtos


@app.route("/vendas/produtos/<produto>") #decorator -> diz qual site vai rodar, por ter o "/" ira rodar no site padrão: http://127.0.0.1:5000
def expecifico(produto): #função
    tabela_vendas_produtos = tabela[["Produto", "Valor Final"]].groupby("Produto").sum()
    if produto in tabela_vendas_produtos.index:
        vendas_produto = tabela_vendas_produtos.loc[produto]
        dic_vendas_produtos = vendas_produto.to_dict()
        return dic_vendas_produtos
    else:
        return {produto: "Inexistente"}

app.run() #coloca o site no ar

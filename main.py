#Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
#Fazer login
#Importar a base de dados
#Cadastrar 1 produto
#Repetir para todos os produtos

import pyautogui as py
import time

py.PAUSE=0.5   
py.press("win")
py.write("chrome")
py.press("enter")
py.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
py.press("enter")
time.sleep(3)
py.click(x=784, y=416)
py.write("testedeautomacao@gmail.com")
py.press("tab")
py.write("umasenha qualquer")
py.click(x=952, y=569)
time.sleep(2)
py.press("enter")
#Base de dados dos produtos
#codigo,marca,tipo,categoria,preco_unitario,custo,obs
import pandas as pd

tabela=pd.read_csv("produtos.csv")

print(tabela)

#Cadastro de produto
for linha in tabela.index:
    py.click(x=708, y=284)

    codigo=tabela.loc[linha, "codigo"]
    py.write(str(codigo))

    py.press("tab")

    marca=tabela.loc[linha, "marca"]
    py.write(marca)

    py.press("tab")

    tipo=tabela.loc[linha, "tipo"]
    py.write(tipo)

    py.press("tab")

    categoria=str (tabela.loc[linha, "categoria"])
    py.write(categoria)

    py.press("tab")

    preco_unitario= str(tabela.loc[linha,"preco_unitario"])
    py.write(str(preco_unitario))

    py.press("tab")

    custo= str(tabela.loc[linha, "custo"])
    py.write(str(custo))

    py.press("tab")

    obs=str(tabela.loc[linha, "obs"])
    
    if obs !="nan":
        py.write(obs)
    
    py.press("tab")
    py.press("enter")
    py.sleep(1.5)

    py.scroll(5000)


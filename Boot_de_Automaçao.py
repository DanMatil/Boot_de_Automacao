# PASSA A PASSO
#1- entra no sistema da empresa
            #https://dlp.hashtagtreinamentos.com/python/intensivao/login
# INSTALAR BIBLIOTECA PYAUTOGUI
#2 - fazer login
#3 - importar base de dados
#4 - cadastrar 1 produto
#5 - repetir o processo de cadastro ate acabar
#===============================================================================



import pyautogui
import time

pyautogui.PAUSE = 0.5 #  AQUI DA UMA PAUSA DE 1 SEGUNDO EM CADA AÇAO DO PYAUTOGUI

# ABRIR NAVEGADOR (SAFARI)
pyautogui.hotkey( "command", "space")#clica em varias teclas
pyautogui.write("safari")#pyautogui.write -> escrever um texto
pyautogui.press("enter")#pyautogui.press -> pressionar 1 tecla do teclado

# ENTRAR NO SITE
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#DAR UMA PAUSA UM POUCO MAIOR (3 SEGUNDOS)
time.sleep(3)

# PASSO 2 - FAZER LOGIN
pyautogui.click(x=621, y=375)
pyautogui.write("daniel@matil.com.br")

# ESCREVE A SENHA
pyautogui.click(x=615, y=472)
pyautogui.write("Sua senha aqui")

# CLICAR NO BOTAO DE LOGAR
pyautogui.click(x=626, y=543)
pyautogui.press("enter")

# PASSO 3 - IMPORTAR A BASE DE DADOS
# install pandas
import pandas
tabela = pandas.read_csv("produtos.csv")#aqui eu cria a variavel tabela e informo pro pandas onde armazer a basede dados produtos.csv

# 4-  CADASTRAR UM PRODUTO
# PARA CADA LINHA AD MINHA TABELA
for linha in tabela.index:
    #1 - clica no campo produto
    pyautogui.click(x=633, y=260)

    # Codigo do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # MARCA
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # TIPO
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # CATEGORIA
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # PREÇO
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # CUSTO
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # OBS
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):#pandas verifica se a informacao esta vazia ou nao
        pyautogui.write(obs)
    pyautogui.press("tab")

    # ENVIA
    pyautogui.press("enter")
    #voltar ao inicio
    pyautogui.scroll(500)



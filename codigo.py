#automação de sistema com Python

# bibliotecas usadas pip install pyautogui pip install pandas openpyxl

# descrever o passo a passo da alimentação do sistema

# passo 1 entrar no sistema
# passo 2 login
# passo 3 abrir base de dados
# passo 4 cadastrar um ítem
# passo 5 repetir operação até acabar a lista de produtos



import pyautogui
import time
import pandas

# pyautogui.click
# pyautogui.write
# pyautogui.press
# pyautogui.hotkey

pyautogui.PAUSE = 0.5

# passo 1 entrar no sistema abrindo o navegador

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1.5)
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(1.5)

# passo 2 login no sistema
# clicar no botão direito

pyautogui.press("tab")
pyautogui.write("pythonautomacao@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhafacil")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2.5)

# passo 3 cadastrar produto
# variável
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

# passo 4 cadastrar um ítem


    #codigo
    pyautogui.press("tab")
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)

    #marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)

    #tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)

    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    #preco Unitatio
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco)

    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)

    #obs
    obs = str(tabela.loc[linha, "obs"])
    pyautogui.press("tab")
    if obs != "nan":
        pyautogui.write(obs)


    #enviar

    pyautogui.press("tab")
    pyautogui.press("enter")

    #voltar para o inicio da tela
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")         



# passo 5 repetir o processo e cadastrar toda a planilha

# for linha in tabela.index:    
   
















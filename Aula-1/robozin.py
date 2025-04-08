import pyautogui  # Automação de mouse, teclado e interações com a tela
import time       # Controle de tempo/pausas
import pandas as pd  # Leitura de arquivos e manipulação de dados
import os         # Para trabalhar com caminhos de arquivos

# Tempo padrão entre cada ação do pyautogui
pyautogui.PAUSE = 0.5

# Passo 1: Abrir o navegador 
print("Abrindo o navegador...")
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
time.sleep(2)

# Passo 2: Acessar o site 
print("Acessando o site da empresa...")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Passo 3: Fazer login 
print("Fazendo login no sistema...")
pyautogui.press("tab")
pyautogui.write("robozin@teste.com")
pyautogui.press("tab")
pyautogui.write("senhasupersegura")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

# Passo 4: Importar a base de dados 
print("Lendo a base de dados de produtos...")
caminho = os.path.join(os.path.dirname(__file__), "produtos.csv")
produtos = pd.read_csv(caminho)

# Passo 5: Cadastrar os produtos 
print("Iniciando o cadastro de produtos...")

for linha in produtos.index:
    print(f"\nCadastrando produto {linha + 1}/{len(produtos)}")

    # Capturar dados da linha atual
    codigo = str(produtos.loc[linha, "codigo"])
    marca = str(produtos.loc[linha, "marca"])
    tipo = str(produtos.loc[linha, "tipo"])
    categoria = str(produtos.loc[linha, "categoria"])
    preco_unitario = str(produtos.loc[linha, "preco_unitario"])
    custo = str(produtos.loc[linha, "custo"])
    obs = str(produtos.loc[linha, "obs"])

    # Preenchendo os campos no formulário
    pyautogui.press("tab")
    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(marca)
    pyautogui.press("tab")
    pyautogui.write(tipo)
    pyautogui.press("tab")
    pyautogui.write(categoria)
    pyautogui.press("tab")
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    pyautogui.write(custo)
    pyautogui.press("tab")
    
    # Escreve observações, se houver
    if not pd.isna(produtos.loc[linha, "obs"]):
        pyautogui.write(obs)
    
    # Envia o formulário
    pyautogui.press("tab")
    pyautogui.press("enter")
    print("Produto cadastrado com sucesso!")

    # Voltar ao topo da página
    pyautogui.scroll(5000)

print("\nCadastro de todos os produtos finalizado com sucesso!")
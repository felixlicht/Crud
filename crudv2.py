'''
carregar_dados e salvar_dados
Funções para carregar dados de arquivos .json
Exemplo: usuarios.json e livros.json
Que devem ser passadas como parametros para leitura e escrita
'''
import json
import os
ARQUIVO_USUARIOS = "usuarios.json"
ARQUIVO_LIVROS   = "livros.json"

#Funções de Escrita e Leitura de dados
def carregar_dados(arquivo):
    if os.path.exists(arquivo):    
        with open(arquivo, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}      

def salvar_dados(arquivo, dados):
    try:
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        return True
    except FileNotFoundError:
        print("Arquivo para salvar não encontrado.")
        return False

def iniciar():
    while True:
        print("Menu de Seleção ")
        print("1 - Fazer login ")
        print("2 - Cadastrar Usuario ")
        print("0 - Fechar Menu ")
        
        escolha = input("Escolha o menu: ")
        pula_linhas()
        
        if   escolha == "1": 
            if login():
                menu ()
        elif escolha == "2": cadastrar_usuario()
        elif escolha == "0":break
        else:
            print("Opcao Invalida, tente novamente\n ")


def pula_linhas():
    print("\n")

#Funções de login e cadastro
def login():
    carregar_dados(ARQUIVO_USUARIOS)
    usuarios = carregar_dados(ARQUIVO_USUARIOS)
    print("MENU DE LOGIN ")
    username = input("Usuario: ")
    senha    = input("Senha:   ")
    if not username or not senha:
        print ("Usuario ou Senhas - Obrigatorios \n")
        return
    
    if usuarios.get(username) == senha:
        print("login com sucesso \n")
        return True
    else:
        print("Usuario ou Senha incorreta \n")
        return False
    
def cadastrar_usuario():
    #carregar_dados(ARQUIVO_USUARIOS)
    print("MENU DE CADASTROS DE USUARIOS ")
    usuarios = carregar_dados(ARQUIVO_USUARIOS)
    username = input("Digite o Usuario: ")
    senha    = input("Digite a Senha de Usuario: ")
    
    if (not username) or (not senha): #verifica se o usuario ou senha estão vazios
        print("Usuario ou Senha invalidos\n ")
        return
    if username in usuarios: #verifica se o nome de usuario já está sendo utilizado
        print("Usuario já existe \n")
        return

    usuarios[username] = senha
    salvar_dados(ARQUIVO_USUARIOS, usuarios)
    
    print("Usuario criado com sucesso!\n ")


#Usuarios só terão acesso a estas funções após completar todas as estapas de cadastro e login
def menu():
    livros = carregar_dados(ARQUIVO_LIVROS)
    while True:
        print("1 - Cadastrar Livros ")
        print("2 - Listar Livros ")
        print("3 - Atualizar Livros ")
        print("4 - Remover Livros")
        print("0 - Cancelar ")
        
        escolha = input("Escolha o menu: ")
        pula_linhas()
        if   escolha == "1": cadastrar_livros(livros)
        elif escolha == "2": listar_livros(livros)
        elif escolha == "3": atualizar_livros(livros)
        elif escolha == "4": remover_livros(livros)
        elif escolha == "0": break
        else: print("Menu invalido \n")
    
def cadastrar_livros(livros):
    #ivros{ ID Titulo; ISBN; Editora; Descrição; Genero }
    #Depois criar regra para não poder cadastrar mais de 1
    titulo    = input("Informe o Titulo: ")
    isbn      = input("Informe o ISBN: ")
    autor     = input("Informe o Autor(a): ")
    #gera automatico, para não ter de ficar digitando
    editora   = "Lorem Ipsum"
    genero    = "dolor sit amet" 
    descricao = "consectetur adipiscing elit"
    ano       = "2025"
    try:
        custo  = float(input("Informe o Custo: "))
        venda  = float(input("Informe a Venda: "))
    except ValueError:
        print("Valores Invalidos \n")
        return
    nova_id = len(livros) + 1
    livros[nova_id] ={
        "Titulo" : titulo,
        "Isbn"   : isbn,
        "Autor"  : autor,
        "Custo"  : custo,
        "Venda"  : venda,
        "Editora": editora,
        "Genero" : genero,
        "Descricao" : descricao,
        "Ano": ano
    }
    print(livros)
    if(salvar_dados(ARQUIVO_LIVROS, livros)):
        print("Livro Cadastrado com Sucesso\n ")
    else:print("Não foi possível salvar o arquivo! \n")
    

def listar_livros(livros):
    print("\nMENU DE CATÁLOGO DE LIVROS ")
    for id, info in livros.items():
        print(f"ID : {id} \n"
              f"Titulo : {info['Titulo']} \n"
              f"Isbn : {info['Isbn']}  \n"
              f"Autor(a) : {info['Autor']} \n"
              f"Custo : {info['Custo']:.2f}\n"
              f"Venda : {info['Venda']:.2f} \n"
              f"Editora : {info['Editora']} \n"
              f"Genero : {info['Genero']} \n"
              f"Descricao : {info['Descricao']} \n"
              f"Ano : {info['Ano']} \n"
              )

def atualizar_livros(livros):
    print("\nMENU DE ATUALIZAÇÃO DE LIVROS ")
    isbn   = input("Digite a ISBN do produto para atualizar: ")

    for id, info in livros.items():
        if info['Isbn'] == isbn:
            titulo    = input("Informe o Titulo: ")
            isbn      = input("Informe o ISBN: ")
            autor     = input("Informe o Autor(a): ")
            #gera automatico, para não ter de ficar digitando
            editora   = "Lorem Ipsum"
            genero    = "dolor sit amet" 
            descricao = "consectetur adipiscing elit"
            ano       = "2025"
            try:
                custo  = float(input("Informe o Custo: "))
                venda  = float(input("Informe a Venda: "))
            except ValueError:
                print("Valores Invalidos \n")
                return

    livros[id] ={
        "Titulo" : titulo,
        "Isbn"   : isbn,
        "Autor"  : autor,
        "Custo"  : custo,
        "Venda"  : venda,
        "Editora": editora,
        "Genero" : genero,
        "Descricao" : descricao,
        "Ano": ano
    }
    if(salvar_dados(ARQUIVO_LIVROS, livros)):
        print("Livro Atualizado com sucesso \n")
    else:
        print("Nao foi possivel atualizar o livro \n")
    

def remover_livros(livros):
    print("\nMENU DE EXCLUSÃO DE LIVROS ")
    #salvar_dados(ARQUIVO_LIVROS, livro)
    pass
    
iniciar()

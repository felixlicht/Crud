"""
carregar_dados e salvar_dados
Funções para carregar dados de arquivos .json
Exemplo: usuarios.json e livros.json
Que devem ser passadas como parametros para leitura e escrita
"""

import json
import os

ARQUIVO_USUARIOS = "usuarios.json"
ARQUIVO_LIVROS = "livros.json"


# Funções de Escrita e Leitura de dados
def carregar_dados(arquivo):
    '''
        Verifica se o arquivo existe no caminho
        Caso exista, retorna o arquivo Json
    '''
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}


def salvar_dados(arquivo, dados):
    '''
        Tenta abrir o arquivo json
        Caso exista, retorna True
    '''
    try:
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        return True
    except FileNotFoundError:
        print("Arquivo para salvar não encontrado.")
        return False


def iniciar():
    '''
        Primeiro Menu do Sistema
        Utilizado para fazer login
        Enquanto verdadeiro, o Menu ficar aberto
    '''
    while True:
        print("Menu de Seleção ")
        print("1 - Fazer login ")
        print("2 - Cadastrar Usuario ")
        print("0 - Fechar Menu ")

        escolha = input("Escolha o menu: ")
        pula_linhas()

        if escolha == "1":
            if login():
                menu()
        elif escolha == "2":
            cadastrar_usuario()
        elif escolha == "0":
            break
        else:
            print("Opcao Invalida, tente novamente\n ")


def pula_linhas():
    '''
        Auto Explicativo: Pula Linhas
    '''
    print("\n")


# Funções de login e cadastro
def login():
    '''
        Função que permite o usuário
        - Fazer Login
    '''
    carregar_dados(ARQUIVO_USUARIOS)
    usuarios = carregar_dados(ARQUIVO_USUARIOS)
    print("MENU DE LOGIN ")
    username = input("Usuario: ")
    senha = input("Senha:   ")
    if not username or not senha:
        print("Usuario ou Senhas - Obrigatorios \n")
        return

    if usuarios.get(username) == senha:
        print("login com sucesso \n")
        return True
    else:
        print("Usuario ou Senha incorreta \n")
        return False


def cadastrar_usuario():
    '''
        Permite o Usuário de Cadastrar
        Caso não haja um login com o mesmo login 
    '''
    # carregar_dados(ARQUIVO_USUARIOS)
    print("MENU DE CADASTROS DE USUARIOS ")
    usuarios = carregar_dados(ARQUIVO_USUARIOS)
    username = input("Digite o Usuario: ")
    senha = input("Digite a Senha de Usuario: ")

    if (not username) or (not senha):  # verifica se o usuario ou senha estão vazios
        print("Usuario ou Senha invalidos\n ")
        return
    if username in usuarios:  # verifica se o nome de usuario já está sendo utilizado
        print("Usuario já existe \n")
        return

    usuarios[username] = senha
    salvar_dados(ARQUIVO_USUARIOS, usuarios)

    print("Usuario criado com sucesso!\n ")


# Usuarios só terão acesso a estas funções após completar todas as estapas de cadastro e login
def menu():
    '''
        Segundo Menu
        Usuário só terá acesso após fazer o login
    '''
    livros = carregar_dados(ARQUIVO_LIVROS)
    while True:
        print("1 - Cadastrar Livros ")
        print("2 - Listar Livros ")
        print("3 - Atualizar Livros ")
        print("4 - Remover Livros")
        print("0 - Cancelar ")

        escolha = int(input("Escolha o menu: \n"))

        options = {
            1: cadastrar_livros,
            2: listar_livros,
            3: atualizar_livros,
            4: remover_livros,
        }

        if escolha not in options.keys():
            print("Menu invalido \n")
            continue 

        options[escolha](livros)


def cadastrar_livros(livros):
    '''
        Permite o usuário cadastrar um livro novo
        Desde que o ISBN informado não esteja cadastrado anteriormente
    '''
    titulo = input("Informe o Titulo: ")
    isbn_nova = input("Informe o ISBN: ").strip()

    for _,info in livros.items(): #como livros.items() retorna uma tupla, é preciso desempacotar o dic
        if info["Isbn"] == str(isbn_nova):
            print("ISBN ja cadastrado\n ")
            return

    autor = input("Informe o Autor(a): ")
    # gera automatico, para não ter de ficar digitando
    editora = "Lorem Ipsum"
    genero = "dolor sit amet"
    descricao = "consectetur adipiscing elit"
    ano = "2025"
    try:
        custo = float(input("Informe o Custo: "))
        venda = float(input("Informe a Venda: "))
    except ValueError:
        print("Valores Invalidos \n")
        return
    nova_id = str(max([int(i) for i in livros.keys()], default=0) + 1)
    livros[nova_id] = {
        "Titulo": titulo,
        "Isbn": isbn_nova,
        "Autor": autor,
        "Custo": custo,
        "Venda": venda,
        "Editora": editora,
        "Genero": genero,
        "Descricao": descricao,
        "Ano": ano,
    }
    if salvar_dados(ARQUIVO_LIVROS, livros):
        print("Livro Cadastrado com Sucesso\n ")
    else:
        print("Não foi possível salvar o arquivo! \n")


def listar_livros(livros):
    '''
        Permite o usuário listar todos os livros já cadastrados
    '''
    print("\nMENU DE CATÁLOGO DE LIVROS ")
    for indice, info in livros.items():
        print(
            f"ID : {indice} \n"
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
    '''
        Pemite a atualização dos livros já cadastrados
        Usa ISBN como busca
    '''
    print("\nMENU DE ATUALIZAÇÃO DE LIVROS ")
    isbn_busca = input("Digite a ISBN do livro para atualizar: ").strip()

    for indice, info in livros.items():
        if info["Isbn"] == isbn_busca:
            print(f"\nLivro encontrado: {info['Titulo']}\n") 
            titulo = input("Informe o Título: ")
            isbn = input("Informe o novo ISBN: ")
            autor = input("Informe o Autor(a): ")
            editora = "Lorem Ipsum"
            genero = "dolor sit amet"
            descricao = "consectetur adipiscing elit"
            ano = "2025"
            try:
                custo = float(input("Informe o Custo: "))
                venda = float(input("Informe a Venda: "))
            except ValueError:
                print("Valores inválidos.\n")
                return

            livros[indice] = {
                "Titulo": titulo,
                "Isbn": isbn,
                "Autor": autor,
                "Custo": custo,
                "Venda": venda,
                "Editora": editora,
                "Genero": genero,
                "Descricao": descricao,
                "Ano": ano,
            }

            if salvar_dados(ARQUIVO_LIVROS, livros):
                print("Livro atualizado com sucesso.\n")
            else:
                print("Não foi possível salvar as alterações.\n")
            break
    else:
        print("ISBN não encontrada.\n")


def remover_livros(livros):
    '''
        Pemite Remover um livro
        Utiliza ISBN com base
    '''
    print("\nMENU DE EXCLUSÃO DE LIVROS ")
    isbn_busca = input("Digite o ISNB do livro que deseja remover: ").strip()
    if not isbn_busca:
        print("ISBN invalido\n ")
        return
    for indice, info in livros.items():
        if info["Isbn"] == isbn_busca:
            livros.pop(indice)
            if salvar_dados(ARQUIVO_LIVROS, livros):
                print(f"Livro ID {indice} Titulo {info['Titulo']} Removido com sucesso\n")
            else:
                print("Erro ao salvar\n")
            break
    else:
        print("ISBN nao encontrada \n")


iniciar()

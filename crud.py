import os
encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

def cadastrar_livros ():
    #id - titulo - estoque - custo - venda
    print("-----Menu de Cadastro de Livros -----\n")
    titulo = input("Informe o Titulo do Livro: ")
    try:
        quantidade = int(input("Informe a quantidade: "))
        try:
            custo  = float(input("Informe o Custo Unitario do Livro: "))
            venda  = float(input("Informe o Valor de Venda Unitario do Livro: "))
        except ValueError:
            print("O preco deve ser um valor REAL\n")
            return 
    except ValueError:
        print("A quantidade do produto deve ser um Valor INTEIRO\n ")
        return
    #Add valores ao dicionario
    novoId = max(livros_cadastrados.keys(), default=0) +1
    livros_cadastrados[novoId] = {'Titulo':titulo, 'Estoque':quantidade, 'Custo':custo, 'Venda':venda}
    #Salva todo o cadastro em um txt
    try:
        with open("arquivo.txt", "w") as f:
            for id, info in livros_cadastrados.items():
                print(f"ID {id} - Titulo {info['Titulo']}")
                f.write(f"ID {id} - {info['Titulo']} - Estoque {info['Estoque']} - Custo {info['Custo']} - Venda {info['Venda']} \n")
        print(f"{f} Savo com sucesso! ")
    except FileExistsError:
        print("O arquivo já existe\n")
    print (f"Novo Livro: {titulo} cadastrado com sucesso! \n")
    
def listar_livros ():
    #id - titulo - estoque - custo - venda
    print("----- Menu de Catalogo de Livros -----\n")
    if len(livros_cadastrados)>=1:
        for id, info in livros_cadastrados.items():
            print(f"ID {id} - Titulo {info['Titulo']} - Estoque {info['Estoque']} - Custo {info['Custo']} - Venda {info['Venda']}")
        quebraLinhas()
    else:
        print("Sem livros no Catalogo\n ")
    
def atualizar_livros ():
    #id - titulo - estoque - custo - venda
    print("----- Menu de Atualizar Catalago de Livros -----  \n")
    if len(livros_cadastrados) >=1:
        try:
            id = int(input("Informe a ID do livro para atualizar: "))
            if id in livros_cadastrados:
                livros_cadastrados[id]['Titulo'] = input("Informe o novo Titulo: ")
                try:
                    livros_cadastrados[id]['Estoque'] = int(input("Informe o estoque atualizado: "))
                    livros_cadastrados[id]['Custo']   = float(input("Informe o Custo atualizado: "))
                    livros_cadastrados[id]['Venda']   = float(input("Informe a Venda atualizada: "))
                    quebraLinhas()
                except ValueError:
                    print("Valores Digitados Incorretos\n ")
                    return 
            #Salva todo o cadastro em um txt
            #Este código pode ser usado como função
            try:
                with open("arquivo.txt", "w") as f:
                    for id, info in livros_cadastrados.items():
                        print(f"ID {id} - Titulo {info['Titulo']}")
                        f.write(f"ID {id} - {info['Titulo']} - Estoque {info['Estoque']} - Custo {info['Custo']} - Venda {info['Venda']} \n")
                print(f"{f} Savo com sucesso! ")
            except FileExistsError:
                print("O arquivo já existe\n")

            print(f"Dados Atualizados:  ID {id} - Titulo - {livros_cadastrados[id]['Titulo']} - Estoque - {livros_cadastrados[id]['Estoque'] } - Custo - {livros_cadastrados[id]['Custo']} - Venda - {livros_cadastrados[id]['Venda']}\n ")
        except ValueError:
            print("ID Invalida\n ")
            return
    else:
        print("Nao ha livros para atualizar\n ")
        return

def remover_livros():
    #id - titulo - estoque - custo - venda
    print("----- Menu de Remover  Livros -----  \n")
    try:
        id = int(input("Informe o ID do livro para ser removido: "))
        if id in livros_cadastrados:
            remover = livros_cadastrados.pop(id)
            print(f"Livro '{remover['Titulo']}' Removido com Sucesso \n")
        else:
            print("ID não localizada\n ")
    except ValueError:
        print("ID Invalida\n ")
        return

def quebraLinhas():
    print("\n")

def menu ():
    while True:
        try:
            menu = int(input("Selecione o menu:\n 1 - Listar Livros\n 2 - Cadastrar Livros\n 3 - Atualizar Livros\n 4 - Remover Livros\n "))
        except ValueError:
            print("Menu Invalido\n ")
            break
        if menu == 1:
            listar_livros()
        elif menu == 2:
            cadastrar_livros()
        elif menu == 3:
            atualizar_livros()
        elif menu == 4:
            remover_livros()
        else:
            print("Opcao incorreta de Menu\n ")

#Gera o primeiro Dicionario de Livros
#id - titulo - estoque - custo - venda 
livros_cadastrados = {
    1:{'Titulo': 'Harry Potter: E a Pedra Filosofal','Estoque': 10,'Custo': 10.5,'Venda' : 14.9},
    2:{'Titulo': 'Harry Potter: E a Camara Secreta','Estoque': 20,'Custo': 11.5,'Venda' : 15.9},
    3:{'Titulo': 'Harry Potter: E o Prisioneiro de Askabahn','Estoque': 30,'Custo': 12.5,'Venda' : 16.9},
    4:{'Titulo': 'Harry Potter: E o Calice de Fogo','Estoque': 40,'Custo': 13.5,'Venda' : 17.9},
    5:{'Titulo': 'Harry Potter: E E a ordem da Fenix','Estoque': 50,'Custo': 14.5,'Venda' : 18.9},
    6:{'Titulo': 'Harry Potter: E o Enigma do Principe','Estoque': 60,'Custo': 15.5,'Venda' : 19.9},
    7:{'Titulo': 'Harry Potter: E as Reliquias da Morte pt-1','Estoque': 70,'Custo': 16.5,'Venda' : 20.9},
    8:{'Titulo': 'Harry Potter: E as Reliquias da Morte pt-2','Estoque': 80,'Custo': 17.5,'Venda' : 20.9}    
}

menu()


#gergrgrgfergre
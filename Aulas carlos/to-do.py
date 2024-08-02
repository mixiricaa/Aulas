import os

tarefas = {}

def adicionar_tarefas(tarefas):
    print("--Adicionar Tarefas--")
    print("Escreva a tarefa que deseja adicionar")
    descricao = input("--> ")
    id_tarefa = len(tarefas) + 1 
    tarefas[id_tarefa] = descricao
    print("Tarefa adicionada!")
    os.system("pause")
    os.system("cls")

def editar_tarefas(tarefas):
    print("--Editar Tarefas--")
    if not tarefas:
        print("Nenhuma tarefa para editar.")
        os.system("pause")
        os.system("cls")
        return
    
    print("Tarefas existentes:")
    for id_tarefa, descricao in tarefas.items():
        print(f"{id_tarefa} - {descricao}")
    
    id_editar = int(input("Qual tarefa deseja editar? \n--> "))
    if id_editar in tarefas:
        nova_descricao = input("Edite a tarefa: ")
        tarefas[id_editar] = nova_descricao
        print("Tarefa editada!")
    else:
        print("Tarefa não encontrada.")
    
    os.system("pause")
    os.system("cls")

def excluir_tarefas(tarefas):
    print("--Excluir Tarefa--")
    if not tarefas:
        print("Nenhuma tarefa para excluir.")
        os.system("pause")
        os.system("cls")
        return
    
    print("Tarefas existentes:")
    for id_tarefa, descricao in tarefas.items():
        print(f"{id_tarefa} - {descricao}")
    
    id_excluir = int(input("Qual tarefa deseja excluir? \n--> "))
    if id_excluir in tarefas:
        del tarefas[id_excluir]
        print("Tarefa excluída!")
    else:
        print("Tarefa não encontrada.")
    
    os.system("pause")
    os.system("cls")

s = 1

while s == 1:
    print("--To-do--")
    print("1 - Adicionar tarefa")
    print("2 - Editar tarefa")
    print("3 - Excluir tarefa")
    print("4 - Sair")
    escolha = int(input("--> "))
    os.system("cls")

    if escolha == 1:
        adicionar_tarefas(tarefas)
    elif escolha == 2:
        editar_tarefas(tarefas)
    elif escolha == 3:
        excluir_tarefas(tarefas)
    elif escolha == 4:
        print("Saindo...")
        break
    else:
        print("Ação invalida!")
        os.system("pause")
        os.system("cls")

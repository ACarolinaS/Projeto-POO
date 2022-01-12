from todo_class import ToDoList, Printer
import datetime
import os
from time import sleep

clear = lambda: os.system('cls')

lista = ToDoList()

while True:

    print('::: Bem-vindo(a) a sua Agenda de Tarefas')
    option = int(input(f'''Digite a opção desejada:
    1 - Adicionar nova tarefa
    2 - Alterar status de uma tarefa
    3 - Remover uma tarefa
    4 - Procurar tarefa por data de entrega
    5 - Visualizar todas as tarefas
    6 - Sair 
    
    Opção: '''))
    
    if option == 6:
        print('Agenda encerrada.')
        break
        
    elif option == 1:
        lista.add_task()
        sleep(3)
        clear()
        
    elif option == 2:
        title = input('Qual o título da tarefa que deseja marcar como concluído? ').capitalize()
        lista.finish_task(title)
        sleep(3)
        clear()
    
    elif option == 3:
        title = input('Qual o título da tarefa que deseja remover? ').capitalize() 
        lista.remove_task(title)
        sleep(3)
        clear()
        
    elif option == 4:
        date = input('Qual a data de entrega da tarefa que deseja buscar (DD/MM/YYYY) [hoje/amanhã]: ').lower() 
        
        if date == 'hoje':
            date = datetime.datetime.now().strftime('%d/%m/%Y')
        elif date == 'amanhã':
            date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')

        lista.view_tasks(date)
        sleep(4)
        clear()
        
    elif option == 5:
        lista.view_all_tasks()
        sleep(4)
        clear()

    else:
        print(msg = 'Opção inválida.\n')
from tempfile import NamedTemporaryFile
import shutil
import csv
import datetime

def create_csv(filename):
    pass

def add_to_csv(filename, row):
    pass

def check_task_csv(filename, date):
    pass

def update_tasklist_on_csv(filename, title, type_of_modification='status'):
    
    replace_file = True
    tempfile = NamedTemporaryFile(mode='w', delete=False, newline='', encoding='utf-8-sig')

    with open(filename, 'r') as csvfile, tempfile:
        reader = csv.reader(csvfile, delimiter=';')
        writer = csv.writer(tempfile, delimiter=';')
        for row in reader:
            try:
                if type_of_modification == 'status':
                    if row[0] == title:
                        print('atualizando tarefa', row[0])
                        row[-1] = 'concluída'
                    writer.writerow(row)

                elif type_of_modification == 'remove':
                    if row[0] != title:
                        writer.writerow(row)

                else:
                    replace_file = False
                    print('modificação não reconhecida')

            except:
                pass

    if replace_file:
        shutil.move(tempfile.name, filename)
        print('Arquivo atualizado com sucesso.')

def insert_valid_date():
    try:
        date = input('Data de entrega (DD/MM/YYYY): ').split('/')
        day, month, year = date
    except:
        print('Data inválida. Tente novamente.')
        return insert_valid_date()
    return day, month, year
class ToDoList:

    dict_of_tasks = {}
    filename = 'tasks.csv'
    create_csv(filename)

    def __init__(self):
        pass

    def add_task(self):
        title = input('Título: ').capitalize()
        if title not in self.dict_of_tasks:
            description = input('Descrição: ')
            date = insert_valid_date()
            day, month, year = date
            status = 'pendente'

            task = [title, description, day, month, year, status]
            self.dict_of_tasks.update(
                {title : {
                    'description': description, 
                    'day': day,
                    'month': month,
                    'year': year,
                    'status': status
                    }
                })
            add_to_csv('tasks.csv', task)
            print('Tarefa adicionada com sucesso.')

        else:
            print('Tarefa já existe.')

    def finish_task(self, title):
        try:
            self.dict_of_tasks[title]['status'] = 'concluída'
            update_tasklist_on_csv(self.filename, title, type_of_modification = 'status')
        except KeyError as e:
            print(f'A tarefa {title} não existe. - {e}')

    def view_tasks(self, date):
        check_task_csv(self.filename, date)

    def remove_task(self, title):
        if title in self.dict_of_tasks:
            del self.dict_of_tasks[title]
            update_tasklist_on_csv(self.filename, title, type_of_modification = 'remove')
        else:
            print(f'A tarefa {title} não existe.')
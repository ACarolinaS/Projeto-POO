from tempfile import NamedTemporaryFile
import shutil
import csv
import datetime

def create_csv(filename):
    with open(filename, 'w', encoding='utf-8-sig', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['título', 'descrição', 'dia', 'mês', 'ano', 'status'])

def add_to_csv(filename, row):
    with open(filename, 'a', encoding='utf-8-sig', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(row)

def check_task_csv(filename, date):
    print(f'As tarefas para o dia {date} é/são: \n')
    no_tasks = True
    day, month, year = date.split('/')

    with open(filename, 'r', encoding='utf-8-sig') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in csvreader:
            if [row[2], row[3], row[4]] == [day, month, year]:
                print(row[0])
                no_tasks = False

    if no_tasks:
        print(f'Não há tarefas para o dia {date}.')

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
            
    def view_all_tasks(self):
        for tarefa in self.dict_of_tasks:
            print(f'Tarefa: {tarefa}')
            for key, value in self.dict_of_tasks[tarefa].items():
                print(f'    {key}: {value}')
def create_csv(filename):
    pass

def add_to_csv(filename, row):
    pass

def check_task_csv(filename, date):
    pass

def update_tasklist_on_csv(filename, title, type_of_modification='status'):
    pass

def insert_valid_date():
    pass

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
            print(msg = 'Tarefa adicionada com sucesso.', color = 'GREEN')

        else:
            print(msg = 'Tarefa já existe.', color = 'BOLD')

    def finish_task(self, title):
        try:
            self.dict_of_tasks[title]['status'] = 'concluída'
            update_tasklist_on_csv(self.filename, title, type_of_modification = 'status')
        except KeyError as e:
            print(msg = f'A tarefa {title} não existe. - {e}', color = 'BOLD')

    def view_tasks(self, date):
        check_task_csv(self.filename, date)

    def remove_task(self, title):
        if title in self.dict_of_tasks:
            del self.dict_of_tasks[title]
            update_tasklist_on_csv(self.filename, title, type_of_modification = 'remove')
        else:
            print(msg = f'A tarefa {title} não existe.', color = 'RED')
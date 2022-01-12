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
        p.print(msg = f'Não há tarefas para o dia {date}.', color = 'BLUE')

def update_tasklist_on_csv(filename, title, type_of_modification):
    
    replace_file = True
    tempfile = NamedTemporaryFile(mode='w', delete=False, newline='', encoding='utf-8-sig')

    with open(filename, 'r', newline='', encoding='utf-8-sig') as csvfile, tempfile:
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
        p.print(msg = 'Arquivo atualizado com sucesso.', color = 'GREEN')

def insert_valid_date():
    try:
        date = input('Data de entrega (DD/MM/YYYY): ').split('/')
        day, month, year = date
    except:
        p.print(msg = 'Data inválida. Tente novamente.', color = 'BOLD')
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
            p.print(msg = 'Tarefa adicionada com sucesso.', color = 'GREEN')

        else:
            p.print(msg = 'Tarefa já existe.', color = 'BOLD')

    def finish_task(self, title):
        try:
            self.dict_of_tasks[title]['status'] = 'concluída'
            update_tasklist_on_csv(self.filename, title, type_of_modification = 'status')
        except KeyError as e:
            p.print(msg = f'A tarefa {title} não existe. - {e}', color = 'BOLD')

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

class Printer:
    _colors_ = {
        "RED": "\033[1;31m",
        "GREEN": "\033[0;32m",
        "YELLOW": "\033[0;93m",
        "BLUE": "\033[1;34m",
        "CYAN": "\033[1;36m",
        "RESET": "\033[0;0m",
        "BOLD": "\033[;1m",
        'MAGENTA': "\033[1;35m",
        "MAGENTAC": "\033[1;95m",
        "REVERSE": "\033[;7m"
    }
    
    def _get_color_(self, key):
        """Gets the corresponding color ANSI code... """
        try:
            return self._colors_[key]
        except:
            return self._colors_["REVERSE"]
        
    def print(self, msg , color="REVERSE"):
        """Main print function..."""

        color = self._get_color_(key=color)

        print("{}{}{}".format(color, msg, self._colors_["REVERSE"]))

p = Printer()
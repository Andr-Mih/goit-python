from os import error, name, supports_bytes_environ
import phone_book as pb
import models as md
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import update

Base = declarative_base()

engine = create_engine('sqlite:///personal_helper.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base.metadata.create_all(engine)
Base.metadata.bind = engine

# tuple with commands words
EXIT_COMMANDS = ("good bye", "close", "exit", "bye")
FIND_COMMANDS = ("find",)
EDIT_COMMANDS = ("edit",)
BIRTHDAY_COMMANDS = ("birthday",)
SELECT_COMMANDS = ("select", "sel")
ADD_COMMANDS = ("add", "+")
DELETE_COMMANDS = ("delete", "del", "-",)
GREETING_COMMANDS = ("hello", "alloha",)
SHOW_ALL_COMMANDS = ("show all", "show")
HELP_COMMANDS = ("help",)
CURRENT_MODES = {'1': 'PhoneBook',
                 '2': 'NotesBook', '3': 'SortFolder'}
CURRENT_MODE = ''
CURRENT_RECORD = None
CURRENT_ID = None





def input_name():
    while True:
        result = input('Contact name (required): ')
        if len(result) >= 3:
            return pb.Name(result)
        else:
            print("Name must have 3 or more characters!!")


def input_phone():
    while True:
        try:
            phone = pb.Phone(input('Contact phone (required): '))
            break
        except ValueError as e:
            print(e)
    return phone


def input_birthday():
    while True:
        try:
            birthday = pb.Birthday(
                input('Contact birthday "MM-DD" format (optional): '))
            break
        except ValueError as e:
            print(e)
    return birthday


def input_email():
    while True:
        try:
            email = pb.Email(input('Contact email (optional): '))
            break
        except ValueError as e:
            print(e)
    return email


#def input_address():
    #return pb.Address(input('New address: '))








def add_contact(*args):

    

    nam = input_name()

    #address = pb.Address(input('Contact address (optional): '))

    phone = input_phone()

    birthd = input_birthday()

    emal = input_email()
    print(nam.value)
    record = pb.Record(nam, phone, birthd, emal)
    
    new_user = md.User(name = nam.value, email = emal.value, birthday = birthd.value)
    new_phon = md.Phone(phone = phone.value, user = new_user)
    
    confirm = input(
        f'Add record {record} to address book (y/n)?: ')
    if confirm.lower() == 'y':
        session.add(new_user)
        session.add(new_phon)
        session.commit()


def phone_add(*args):
    if CURRENT_MODE == '1':
        user_i = input('Enter the user id for add phone: ')
        phone = input_phone()
        new_phon = md.Phone(phone = phone.value, user_id = user_i)
    confirm = input(
        f'Add phone {phone.value} to user with id = {user_i} (y/n)?: ')
    if confirm.lower() == 'y':
        session.add(new_phon)
        session.commit()

# commands functions


def add_command(*args):
    if CURRENT_MODE == '1'and args[0] == '':
        add_contact()
    elif CURRENT_MODE == '1' and args[0] == 'phone':
        phone_add()
    





def greeting_command(*args):
    print(f'in greeting_command')


def show_all_command(*args):
    if CURRENT_MODE == '1':
        for person in session.query(md.User).all():
            print(person.id, person.name, person.email, person.birthday)
        
    else:
        print(CURRENT_RECORD)

    
def edit_command(*args):

    if CURRENT_MODE == '1':
        param = input('Enter the id record for edit: ')
        param1 = input('Enter the record: ')
        param = f'{param}'
        if param1 == 'name':
            name = input('Enter the new name: ')
            session.query(md.User).filter(md.User.id == param).update({'name': name}, synchronize_session = 'fetch')
            session.commit()

        if param1 == 'email':
            email = input('Enter the new email: ')
            session.query(md.User).filter(md.User.id == param).update({'email': email}, synchronize_session = 'fetch')
            session.commit()

        if param1 == 'birthday':
            birthday = input('Enter the new birthday: ')
            session.query(md.User).filter(md.User.id == param).update({'birthday': birthday}, synchronize_session = 'fetch')
            session.commit()

        if param1 == 'phone':
            phone = input('Enter the new phone: ')
            session.query(md.Phone).filter(md.Phone.id == param).update({'phone': phone}, synchronize_session = 'fetch')
            session.commit()

        
    
    else:
        print(non_command())


def help_command(*args):
    if CURRENT_MODE == '1' or CURRENT_MODE == '2':
        print(f"""In {CURRENT_MODES[CURRENT_MODE]} mode.\n
            You can see all records in your {CURRENT_MODES[CURRENT_MODE]} - just type "Show" command \n
            You can add, delete or edit record in your AddressBook\n
            For adding type {ADD_COMMANDS} \n
            For deleting type {DELETE_COMMANDS} and specify the id record \n
            Before editing you must select record, type {SELECT_COMMANDS} and specify the id \n """)
    elif CURRENT_MODE == '3':
        print(f"""In {CURRENT_MODES[CURRENT_MODE]} mode.\n
            You can sort and organize your folders, just type command "sort" and PATH to folder\n """)
    else:
        print(f"""I can work in different mode.\n
            1. First - {CURRENT_MODES['1']} mode\n
            2. Second - {CURRENT_MODES['2']} mode\n
            3. Third - {CURRENT_MODES['3']} mode\n
            in each mode you can call command 'help' for more information""")


def delete_command(*args):
    if CURRENT_MODE == '1':
        param = input('Enter parameter: ')
        param = f'{param}'
        for ses in session.query(md.User).filter(md.User.id == param):
            session.delete(ses)
            session.commit()

   

def find_command(*args):
    if CURRENT_MODE == '1':
        while True:
            param = input('Enter parameter: ')
            if len(param) < 3:
                raise ValueError(f'Parameter must be 3 or more symbol')
            break
        if param.isalpha():
            param = f'%' + str(param) + '%'
            try:
                for person in session.query(md.User).filter(md.User.name.like(param)):
                    print(person.name, person.email)
                for person in session.query(md.User).filter(md.User.email.like(param)):
                    print(person.name, person.email)
            except ValueError as e:
                print(e)
        elif param.isdigit():
            param = f'%' + str(param) + '%'
            try:
                for phone in session.query(md.Phone).filter(md.Phone.phone.like(param)):
                    for person in session.query(md.User).filter(md.User.id == md.Phone.user_id):
                        print(person.name, person.email, phone.phone)
            except ValueError as e:
                print(e)

    


def exit_command(*args):
    global CURRENT_RECORD
    CURRENT_RECORD = None
    return('exit')


COMMANDS = {ADD_COMMANDS: add_command, GREETING_COMMANDS: greeting_command, SHOW_ALL_COMMANDS: show_all_command,
            EXIT_COMMANDS: exit_command, HELP_COMMANDS: help_command, DELETE_COMMANDS: delete_command,
            EDIT_COMMANDS: edit_command, FIND_COMMANDS: find_command}


# general function


def non_command():
    return 'Sorry, i don`t know this command'


def parse_data(command, list):
    for i in list:
        if command.startswith(i):
            data = command.replace(i, '').strip()
            return data.split(' ')


def parse_command(command):
    for i in COMMANDS.keys():
        com = command.lower()
        if com.startswith(i):
            data = parse_data(command, i)
            return COMMANDS[i](*data)
    return non_command()


def work_mode(*args):
    global CURRENT_MODE
    if args[0] in CURRENT_MODES.keys():
        print(f'We are in {CURRENT_MODES[args[0]]} mode')
        CURRENT_MODE = args[0]
        while True:
            result = parse_command(
                input(f'({CURRENT_MODES[args[0]]} mode {"" if not CURRENT_RECORD else str(CURRENT_RECORD) }) type command: '))
            if result == 'exit':
                print("Good Bye!")
                CURRENT_MODE = ''
                break
    else:
        pass


if __name__ == '__main__':
    print('Hi! I\'m your personal helper (PH). For more information type "help"')
    while True:
        result = input('PH says - please, select a workmode or "exit":')
        if result in ('1', '2', '3'):
            work_mode(result)
        else:
            result = parse_command(result)
        if result == 'exit':
            print("Good Bye!")
            break
from collections import UserDict, UserList


class Field:
    pass

class Phone(Field):
    phone = ''

class Name(Field):
    name = ''

class Record(UserList):

    name = Name.name
    phones = [Phone.phone]

    def add_phone(self, value):
        if value in self.phones:
            return self.phones
        else:
            self.phones.append(value)
            return self.phones

    def del_phone(self, value):
        if value in self.phones:
            self.phones.remove(value)
        else:
            print(f'{value} is not exist')

    def change_phone(self, value, new_value):
        if value in self.data.phones:
            self.phones.remove(value)
            self.phones.append(new_value)
        else:
            print(f'{value} not in phones book')


class AddressBook(UserDict):

    def add_record(self, Record):
        self.data[Record.name] = Record.phones


def main():
    user = Record()
    user.name = 'Ivan'
    print(user.name)
    user.add_phone('+380501111111')
    user.add_phone('+380501111112')
    user.add_phone('3333')
    user.del_phone('5555')
    user.del_phone('3333')
    print(user.phones)
    f = AddressBook()
    f.add_record(user)
    print(f)
    
    


if __name__ == '__main__':
    main()

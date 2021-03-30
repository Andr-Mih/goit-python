from datetime import datetime
import re
from pickle import dump, load
from collections import UserDict, UserList
from copy import copy


class Field:
    pass

class Phone(Field):
    
    def __init__(self, phone):
        self.__phone = ''
        self.phone = phone

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if re.match(r'[+][0-9]{10}', value):
            self.__phone = value[:11]
        else:
            print(f'Phone must consist 10 digits')

class Name(Field):
    def __init__(self, name):
        self.name = name

class Birthday(Field):
    
    def __init__(self, value):
        self.__birthday = None
        self.birthday = value

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        if re.match(r'\d\d/\d\d/\d\d\d\d', value):
            self.__birthday = value
        else:
            print(f'Enter birthday if format DD/MM/YYYY')



class Record(UserList):

    def __init__(self, Name, Phone, Birthday=None):
        self.name = Name.name
        self.phones = [Phone.phone]
        self.birthday = Birthday.birthday


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

    def days_to_bithday(self):
        if self.birthday:
            now = datetime.now().date()
            bith = datetime.strptime(self.birthday, '%d/%m/%Y').date()
            if bith.month < now.month:
                next_birt = datetime(year = now.year+1, month = bith.month, day = bith.day).date()
                result = next_birt - now
            elif bith.month > now.month:
                next_birt = datetime(year = now.year, month = bith.month, day = bith.day).date()
                result = next_birt - now
            elif bith.month == now.month and bith.day > now.day:
                next_birt = datetime(year = now.year, month = bith.month, day = bith.day).date()
                result = next_birt - now
            else:
                next_birt = datetime(year = now.year+1, month = bith.month, day = bith.day).date()
                result = next_birt - now
        return f'{result.days} days left to Bithday'


class AddressBook(UserDict):

    def __init__(self):
        self.number_of_records = 2
        self.data = {}
        self.current_value = 0
        

    def add_record(self, Record):
        self.data[Record.name] = Record.phones

    def _list_keys(self):
        self.keys = []
        for key in self.data.keys():
            self.keys.append(key)
        return self.keys


    def __next__ (self):
        
        result1 = ''
        self._list_keys()
        end_value = self.current_value + self.number_of_records
        for k in self.keys[self.current_value : end_value]:
            result = f'{self.keys[self.current_value]} : {self.data[self.keys[self.current_value]]}\n'
            self.current_value +=1
            result1 += result
        self.current_value = end_value
        
        if self.current_value > len(self.keys):
            raise StopIteration
        return result1


    def search(self, line):
        self.value = str(line)
        self.dict_key = {}
        self.dict_value = {}
        result_key = None
        result_value = None
        for key, value in self.data.items():
            if key.lower().find(self.value) >= 0:
                self.dict_key[key] = self.data[key]
            for val in value:
                if str(value).find(self.value) >= 0:
                    self.dict_value[key] = value

        if self.dict_key:
            result_key = self.dict_key
        if self.dict_value:
            result_value = self.dict_value
        return result_key, result_value
            
            
        
                  
        
        
        
    #def __iter__(self):
       # return self



def main():

    try:
        with open('data.txt', 'rb') as file:
            f = load(file)
        print(f)
    except:
        'File not found'
    
    user_phone = Phone('+380501231231')
    user_name = Name('Vas')
    user_birthday = Birthday('12/03/2010')
    user = Record(user_name, user_phone, user_birthday)
    print(user.name)
    print(user.phones)
    print(user.birthday)
    user.add_phone('+380501111888')
    user.add_phone('+380501111112')
    user.add_phone('3333')
    user.del_phone('5555')
    user.del_phone('3333')
    print(user.phones)
    f = AddressBook()
    f.add_record(user)
    print(f)
    print(user.days_to_bithday())
    user_phone1 = Phone('+38050123122')
    user_name1 = Name('Ivas')
    user_birthday1 = Birthday('12/08/2010')
    user1 = Record(user_name1, user_phone1, user_birthday1)
    user_phone2 = Phone('+38050123155')
    user_name2 = Name('Kolt')
    user_birthday2 = Birthday('15/08/2011')
    user2 = Record(user_name2, user_phone2, user_birthday2)
    user_phone3 = Phone('+380501717177')
    user_name3 = Name('Roman')
    user_birthday3 = Birthday('12/10/2001')
    user3 = Record(user_name3, user_phone3, user_birthday3)
    f.add_record(user1)
    f.add_record(user2)
    f.add_record(user3)

    print(f)
    print(next(f))
    print(next(f))
    #print(next(f))

    print(f)
    print(user1.days_to_bithday())
    #print(user2.days_to_bithday())

    with open('data.txt', 'wb') as file:
        dump(f, file)

    ask = input('Enter a search request: ')
    print(f.search(ask))
    

    


if __name__ == '__main__':
    main()

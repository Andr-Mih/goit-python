from datetime import datetime
from mongoengine import *

from models_db import *

connect(host="mongodb+srv://dev:j2876ChsUfjqBnz@cluster0.onoag.mongodb.net/PhoneBook?retryWrites=true&w=majority")

if __name__ == '__main__':
    try:
        email = Email(email='Ivan@gmail.com')
        pb = PhoneBook(name='Ivan', emails=[email, ], phones=[Phone(phone='0985487325'), ], birthday='1997-10-12',
                       address='Kharkiv, 61000')
    except ValidationError as e:
        print(e)
    print('Records in db: ', len(PhoneBook.objects))

    for record in PhoneBook.objects:
        print(record.birthday.year)

    young_p = PhoneBook.objects(birthday__lte='1993-10-17')
    print('Records in db with filters: ', len(young_p))

    if PhoneBook.objects(name=pb.name):
        PhoneBook.objects(name=pb.name).delete()
        print('Records in db after deleting: ', len(PhoneBook.objects))
        pb.save()
        print('Records in db after saving: ', len(PhoneBook.objects))
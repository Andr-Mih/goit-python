from datetime import datetime
from mongoengine import *
import re


def email_validations(value):
    if not re.match('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', value):
        raise ValueError(
            'Email not valid, must be "name@domenname.com"')


def phone_validations(value):
    if not re.match('\d{10}$', value):
        raise ValueError('Phone number must have 10 digits')


class Email(EmbeddedDocument):
    email = StringField(validation=email_validations)


class Phone(EmbeddedDocument):
    phone = StringField(validation=phone_validations)


class BirthdayField(DateField):
    def validate(self, value):
        if not re.match('\d{4}-\d{2}-\d{2}', value):
            self.error('Birthday must be "yyyy-mm-dd" format')
        b_year, b_month, b_day = value.split('-')
        if int(b_month) > 12 or int(b_day) > 31:
            self.error('Month must be in "01-12" day must be in "01-31"')
        else:
            value = datetime(int(b_year), int(b_month), int(b_day))
            super(BirthdayField, self).validate(value)


class PhoneBook(Document):
    name = StringField(required=True)
    birthday = BirthdayField()
    emails = ListField(EmbeddedDocumentField(Email))
    phones = ListField(EmbeddedDocumentField(Phone))
    address = StringField(max_length=100)

    meta = {'allow_inheritance': True}
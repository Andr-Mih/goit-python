from collections import UserDict
from datetime import date, datetime
from os import error, name
import pickle
import re
import unittest


class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Birthday(Field):
    # def __init__(self, birthday=''):
    #     self.birthday = birthday
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if not new_value:
            self.__value = new_value
        else:
            if not re.match("\d{2}-\d{2}", new_value):
                raise ValueError('Birthday must be "mm-dd" format')
            b_month, b_day = new_value.split("-")
            if int(b_month) > 12 or int(b_day) > 31:
                raise ValueError('Month must be in "01-12" day must be in "01-31"')
            else:
                self.__value = new_value


class BirtdayTestCase(unittest.TestCase):
    def test_birthday(self):
        a = Birthday("11-11")
        self.assertIsInstance(a, Birthday)
        with self.assertRaises(ValueError):
            b = Birthday("13-13")


class Name(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Phone(Field):
    # def __init__(self, phone):
    #     self.phone = phone
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if not re.match("\d{10}$", new_value):
            raise ValueError("Phone number must have 10 digits")
        else:
            self.__value = new_value


class PhoneTestCase(unittest.TestCase):
    def test_phone(self):
        phone = "1380999999"
        phon = Phone(phone)
        self.assertIsInstance(phon, Phone)
        with self.assertRaises(ValueError):
            b = Phone("+3805012466")


class Email(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if not new_value:
            self.__value = new_value
        else:
            if not re.match("^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$", new_value):
                raise ValueError('Email not valid format, must be "name@domenname.com"')
            else:
                self.__value = new_value


class EmailTestCase(unittest.TestCase):
    def test_email(self):
        email = "abracadabra@com.com"
        mail = Email(email)
        self.assertNotIsInstance(mail, Phone)
        with self.assertRaises(ValueError):
            b = Email("123243gmail.com")


class Address(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class TestAddress(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p = Address("Odessa, Primorskaia 14")

    def test_value(self):
        self.assertEqual(self.p.value, "Odessa, Primorskaia 14")


class Record:
    def __init__(self, *args):

        self.records = {}
        self.records["phones"] = []
        self.records["birthday"] = ""
        self.records["email"] = ""
        self.records["address"] = ""

        for arg in args:

            if isinstance(arg, Name):
                self.records["name"] = arg.value
            elif isinstance(arg, Phone):
                self.records["phones"].append(arg.value)
            elif isinstance(arg, Birthday):
                self.records["birthday"] = arg.value
            elif isinstance(arg, Email):
                self.records["email"] = arg.value
            elif isinstance(arg, Address):
                self.records["address"] = arg.value

    def __str__(self):
        result = f'Name - {self.records["name"]}, phones - {self.records["phones"]}, email - {self.records["email"]}, address - {self.records["address"]}, birthday - {self.records["birthday"]}'
        return result

    def add_phone(self, obj):
        if isinstance(obj, Phone):
            self.records["phones"].append(obj.value)
            # self.record[self.name] = self.phones

    def edit_phone(self, index, obj):
        if isinstance(obj, Phone):
            self.records["phones"][index] = obj.value

    def delete_phone(self, index):
        self.records["phones"].pop(index)

    def __count_days(self, d_now, d_birth):
        if d_now > d_birth:
            d_birth = date(d_birth.year + 1, d_birth.month, d_birth.day)
        return d_birth - d_now

    def days_to_birthday(self):
        __birthday = self.records["birthday"]

        if __birthday != "":
            result = self.__count_days(
                datetime.now().date(),
                date(
                    year=datetime.now().year,
                    month=int(__birthday.split("-")[0]),
                    day=int(__birthday.split("-")[1]),
                ),
            )

            return result.days
        else:
            return -1


class RecordTestCase(unittest.TestCase):
    def setUp(self):
        self.name = "Ivan"
        self.phone = "0991452145"
        self.phone1 = "0991452122"
        self.birthday = "10-10"
        self.birthday1 = "14-11"
        self.mail = "ivan@fox.com"
        self.adress = "Kyiv, Chkalova, 11"
        self.record = Record(
            Name(self.name),
            Phone(self.phone),
            Email(self.mail),
            Address(self.adress),
            Birthday(self.birthday),
        )

    def test_record(self):

        self.assertIsNot(Name(self.name), Name("Ivan"))
        self.assertTrue(Name(self.name))
        self.assertTrue(Phone(self.phone))
        self.assertTrue(Email(self.mail))
        self.assertTrue(Address(self.adress))
        self.assertTrue(self.record)
        with self.assertRaises(ValueError):
            self.birt = Birthday(self.birthday1)

    def test_add_phone(self):
        self.record.add_phone(Phone(self.phone1))
        self.assertTrue(self.phone1 in self.record.records["phones"])
        # print((self.record.records['phones']))

    def test_edit_phone(self):
        self.record.edit_phone(0, Phone("0505256145"))
        self.assertTrue("0505256145" in self.record.records["phones"])
        self.assertFalse(self.phone1 in self.record.records["phones"])

    def test_delete_phone(self):
        self.record.delete_phone(0)
        self.assertEqual(len(self.record.records["phones"]), 0)


class AddressBook(UserDict):

    __record_count = 0

    def __init__(self):
        super(AddressBook, self).__init__()

    def __iter__(self):
        return self

    def __next__(self):
        if self.__record_count < len(self.data):
            result = self.data[self.__record_count]
            self.__record_count += 1
            return result
        else:
            raise StopIteration

    def __getstate__(self):
        self._AddressBook__record_count = 0
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__ = state

    def __str__(self):
        result = ""
        for key, data in self.data.items():
            result += f'id - {key} | name - {data["name"]} | birthday - {data["birthday"]} | address - {data["address"]} | phones - {data["phones"]} | email - {data["email"]}\n'
        return result

    def __getitem__(self, key):
        rec = self.data[key]
        return f'id - {key} | name - {rec["name"]} | birthday - {rec["birthday"]} | address - {rec["address"]} | phones - {rec["phones"]} | email - {rec["email"]}'

    def add_record(self, obj):
        if isinstance(obj, Record):
            self.data[len(self.data)] = obj.records

    def delete_record(self, key):
        if key in self.data:
            self.data.pop(key)
            new_ab = UserDict()
            i = 0
            for v in self.data.values():
                new_ab[i] = v
                i += 1
            self.data = new_ab
        else:
            return f"{key} is not exist in AddressBook."

    def find(self, param):

        result = []

        if len(param) < 3:
            raise ValueError(f"Parameter must be 3 or more symbol")

        if param.isalpha():
            # result =  list(filter(lambda value: param.lower() in value['name'].lower(), self.data.values()))
            for key, value in self.data.items():
                if param.lower() in value["name"].lower():
                    result.append(self[key])
            return result
        elif param.isdigit():

            for key, value in self.data.items():
                if list((x for x in value["phones"] if param in x)):
                    result.append(self[key])
            return result
        else:
            return result


class AddressBookTestCase(unittest.TestCase):
    def setUp(self):
        self.name = "Ivan"
        self.phone = "0991452145"
        self.phone1 = "0991452122"
        self.birthday = "10-10"
        self.birthday1 = "14-11"
        self.mail = "ivan@fox.com"
        self.adress = "Kyiv, Chkalova, 11"
        self.record = Record(
            Name(self.name),
            Phone(self.phone),
            Email(self.mail),
            Address(self.adress),
            Birthday(self.birthday),
        )
        self.data = AddressBook()

    def test_add_record(self):
        self.data.add_record(self.record)
        self.assertTrue(self.data[0].find("Ivan"))

    def test_delete_record(self):
        self.data.add_record(self.record)
        self.data.delete_record(0)
        self.assertEqual(len(self.data), 0)

    def test_find_record(self):
        self.data.add_record(self.record)
        self.assertTrue(self.data.find("Ivan"))
        self.assertTrue(self.data.find("099"))
        self.assertFalse(self.data.find("Semen"))


def save_addressBook(obj):
    with open("address_book.bin", "wb") as file:
        pickle.dump(obj, file)


def load_addressBook():
    try:
        file = open("address_book.bin", "rb")
    except FileNotFoundError:
        return False
    else:
        with file:
            return pickle.load(file)


if __name__ == "__main__":
    unittest.main()

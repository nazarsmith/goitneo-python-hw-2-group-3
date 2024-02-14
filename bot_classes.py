from collections import UserDict
import re


class NoNumber(TypeError):
    pass


class NoName(TypeError):
    pass


class Field:
    def __init__(self, item):
        self.item = item

    def __str__(self):
        return str(self.item)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)
        self.name = name


class Phone(Field):
    def __init__(self, phone):
        super().__init__(phone)
        self.phone = re.match("[0-9]{10}", phone).group(0)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.item}, phones: {'; '.join(p.item for p in self.phones)}"

    def list_str_rep(self, lst: list):
        return [str(i) for i in lst]

    def error_handler(function):
        def handle(self, *args, **kwargs):
            try:
                return function(self, *args, **kwargs)
            except IndexError:
                return "This phone number is not associated with this contact."

            except ValueError:
                return f"{args[0]} is not on the list of {self.name}'s phone numbers."

            except NoNumber as err:
                return err.args[0]

            except TypeError:
                return "The phone number(s) not provided. Try again."

            except AttributeError:
                return "The phone number is of invalid format. Try again."

            except:
                return "Something went wrong."

        return handle

    @error_handler
    def add_phone(self, phone=None):
        if not phone:
            raise NoNumber("No phone number was provided.")
        phone_num = Phone(phone)
        self.phones.append(phone_num)

    @error_handler
    def edit_phone(self, old_phone, new_phone):
        old_phone_index = self.list_str_rep(self.phones).index(old_phone)
        self.phones[old_phone_index] = Phone(new_phone)

    @error_handler
    def find_phone(self, phone=None):
        if not phone:
            raise NoNumber("No phone number was provided.")
        found_phone_index = self.list_str_rep(self.phones).index(phone)
        found_phone = self.phones[found_phone_index]
        return found_phone

    @error_handler
    def remove_phone(self, phone=None):
        if not phone:
            raise NoNumber("No phone number was provided.")
        found_phone_index = self.list_str_rep(self.phones).index(phone)
        self.phones.pop(found_phone_index)


class AddressBook(UserDict):
    records = 0

    def __init__(self):
        self.data = {}

    def error_handler(function):
        def handle(self, *args, **kwargs):
            try:
                return function(self, *args, **kwargs)
            except KeyError:
                return f"The contacts book doesn't have a contact named {args[0]}"
            except NoName as err:
                return err.args[0]
            except TypeError:
                return "Record details not provided."
            except:
                return "Something went wrong."

        return handle

    @error_handler
    def add_record(self, record):
        self.data.update({str(record.name): record})
        AddressBook.records += 1

    @error_handler
    def find(self, name=None):
        if not name:
            raise NoName("The name of a contact not provided.")
        return self.data[name]

    @error_handler
    def delete(self, name=None):
        if not name:
            raise NoName("The name of a contact not provided.")
        self.data.pop(name)
        AddressBook.records -= 1

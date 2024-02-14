from bot_classes import AddressBook, Record


def create_record(name):
    record = Record(name)
    return record


def create_address_book():
    address_book = AddressBook()
    return address_book


def test_record():

    def test_no_phone(test):
        assert test == "No phone number was provided."

    john_record = create_record("John")
    assert str(john_record) == "Contact name: John, phones: "
    test_no_phone(john_record.add_phone())
    john_record.add_phone("1234123412")
    assert str(john_record) == "Contact name: John, phones: 1234123412"
    assert (
        john_record.add_phone("1234")
        == "The phone number is of invalid format. Try again."
    )
    john_record.add_phone("1234555888")
    assert str(john_record) == "Contact name: John, phones: 1234123412; 1234555888"
    assert john_record.edit_phone() == "The phone number(s) not provided. Try again."
    john_record.edit_phone("1234123412", "8888999900")
    assert str(john_record) == "Contact name: John, phones: 8888999900; 1234555888"
    test_no_phone(john_record.find_phone())
    assert (
        john_record.find_phone("1111111111")
        == "1111111111 is not on the list of John's phone numbers."
    )
    found_phone = john_record.find_phone("1234555888")
    assert f"{john_record.name}: {found_phone}" == "John: 1234555888"
    test_no_phone(john_record.remove_phone())
    john_record.remove_phone("1234555888")
    assert str(john_record) == "Contact name: John, phones: 8888999900"


def test_address_book():

    def create_record_to_add(name=None, phone=None):
        record = create_record(name)
        record.add_phone(phone)
        return record

    address_book = create_address_book()
    assert address_book == {}
    assert address_book.add_record() == "Record details not provided."
    address_book.add_record(create_record_to_add("John", "1234555888"))
    assert str(address_book["John"]) == "Contact name: John, phones: 1234555888"
    address_book.add_record(create_record_to_add("Jane", "1234432199"))
    assert str(address_book["Jane"]) == "Contact name: Jane, phones: 1234432199"
    records = [str(record) for name, record in address_book.data.items()]
    assert records == [
        "Contact name: John, phones: 1234555888",
        "Contact name: Jane, phones: 1234432199",
    ]
    assert address_book.records == 2
    assert address_book.find() == "The name of a contact not provided."
    assert (
        address_book.find("Jake")
        == "The contacts book doesn't have a contact named Jake"
    )
    john_found = address_book.find("John")
    assert str(john_found) == "Contact name: John, phones: 1234555888"
    assert address_book.delete() == "The name of a contact not provided."
    assert (
        address_book.delete("Jake")
        == "The contacts book doesn't have a contact named Jake"
    )
    address_book.delete("John")
    records = [str(record) for name, record in address_book.data.items()]
    assert records == [
        "Contact name: Jane, phones: 1234432199",
    ]
    assert address_book.records == 1

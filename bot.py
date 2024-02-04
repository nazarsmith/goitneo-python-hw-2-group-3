from handler import *


def main():
    contacts = {}

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("How can I help you?\nEnter a command: ")

        command, *args = parser(user_input)
        if command in ["exit", "close"]:
            print("Good bye!")
            break

        elif command in ["hello", "hi", "greetings"]:
            print(greeting(), end=" ")

        elif command == "add":
            print(add_contact(contacts, args))

        elif command == "all":
            [print(c) for c in show_all(contacts)]

        elif command == "phone":
            print(show_phone(contacts, args))

        elif command == "change":
            print(change_contact(contacts, args))

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":

    main()

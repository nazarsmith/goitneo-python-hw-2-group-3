from handler import (
    parser,
    add_contact,
    show_all,
    change_contact,
    show_phone,
    greeting,
)


def main():
    contacts = {}

    print("Welcome to the assistant bot!")
    while True:

        user_input = input("How can I help you?\nEnter a command: ")
        command, *args, message = parser(user_input)
        if message:
            print(message)

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

        elif not command:
            pass

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

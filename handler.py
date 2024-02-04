import random
import re


def parser(user_input):

    command, *args = user_input.split()
    command = command.lower().strip()
    ## for cases when name + surname are provided
    if len(args) > 2:
        args[0] = args[0] + " " + args[1]
        del args[1]
    return command, *args


def check_phone_num(phone_num):
    pattern = "^[\+0-9\-]{10,16}$"
    phone_num = re.match(pattern, phone_num)

    ## throws exception if there was no match
    phone_num = phone_num.group(0)
    ## check if the phone number match contains only numbers
    int(phone_num.strip("+"))

    return phone_num


def greeting():
    ## select and play a greeting reaction
    prompt = random.choice(["Hello!", "Hi!", "Greetings!"])
    return prompt


def add_contact(contacts, args):
    name = args[0]
    confirm = None
    if name in contacts.keys():
        confirm = input("A contact with this name found. Update it? yes / no: ")
        confirm.lower()
    if confirm in ["yes", "1", "affirmative", "y"] or not confirm:
        try:
            phone_num = check_phone_num(args[-1])
            contacts.update({name: phone_num})
            return "Contact added."
        except:
            return "Invalid or no phone number was entered. Please try again."
    return "Canelling contact addition."


def change_contact(contacts, args):
    try:
        check_phone_num(args[1])
        contacts.update({args[0]: args[1]})
        return "Contact updated."
    except:
        return "Invalid or no phone number was entered. Please try again."


def show_phone(contacts, args):
    ## for cases when name + surname are provided
    if len(args) == 2:
        args = [" ".join(args)]
    try:
        return f"{args[0]}'s phone number: {contacts[args[0]]}"
    except:
        return "No contact with this name was found. Please try again."


def show_all(contacts):
    names = list(contacts.keys())
    phones = list(contacts.values())

    for i in range(len(contacts.items())):
        yield "{:>2}. | {:^20} | {:>10}".format(i + 1, names[i], phones[i])

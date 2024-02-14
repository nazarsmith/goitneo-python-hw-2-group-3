import random
import re


class WrongInfoException(ValueError):
    def __init__(self, message):
        self.message = message


def wrong_input_handling(function):
    def handling(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except WrongInfoException as err:
            return err
        except AttributeError:
            return "The number you entered is too short or too long. Try again."
        except KeyError:
            return "No contact with this name was found. Try again."
        except ValueError:
            return "The number must contain only digits and/or a + sign. Try again."
        except:
            return "Something went wrong. Please try again."

    return handling


def parser(user_input):
    if user_input == "":
        return None, None, "Please start with a valid command."

    command, *args = user_input.split()
    command = command.lower().strip()

    ## for cases when name + surname are provided
    if len(args) > 2:
        args[0] = args[0] + " " + args[1]
        del args[1]
    return command, *args, None


def check_phone_num(phone_num):
    pattern = "^[\+0-9\-]{10,16}$"

    int(phone_num.strip("+"))
    phone_num = re.match(pattern, phone_num)
    phone_num = phone_num.group(0)

    return phone_num


def greeting():
    ## select and play a greeting reaction
    prompt = random.choice(["Hello!", "Hi!", "Greetings!"])
    return prompt


@wrong_input_handling
def add_contact(contacts, args):

    if len(args) == 1:
        raise WrongInfoException("Please provide both a name and a phone number.")

    elif len(args) < 1:
        raise WrongInfoException(
            "Neither name nor phone number provided. Please try again."
        )

    elif len(args) > 1:
        name = args[0]
        confirm = None

    if name in contacts.keys():
        confirm = input("A contact with this name found. Update it? yes / no: ")
        confirm.lower()
    if confirm in ["yes", "1", "affirmative", "y"] or not confirm:
        phone_num = check_phone_num(args[-1])
        contacts.update({name: phone_num})
        return "Contact added."

    return "Canelling contact addition."


@wrong_input_handling
def change_contact(contacts, args):
    check_phone_num(args[1])
    contacts.update({args[0]: args[1]})
    return "Contact updated."


def show_phone(contacts, args):
    ## for cases when name + surname are provided
    if len(args) == 2:
        args = [" ".join(args)]

    return f"{args[0]}'s phone number: {contacts[args[0]]}"


def show_all(contacts):
    names = list(contacts.keys())
    phones = list(contacts.values())

    for i in range(len(contacts.items())):
        yield "{:>2}. | {:^20} | {:>10}".format(i + 1, names[i], phones[i])

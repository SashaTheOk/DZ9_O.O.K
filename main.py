ADDRESSBOOK = {}


def input_error(inner):
    def wrap(*args):
        try:
            return inner(*args)
        except IndexError:
            return "Give me name and phone please"
        except KeyError as e:
            return f"Contact {str(e)} not found"
        except ValueError:
            return "Invalid input. Please provide a valid value."
    return wrap


@input_error
def add_handler(data):  # Функції обробники команд
    name = data[0].title()
    phone = data[1]
    ADDRESSBOOK[name] = phone
    return f"Contact {name} with phone {phone} was saved"


@input_error
def delete_handler(data): # видалення
    name = data[0].title()
    if name in ADDRESSBOOK:
        del ADDRESSBOOK[name]
        return f"Contact {name} has been deleted."
    else:
        return f"Contact {name} not found."


@input_error
def edit_handler(data): # зміна даних
    name = data[0].title()
    if name in ADDRESSBOOK:
        new_phone = data[1]
        ADDRESSBOOK[name] = new_phone
        return f"The phone number for {name} has been updated to {new_phone}."
    else:
        return f"Contact {name} not found."


def exit_handler(*args):
    return "Good bye!"


def hello_handler(*args):
    return "How can I help you?"


@input_error
def list_contacts(*args): # всі контакти
    if not ADDRESSBOOK:
        return "The address book is empty."
    else:
        result = "Contacts:\n"
        for name, phone in ADDRESSBOOK.items():
            result += f"{name}: {phone}\n"
        return result


@input_error
def command_parser(raw_str: str):  # Парсер команд
    elements = raw_str.split()
    for key, value in COMMANDS.items():
        if elements[0].lower() in value:
            return key(elements[1:])
    return "Unknown command"


@input_error
def show_phone_handler(data): #пошук через номер тел.
    phone = data[0]
    for name, stored_phone in ADDRESSBOOK.items():
        if phone == stored_phone:
            return f"The contact with phone number {phone} is {name}."
    return f"Contact with phone number {phone} not found."


COMMANDS = {
    add_handler: ["add", "додай", "+"],
    list_contacts: ["show all", "list", "список"],
    delete_handler: ["delete", "видалити", "-"],
    edit_handler: ["change", "edit", "редагувати"],
    exit_handler: ["good bye", "close", "exit", "вийти"],
    hello_handler: ["hello", "старт"],
    show_phone_handler: ["phone", "номер"]
}


def main():  # Цикл запит-відповідь.
    while True:
        user_input = input(">>> ")  # add Vlad 0987009090
        result = command_parser(user_input)
        print(result)
        if result == "Good bye!":
            break


if __name__ == "__main__":
    main()

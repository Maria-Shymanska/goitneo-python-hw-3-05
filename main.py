from classes import AddressBook



def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name"

    return inner



@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: Invalid number of arguments. Use 'add [name] [phone number]'."
    
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added with phone number {phone}."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: Invalid number of arguments. Use 'change [name] [new phone number]'."
    
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Phone number for {name} changed to {new_phone}."
    else:
        return f"Contact {name} not found."
    
@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: Invalid number of arguments. Use 'phone [name]'."
    
    name = args[0]
    if name in contacts:
        return f"The phone number for {name} is {contacts[name]}."
    else:
        return f"Contact {name} not found."

def show_all(contacts):
    if not contacts:
        return "No contacts available."
    
    
@input_error
def add_birthday(args, contacts):
    name = args[0]
    rec = contacts.find(name)
    birthday = args[1]
    rec.add_birthday(birthday)
    return "Birthday added."

def show_birthday(args, contacts):
    name = args[0]
    rec = contacts.find(name)
    return((rec.show_birthday()))

def birthdays(contacts):
    birthdays_dict = dict(contacts.week_birthdays(contacts))
    return(birthdays_dict)

    # result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    # return result



def main():
    contacts = AddressBook()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "add-birthday":
            print(add_birthday(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "birthdays":
            print(birthdays(contacts))
        elif command == "help":
            print(f"""
            This is a console bot-assitant.
            The bot works with following commands:
1) add [Name] [Phone]                      Add new contact with a "Name" and "Phone number".
2) change [Name] [New phone]               Change phone number to "New phone" for contact with "Name".
3) phone [Name]                            Show phohne number for contact "Name".
4) all                                     Show all contacts in AddressBook.
5) add-birthday [Name] [Date of Birth]     Add "Date of Birth" for contact "Name".
6) show-birthday [Name]                    Show Date of Birth for contact "Name".
7) birthdays                               Show all birthdays for the next week.
8) hello                                   Receive "Hello" from the bot.
9) close OR exit                           Close the program.
10) help                                   Get this list of commands.        """)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
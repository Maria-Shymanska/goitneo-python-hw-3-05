
from collections import UserDict, defaultdict
from datetime import datetime, timedelta

class Field:                #  Base Class for Record Fields
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):    # A class to store the contact's name. Required field.
    def __init__(self, value: str):
        if not value.isalpha():
            print("The name must consist letters only")
            raise ValueError
        if not value.istitle():
            print("The name must start with an upper case letter and the rest letter must be lower case")
            raise ValueError
        self.value = value
        
class Birthday:
    def __init__(self, value: str):
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except:
            print("The birthday date must be in format DD.MM.YYYY")
            raise ValueError
        self.value = value
        
    
class Phone(Field):
    def __init__(self, value: str):
        # Perform validation for phone number format (e.g., 10 digits)
        if not isinstance(value, str) or not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number format.")
        super().__init__(value) 

class Record:
    def __init__(self, name, birthday = None):
        self.name = Name(name)
        self.phones = []
        self.birthday = birthday

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)
        
    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if str(phone) == old_phone:
                self.phones[i] = Phone(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if str(p) == phone:
                return p
        

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, value):
        if not (self.data.get(value)):
            print("There is not such name in AddressBook")
            raise ValueError
        return(self.data.get(value))
    
    
    
    def get_birthdays_per_week(users):
    
        birthdays_by_day = defaultdict(list)

        today = datetime.today().date()

        for user in users:
            name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        day_of_week = (today + timedelta(days=delta_days)).strftime("%A")
        if delta_days < 7:
            birthdays_by_day[day_of_week].append(name)
        else:
            print("Invalid command")
        


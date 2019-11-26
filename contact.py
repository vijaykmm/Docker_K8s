# Creating class named contacts with methods for editing and adding new 
# contacts. Also there are static methods for showing a specific or all
# contacts data and for showing if there's no contact saved on the address book.

class Contact:

    def __init__(self, name, surname, number, email):
        self.name = name
        self.surname = surname
        self.number = number
        self.email = email

    def edit_name(self, name):
        self.name = name
        return self.name

    def edit_surname(self, surname):
        self.surname = surname
        return self.surname

    def edit_number(self, number):
        self.number = number
        return self.number

    def edit_email(self, email):
        self.email = email
        return self.email

    @classmethod
    def add(cls, name, surname, number, email):
        return cls(name, surname, number, email)

    # This method prints prints all data of a specific entry it index is provided
    # otherwise it prints data of all entries saved in address book (fullnames, 
    # numbers and emails)
    @staticmethod
    def summary(index=0):
        if index == 0:
            for j in range(0, len(address_book)):
                print(address_book[j].name, address_book[j].surname, end=' / ')
                print(address_book[j].number, '/', address_book[j].email)
        else:
            print(address_book[index].name, address_book[index].surname, end=' / ')
            print(address_book[index].number, '/', address_book[index].email)
        print()
        return None

    # Prints only the names saved in the address book
    @staticmethod
    def saved():
        print('CONTACTS SAVED: ', end='')
        for j in range(0, len(address_book)):
            print(j, address_book[j].name, end=' || ')
        return None

    # Prompts the user if there's no contact saved in address book
    @staticmethod
    def isempty(list):
        if len(list) == 0:
            print('NO CONTACT SAVED\n')
            return True
        return False

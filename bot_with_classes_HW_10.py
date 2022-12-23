from collections import UserDict
finish_words = ["goodbye", "close", "exit"]
COMMAND_WORDS = ["add", "change", "phone", "show all", "help"]

class PhoneNotInt(Exception):
    pass

class AddressBook(UserDict):

    user_id = 0
    address_book = {}

    def add_record(self, new_user):
        for key, val in new_user.items():

            self.data[key] = val
            
        AddressBook.user_id += 1
        AddressBook.address_book.update(self.data)
        return self.data

class Field:
    pass

class Record(Field):

    def record_name(self, name):
        self.name = name
        return self.name


    def record_phone(self, phones):
        self.phone_numb = phones
        return self.phone_numb

    def add_user(self, name, phones):

        new_user = {}

        if len(AddressBook().address_book):

            for elem in AddressBook().address_book:
                if name in elem:
                    name = name + str(AddressBook.user_id)

        new_user[name] = phones

        return new_user

    def change_number(self, name, phones):
        for key in AddressBook().address_book: 
            if key == name:
                AddressBook().address_book[name] = phones
                return AddressBook().address_book[name]
        return f"There is no user with name {name}"

    def show_phone(self, name):
        
        for key, val in AddressBook().address_book.items():
            if key == name:
                return f"the user {key} has the next phone numbers {val}"
        return f"There is not {name} in the Address book"

class Name(Field):

    def user_name_def(self, name):
        self.name_value = name
        return self.name_value
        

class Phone(Field):

    def user_phones_def(self, phones):

        self.phones = phones
        

        #while not self.phones:
            #raise PhoneNotInt

        while True:

            try:
                for elem in self.phones:
                    if not elem.isdigit():
                        raise PhoneNotInt
                    else:
                        break
            except PhoneNotInt:
                inp_phones = input("Phones should include only numbers. Please, enter phone number without symbols ")
                self.phones = inp_phones.split(" ")

            else:
                return self.phones
            
        
def main():

    """
    This function takes the command from user and do what the user asks.
    It stops the process when the key words are entered

    """

    while True:

        user_command = input("Enter your command and data or enter 'help' to get the manual of bot  ")
        user_command_small_letters = user_command.lower()

        if user_command_small_letters == "hello":
            print("How can I help you?")


        for word in COMMAND_WORDS:

            if user_command_small_letters.startswith(word):

                user_data = user_command.split(" ")
                
                if user_data[0].lower() == "add":
                    if len(user_data) > 2:
                        add_new_user = AddressBook()
                        print(f"add to the address book {add_new_user.add_record(Record().add_user(Record().record_name(Name().user_name_def(user_data[1])), Record().record_phone(Phone().user_phones_def(user_data[2:]))))}")

                elif user_data[0].lower() == "help":
                    print("Enter 'add' and user's name and phone to add the user, 'change' and user's name and phone for changing the phone number, 'phone' and user's name to show the phone number, 'show all' to see the all users")

                elif user_command_small_letters.startswith("show all"):
                    print(AddressBook().address_book)

                elif user_data[0].lower() == "change":
                    if len(user_data) > 2:
                        change_user = Record()
                        print(f"changes in the address book: for {change_user.record_name(Name().user_name_def(user_data[1]))} result {change_user.change_number(change_user.record_name(Name().user_name_def(user_data[1])), change_user.record_phone(Phone().user_phones_def(user_data[2:])))}")

                elif user_data[0].lower() == "phone":
                    if len(user_data) > 1:
                        print(Record().show_phone(Name().user_name_def(user_data[1])))
                    
                    

        if user_command_small_letters in finish_words:
            break

        
        
    print("Good bye!")


if __name__ == '__main__':
    main()

    


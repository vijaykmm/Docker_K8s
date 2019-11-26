address_book = []
msg_error = '{}Invalid option{}'.format('\033[31m', '\033[m'    # Red text

access = input('Press any key to access')

while True:
    print('=-=-===-=-=-=-=-  CONTACTS MENU -=-=-=-=-=-==-==')
    print("""[ 1 ] ADD    [ 3 ] DELETE     [ 5 ] VIEW ALL
[ 2 ] MODIFY    [ 4 ] VIEW   [ 0 ] FINISH""")

  option = input('>>> ')

  #This if and elif blocks check if user input ranges from 0-5
  if not option.isnumeric():
      print(msg_error)
      continue

  elif option not in '012345':
      print(msg_error)
      continue

  # If between 0-5, convert value to integer and...
  else:
      option = int(option)

  if option == 0:
      print('>>> Program ended\n')
      break

  # Add new contact
  elif option == 1:
      name = input('Name: ').capitalize().strip()
      surname = input('Surname: ').capitalize().strip()
      number = input('Number: ').strip()
      email = input('Email: ').strip().lower()

      # Trasnform into Contact class and append to address book
      address_book.append(Contact.add(name, surname, number, email))
      print('Contact saved\n')

  # Modify a contact
  elif option == 2:
      if Contact.isempty(address_book):
          continue

      Contact.saved()
      name_index = int(input('\nModify which name? '))
      print('\nModify which entry?')
      entry_index = int(input('[ 1 ] NAME   [ 2 ] SURNAME   [ 3 ] NUMBER   [ 4 ] EMAIL\n>>>'))

      # Use object methods to modify within the list address book
      # User wants to modify name
      if entry_index == 1:
          modification = input('New name: ').capitalize().strip()
          address_book[name_index].edit_name(modification)

      # User wants to modify surname
      elif entry_index == 2:
          modification = input('New surname: ').capitalize().strip()
          address_book[name_index].edit_surname(modification)

      # User wants to modify number
      elif entry_index == 3:
          modification = input('New number: ').strip()
          address_book[name_index].edit_number(modification)

      # User wants to modify email
      elif entry_index == 4:
          modification = input('New email: ').lower().strip()
          address_book[name_index].edit_email(modification)
      print('Modification saved\n')

  # Delete a contact
  elif option == 3:
      if Contact.isempty(address_book):
          continue

      Contact.saved()
      name_index = int(input('\nWhich contact delete? '))
      del address_book[name_index]
      print('Contact deleted')

  # View specific contact details
  elif option == 4:
      if Contact.isempty(address_book):
          continue

      Contact.saved()
      index = int(input('\nContact position: '))
      Contact.summary(index)

  # View details of all contacts
  elif option == 5:
      if Contact.isempty(address_book):
          continue
      Contact.summary()

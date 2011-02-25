# superphonebook.py
# Super phone book to search, insert, delete, update, show all

'''Populate phone book with existing contacts'''
def initialize():
    try:
        # open input file
        infile = open("CONTACTS.TXT", "r")

        # read contents
        lines = infile.readlines()

        for line in lines: # for each contact
            line = line.rstrip("\n") # remove trailing new line character
            name = line[:20].strip() # get name with trailing white space removed
            contact_no = line [20:]      # get contact number
            phonebook[name] = contact_no # insert to phonebook dictionary
        
    except IOError: # file read error
        print("CONTACTS.TXT does not exist? Starting with empty phone book.")    


'''Menu to display options'''
def menu():
    print("Welcome to Super Phone Book")
    print("(1) Search")
    print("(2) Insert")
    print("(3) Update")
    print("(4) Delete")
    print("(5) Show all")
    print("(6) Import")
    print("(7) Export")
    print("(0) Quit")

'''Search name and return contact number if found, else return not found'''
def search(search_name):
    if search_name in phonebook.keys(): # found, show name and phone
        print("Contact number for", search_name, "is", phonebook[search_name])
    else: # not found
        print("No such contact")


'''Insert entry with name and contact number if not found, else prompt for update'''
def insert(insert_name):
    if insert_name not in phonebook.keys(): # not found, insert
        contact_no = input("Enter contact number: ")
        phonebook[insert_name] = contact_no
        print("Entry added")
    else: # found, prompt for update 
        update_ans = input("Already exists! Update(y/n)? ")
        if update_ans == 'y':
            update(insert_name)


'''Update entry with new contact number if found, else prompt for insert'''
def update(update_name):
    if update_name in phonebook.keys(): # found, update
        print("Current contact number for", update_name, "is", phonebook[update_name])
        contact_no = input("Enter new contact number: ")
        phonebook[update_name] = contact_no
        print("Entry updated.")
    else: # not found, prompt for insert
        insert_ans = input("Contact does not exist! Insert(y/n) ")
        if insert_ans == 'y':
            insert(update_name)


'''Delete entry if found, else error'''
def delete(delete_name):
    if delete_name in phonebook.keys(): # found, delete
        del phonebook[delete_name]
        print("Entry deleted.")
    else: # not found, error
        print("Contact not found! Nothing to delete.")
        

'''Display all names and contact numbers'''
def show_all():
    print("Name | Contact No") # heading
    for key, value in phonebook.items():
        print(key, value) # contact name and number
    print(len(phonebook), "contacts in phone book.") # number of records


'''Import contacts from text file'''
def import_contacts():

    successful_import = 0
    
    try:
        # open input contacts file
        infile = open("NEWCONTACTS.TXT", "r")
        
        # read all contents
        lines = infile.readlines()
        
        for line in lines: # for each contact
            line = line.rstrip("\n") # remove trailing new line character
            name = line[:20].strip() # get name with trailing white space removed
            contact_no = line [20:]      # get contact number
            if name not in phonebook.keys(): # if not exist, insert and increment successful import
                phonebook[name] = contact_no
                successful_import = successful_import + 1

        # show import status        
        print(successful_import, "contacts imported.")
        if successful_import != len(lines):
            print(len(lines) - successful_import, "contacts already exist.")

        # close input file
        infile.close()
        
    except IOError: # file read error
        print("NEWCONTACTS.TXT does not exist! Cannot import.")
    

'''Export contacts to text file'''
def export_contacts():
    try:
        # open output contacts file
        outfile = open("CONTACTS.TXT", "w")

        # write formatted names and contact numbers to file
        for key, value in phonebook.items():
            outfile.write("{0:20s}{1}\n".format(key, value))

        # show export status    
        print(len(phonebook), "contacts exported.")

        # close output file
        outfile.close()
        
    except IOError: # file write error
        print("Unable to export. Maybe disk full?")


# main

# initialize an empty dictionary
phonebook = {}

# populate phone book with existing contacts
initialize()

# assume not done
done = False

# loop until user chooses to quit
while not done:
    # display menu
    menu()
    # get choice from user
    option = input("What do you want to do today? ")
    if option == '1': # search
        name = input("Enter name to search: ")
        search(name)
    elif option == '2': # insert
        name = input("Enter name to insert: ")
        insert(name)
    elif option == '3': # update
        name = input("Enter name to update: ")
        update(name)
    elif option == '4': # delete
        name = input("Enter name to delete: ")
        delete(name)
    elif option == '5': # show all
        show_all()
    elif option == '6': # import contacts
        import_contacts()
    elif option == '7': # export contacts
        export_contacts()        
    elif option == '0': # quit
        done = True
    else: # invalid choices
        print("Invalid option! Try again.")
    print()
        
# exit
print("Bye.")

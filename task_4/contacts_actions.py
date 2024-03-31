def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Some arguments are missing"
            
def update_cantact(args, contacts):
    try:
        name, phone = args
        for contact in contacts.keys():
            if contact == name:
                contacts[name] = phone
                return "The contact number has been successfully changed."
    except ValueError:
        return "Some arguments are missing" 
  
def show_contact(args, contacts):
    try:
        name = args[0]
        for contact in contacts.keys():
            if contact == name:
                return contacts.get(name)
    except IndexError:
        return "Some arguments are missing"

def show_all_contacts(contacts):
    return contacts
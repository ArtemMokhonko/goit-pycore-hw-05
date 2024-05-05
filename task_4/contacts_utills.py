from error_decorator import input_error

@input_error
def add_contact(args: list[str], contacts: dict):
    name, phone = args
    if name in contacts:
        return f"This contact already exist."
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return f"Contact does not exist." 
    contacts[name] = phone
    return "Contact changed."

@input_error
def show_phone(args: list[str], contacts: dict):
    name,  = args
    
    return f"phone number: {contacts[name]}"

@input_error
def all_contacts(contacts: dict):
    if not contacts:
        return "There are no contacts."
    str_s = 'All contacts: \n'
    for name, phone in contacts.items():
        str_s += f"{name} {phone} \n"
            
    return str_s[:len(str_s)-1]




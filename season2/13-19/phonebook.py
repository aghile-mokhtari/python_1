import json
import pickle
import yaml
import csv
contacts = []
STORAGE = 'text'
def add():
    contacts.append(dict(
        firstname=input('FirstName :'),
        lastname=input('LastName :'),
        phone=input('PhonNumber :'),
        email = input('Email:')
    ))
    save()
def find(view_only=False):
    x = input('what do you looking for?')
    result = []
    for contact in contacts:
        if x in ' '.join(contact.values()):
            result.append(contact)
    view(result)
    if not view_only:
        if len(result) > 1:
            n = int(input('wich one ? '))
            return result[n-1]
        elif len(result) == 1:
            return result[0]
def delete():
    contact = find()
    if contact:
        if input('Are you shure?').strip().startswith('y'):
            contacts.remove(contact)
            print(f'{contact["firstname"]}{contact["lastname"]} has been deleted')
    save()

def edit():
    contact = find()
    if contact:
        for key in contact.keys():
            contact[key] = input(f'{key}({contact[key]}) : ') or contact[key]
        print('the contact has been changed')
    save()
def save():
    match STORAGE:
        case 'text':
            with open ('data.txt' , 'w') as f:
                f.write(str(contacts))
        case 'json':
            with open ('data.json' , 'w') as f:
                json.dump(contacts , f, indent=4)
        case 'pickle':
            with open ('data.pkl' , 'wb') as f:
                pickle.dump(contacts , f)
        case 'yaml':
            with open ('data.yaml' , 'w') as f:
                yaml.dump(contacts , f)
        case 'csv':
            with open ('data.csv' , 'w') as f:
               writer = csv.DictWriter(f , fieldnames=contacts[0].keys())
               writer.writeheader()
               writer.writerows(contacts)

def load():
    global contacts
    try:
        match STORAGE:
            case 'text':
                with open ('data.txt' , 'r') as f:
                    contacts = eval(f.read()) 
            case 'json':
                with open ('data.json' , 'r') as f:
                    contacts = json.load(f) 
            case 'pickle':
                with open ('data.pkl' , 'rb') as f:
                    contacts = pickle.load(f) 
            case 'yaml':
                with open ('data.yml' , 'r') as f:
                    contacts = pickle.load(f , loader=yaml.FullLoader)
            case 'csv':
                with open ('data.csv' , 'rb') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        contacts.append(row)
    except:
        print('welcome!')
  
def view(l):
    if l:
        print(' NUM ' , *[n.capitalize().center(14) for n in l[0].keys()])
        for idx,contact in enumerate(l , start=1):
            print(str(idx).center(6) , *[n.center(14) for n in contact.values()])
    else:
        print('Nothing to show !')
    
   
def exit_():
    exit()

def menu():
    while True:
        cmd = input('what do you want to do?')
        match cmd:
            case 'add' | 'a':
                add()
            case 'delete' | 'd':
                delete()
            case 'edit' | 'e':
                edit()
            case 'exit' | 'q':
                exit_()
            case 'view' | 'v':
                view(contacts)
            case 'find' | 'f':
                find(view_only=True)
            case _ :
                help_()





if __name__ == '__main__':
    load()
    menu()
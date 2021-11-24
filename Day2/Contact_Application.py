#contact application
#adding new contact
#delete contact
#edit contact
#display contacts
def add(contacts):
    details=input().split()
    if details[0] in contacts:
        print('User altready exsisted')
    else: contacts[details[0]]=details[1]
def delete(contacts):
    name=input()
    if name in contacts:
        contacts.pop(name)
    else: print('Name not found!')
def edit(contacts):
    name=input()
    if name in contacts:
        number=input()
        contacts[name]=number
    else: print('contact does not exist')
def display(contacts):
    for name in contacts:
        print(name,contacts[name])
def search(contacts):
    name=input()
    if name in contacts: print(name,contacts[name])
    else: print('contact not found')
        
contacts={}
features=['add','delete','edit','display']
print('CONTACTS')
for method in features:
    print(method)

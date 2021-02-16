import sys
	#listas de diccionario 	
clients=[
     {
      'name':'Pablo',
      'company':'Google',
      'email':'ejemplo@hotmail.com',
      'position':'tecnico1',
     
     },

     { 
      'name':'Pedrito',
      'company':'Google',
      'email':'ejemplo2@hotmail.com',
      'position':'tecnico2',

     }

]
def create_client(client):
    global clients
    if client not in clients:  
        clients.append(client)
    else:
        print('Client already is in the client\' list')

def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name}| {company} |{email}|{position}'.format(
         uid=idx,
         name=client['name'],
         company=client['company'],
         email=client['email'],
         position=client['position'],   ))

def update_client(client_name):
    global clients
    for idx, client in enumerate(clients):
        if client['name']==client_name:
           print('El usuario si existe')
           nuevo={
	         'name':input('Teclea el nuevo nombre'),
                 'company':input('Teclea la nueva compania'),
                 'email':input('Teclea el nuevo valor de email'),
                 'position':input('Teclea la nueva posioscion'),}
           client.update(nuevo) 
           continue
        else:
           continue
           print('El usuario no existe')
           

def delet_client(client_name):
     borrar=-1
     for idx, client in enumerate(clients):
        if client['name']==client_name:
           borrar=idx
     clients.pop(borrar)


def search_client(client_name):
    impresion=0
    for idx, client in enumerate(clients):
        if client['name']==client_name:
           print('el usuario si exite',client,'\n')
           break
        else :
           impresion=1;
    if impresion==1:
        print("El usuario no existe")
def _get_client_field(field_name):
    field=None
    while not field:
       field=input('What is the client{}'.format(field_name))
    return field



def _get_client_name():   
    client_name=None
    while not client_name:
       client_name= input ('Whats is name the client name: ')
       if client_name=='exit':
           client_name=None
           break
    if not client_name:
           sys.exit()   
    return client_name


def _print_welcome():
    print('Welcome to alex ventas XD')
    print('+'*50)
    print('what would you like to do today?')
    print('[C]reate client')
    print('[D]elete client ')
    print('[U]pdate client')
    print('[S]earch client')
    print('[L]ist client')

if __name__=='__main__':
    _print_welcome()
    command=input()
    command=command.upper()
    if command== 'C':
        client={
            'name':_get_client_field('name'),
            'company':_get_client_field('company'),
            'email':_get_client_field('email'),
            'position':_get_client_field('position'),
              }        
        create_client(client)
        list_clients()
    elif command== 'D':
       list_clients()
       client_name=_get_client_name()
       delet_client(client_name)
       list_clients()
   
    elif command=='U':
       client_name=_get_client_name()
       update_client(client_name)
       list_clients()
    elif command=='S':
       search_client(input("Teclea el valor del nombre a buscar  "))
    elif command=='L':
        list_clients()
    else:
        print('Invalid command')


    

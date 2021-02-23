PASSWORD='12345' #se declara una constanta



def password_required(func): #Se crea un decorador llamando a la funcion
    def wrapper(): #Se crea las caracteristicas del decorador
        password=input("Teclea una contraseña") #Se pide un valor a comparar de contraseña
        if password==PASSWORD: # Se compara la contraseña
            return func() #Se llama a la funcion  needs_password
        else: # Si el valor es false se otorga una nueva opción
            print("La contraseña es incorrecta") #Se imprime algo
    return wrapper #Se regresa a wrapper


@password_required #Se coloca un decorador aun a funcion 
def needs_password():
    print('La contraseña es correcta')

def upper(func):
    def wripper(*args, **kwargs):
        result= func(*args, **kwargs)
        return result.upper()
    return wripper
@upper
def say_my_name(name):
    return ("Hola, {}".format(name))    

if __name__== '__main__':
   print (say_my_name("Alex"))


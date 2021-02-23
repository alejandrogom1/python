




class Person:
   def __init__(self,name,age):
      self.name=name
      self.age=age



   def say_hellow(self):
      print ('Hellow, my neme is {} and I am {} years old'.format(self.name, self.age))



if __name__=='__main__':  
    person=Person('Alex','56')
    print('Edad: {}'.format(person.age))
    person.say_hellow()

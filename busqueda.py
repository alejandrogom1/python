import random





def binary_search(data, target, low, high):
    if low> high:
        return False 
    mitad=(low+high )//2
    
    if target == data[mitad]:
        return True
    elif target<data[mitad]:
        return binary_search(data, target, low, mitad-1)
    else:
        return binary_search(data, target, mitad+1, high)        


 
if __name__== '__main__':
    data=[random.randint(0,100) for i in range(10)]
    sorted_data=sorted(data)
    print(sorted_data)
    target=int(input("Cual es el valor a buscar"))
    found=binary_search(sorted_data,target,0,len(data)-1)
    print(found)

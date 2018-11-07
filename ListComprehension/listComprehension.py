if __name__ == '__main__':
    x = int(input("enter X "))
    y = int(input("enter Y "))
    z = int(input("enter Z "))
    n = int(input("enter N "))
    
    lista=[]
    lista.extend([i,j,k] for i in range(x+1) for j in range (y+1) for k in range(z+1) if (i+j+k) != n)
    print(lista)

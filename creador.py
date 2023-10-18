import random

charateres= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
cantidades = int(input("ingresa el numero de characteres tiene tu contraseña"))
contraseñas = ""
for i in range(cantidades):
    x = random.randint(0,len(caracters)-1)
    y= caracters[x]
    contraseña+=y
print("contraseña")

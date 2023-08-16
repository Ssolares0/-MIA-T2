import re
import os
import time
import random
import struct

def execute(tk):
    
    tk.pop(0)
    tk.pop(0)
    
    
    
    #Sumamos cada valor
    path = ""
    for x in range(len(tk)):
        #print(tk[x])
        path = path  +tk[x] + " "
    path_final= path.rstrip()

    with open(path_final,"r") as file:
        for line in file:
            # quitamos los espacions inecesarios
            line = line.strip()
            print("Ejecutando comando: "+ line)
                
            if line == "mkdisk":
                analyze_mkdisk(line)
            if line == "rep":
                rep(line)
            
    file.close()            

            #analyze(line)
    


def analyze_mkdisk(token_):
    #print(token_)
    """Creamos el archivo vacio"""
    with open("Salida/Hard_disk.dsk","wb") as file:
        size_kilobyte =1024
        for i in range (0,5000):
            file.write(b'\x00'*size_kilobyte)
        file.close()

    """Creamos el MBR"""      
    with open("Salida/Hard_disk.dsk","rb+") as file:
        file.seek(0,0)
        size_file = os.path.getsize("Salida/Hard_disk.dsk")
        print(size_file)
        date_file = time.ctime(os.path.getctime("Salida/Hard_disk.dsk"))
        num_random = random.randint(0,9)

        data_pack = struct.pack("i 24s 8s",size_file,date_file.encode(),str(num_random).encode('utf-8'))
        file.write(data_pack)
        
def rep(token_):
    #Vamos a abrir y leer un archivo binario
    with open("Salida/Hard_disk.dsk","rb") as file:
        file.seek(0,0)
        data = file.read(36)
        data_unpack = struct.unpack("i 24s 8s",data)
        print("Size: " +str( data_unpack[0]))
        print("Date: " + data_unpack[1].decode())
        print("Random: " + data_unpack[2].decode())
    file.close()
    

        

def analyze(comando):

    # Analizamos el comando 

    token_ = re.split(" ",comando)

    # Cadena en minuscula
    token_[0] = token_[0].lower()
    
    if token_[0] == "exec":
        #print(token_)
        execute(token_[1:])
    if token_[0] == "mkdisk":
        analyze_mkdisk(token_[1:])
        

    if token_[0] == "rep":
        rep(token_[1:])  
            
    else: 
        
        analyze(input("< "))


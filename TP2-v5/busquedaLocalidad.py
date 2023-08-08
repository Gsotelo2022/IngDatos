from pymongo import MongoClient
import sqlite3
import Menu
import obtenerProvincia
import obtenerLocalidad
from clima import coleccion_clima
import time

def buscar_localidad():
    obtenerProvincia.coleccion_provincia()
    obtenerLocalidad.coleccion_localidad()
    coleccion_clima()    
    
    #Conexion
    cliente = MongoClient('mongodb://localhost:27017')

    bd = cliente['argentina']
    coleccion = bd['clima']
    
    #encuentro
    enc=0
    cont=0

    while enc==0:  
        cont+=1
        if cont ==1:
            loc= input('\nIngrese Localidad: ')
            loc1=loc.lower().title().replace('á','a').replace('é','e').\
                replace('í','i').replace('ó','o').replace('ú','u')
        else:
            print('La localidad ingresada no se encuentra...\n')
            print('Usted volvera al menu principal!')
            time.sleep(5)            
            enc=1
            break
        if enc!=1:  
            #cargo climas
            clima = coleccion.find()

            for buscar in clima:
                if buscar['localidad'] == loc1:
                    print('Provincia: ', buscar['provincia'])
                    print('Temperatura: ', round((buscar['temperatura']-273.15),2),'º') 
                    print('Humedad: ', buscar['humedad'], '%')
                    print('_________________________________________________')        
                    enc=1
        else:
            Menu.menu()
                
    cliente.close()
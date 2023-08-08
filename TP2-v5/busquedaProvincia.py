from pymongo import MongoClient
import sqlite3
import time
import Menu
import obtenerProvincia
import obtenerLocalidad
from clima import coleccion_clima

def buscar_provincia():
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
        ####### ABRIMOS ARCHIVO
        cont+=1
        if cont ==1:
            prov = input('\nIngrese Provincia: ')
            prov1 = prov.lower().title().replace('á','a').replace('é','e').\
                replace('í','i').replace('ó','o').replace('ú','u')   
        else:
            print('La provincia ingresada no se encuentra...\n')
            print('Usted volvera al menu principal!')
            time.sleep(5)            
            enc=1              
            break
        if enc!=1:
            #cargos climas
            clima = coleccion.find()   
            for buscar in clima:
                if buscar['provincia'] == prov1:
                    print('Localidad: ', buscar['localidad'])
                    print('Temperatura: ', round((buscar['temperatura']-273.15),2),'º') 
                    print('Humedad: ', buscar['humedad'],'%')
                    print('_________________________________________________')
                    enc=1
        else:
             Menu.menu()  
             
    ###FINALIZAR ARCHIVO                           
    cliente.close()
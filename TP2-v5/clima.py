def coleccion_clima():
    import requests
    import json
    from bs4 import BeautifulSoup
    from pymongo import MongoClient
    import datetime
    import os
    #Conexion
    cliente = MongoClient('mongodb://localhost:27017')

    bd_loc = cliente['argentina']
    coleccion_loc = bd_loc['localidades']
    localidades = coleccion_loc.find() 
  
    collist = cliente.argentina.list_collection_names()
    
    if not "clima" in collist:            
        for localidad in localidades:       
            #Apertura del archivo
            archivo=open('auditoria.txt','a', encoding = 'utf-8')
            key = 'b3db4d1afb77d90c0cbe668d38d21d1f'
            url = 'http://api.openweathermap.org/data/2.5/weather?q=' + str(localidad['localidad']) + '&appid=' + key

            response = requests.get(url)
            objeto = json.loads(response.text)
            x =response.json()     

            #Capturamos error 404 
            if x["cod"] != "404": 
                y = x["main"] 
                dev = cliente.argentina.clima.insert_one({'provincia':localidad['provincia'],\
                    'localidad':localidad['localidad'],'temperatura':objeto['main']['temp'],'humedad':objeto['main']['humidity']})
                #Se guarda auditoria
                ahora=datetime.datetime.now()
                archivo.write((ahora.strftime('[%d/%m/%Y %H:%M:%M]'))+' INSERT [Provincia: {}] [Localidades: {}] [Temperatura: {}] [Humedad: {}]\n'\
                    .format(localidad['provincia'],localidad['localidad'],objeto['main']['temp'],objeto['main']['humidity']))                                                                                                                                                
    else:
        #Eliminar la collection y actualizarla 
        print('\nEl clima se esta actualizando...\n')        
        mydb= cliente['argentina']
        mycol=mydb['clima']
        mycol.drop()    
        #Se guarda auditoria
        ahora=datetime.datetime.now()        
        archivo.write((ahora.strftime('[%d/%m/%Y %H:%M:%M]'+'Eliminacion de la coleccion CLIMA')))
        coleccion_clima()

    archivo.close()  
    cliente.close()      
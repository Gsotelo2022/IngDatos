def coleccion_provincia():
    import requests
    import json
    from pymongo import MongoClient
    import datetime
    import os
    #Request
    url='https://apis.datos.gob.ar/georef/api/provincias'

    #Conexion
    cliente = MongoClient('mongodb://localhost:27017')

    #Obtener resultado de la api
    response = requests.get(url)

    #Guardar resultado en un txt
    response_json=json.loads(response.text.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u'))

    #Valida si esta o no creada la coleccion
    collist = cliente.argentina.list_collection_names()
    #Apertura del archivo
    archivo=open('auditoria.txt','a', encoding = 'utf-8')

    if not "provincias" in collist:   
        for prov in response_json['provincias']:                
            #insertar un valor    
            dev = cliente.argentina.provincias.insert_one({'Provincia':prov['nombre']})
             
            #Se guarda auditoria
            ahora=datetime.datetime.now()           
            archivo.write((ahora.strftime('[%d/%m/%Y %H:%M:%M]'))+' INSERT {} in Provincia\n'.format(prov['nombre']))
    archivo.close()
    cliente.close()
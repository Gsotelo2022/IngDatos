def coleccion_localidad():
    import requests
    import json
    from pymongo import MongoClient
    import datetime
    import os
    #Conexion
    cliente = MongoClient('mongodb://localhost:27017')
    
    bd_prov = cliente['argentina']
    coleccion_prov = bd_prov['provincias']
    provincia = coleccion_prov.find()
    
    collist = cliente.argentina.list_collection_names()
    #Apertura del archivo
    archivo=open('auditoria.txt','a', encoding = 'utf-8')

    if not "localidades" in collist:
        for prov in provincia:
            url_localidad = 'https://apis.datos.gob.ar/georef/api/municipios?provincia=' + prov['Provincia']
            response_localidad = requests.get(url_localidad)
            response_json_localidad=json.loads(response_localidad.text.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u'))
            for localidad in response_json_localidad['municipios']:
                dev = cliente.argentina.localidades.insert_one({'provincia':prov['Provincia'],'localidad':localidad['nombre']})
                #Se guarda auditoria
                ahora=datetime.datetime.now()
                archivo.write((ahora.strftime('[%d/%m/%Y %H:%M:%M]'))+' INSERT {} in Provincia - Localidades {}\n'.format(prov['Provincia'],localidad['nombre']))
    archivo.close()            
    cliente.close()
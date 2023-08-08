import busquedaProvincia
import busquedaLocalidad

def menu():
    opcion=0
    #contador
    con=0
    mensaje = 'Clima de la Argentina'
    print(mensaje)
    print('=' * len(mensaje))
    
    while opcion != 3:        
        print('Seleccione el tipo de consulta que quiere realizar:')
        print('1) Por Provincia\n2) Por Localidad\n3) Salir\n')
        opcion = int(input('Elija la opcion: '))  
       
        if opcion < 1 or opcion > 3:
            print('La opcion elegida no es correcta...\n')
        else:
            if opcion == 1:
                print('Se esta realizando la consulta...\nAguarde unos instantes...\n')
                busquedaProvincia.buscar_provincia()
            elif opcion == 2:
                print('Se esta realizando la consulta...\nAguarde unos instantes...\n')
                busquedaLocalidad.buscar_localidad()
            elif opcion == 3:
                break

def run():
    menu()

if __name__ == '__main__':
	run()
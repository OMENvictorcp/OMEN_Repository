SALIDA = 'Salir'


def guardar_lista_a_disco(lista_compra):
    nombre_fichero = input('Como quieres que se llame el fichero?')

    with open(nombre_fichero + 'txt', 'w') as mi_archivo:
        mi_archivo.write('\n'.join(lista_compra))



def preguntar_producto_usuario():
    return input('Introduce un producto [{} para salir]'.format(SALIDA))

def main():
    lista_compra = []

    input_usuario = preguntar_producto_usuario()

    while input_usuario != SALIDA:
        lista_compra.append(input_usuario)
        print('\n'.join(lista_compra))
        input_usuario = preguntar_producto_usuario()
    guardar_lista_a_disco(lista_compra)



if __name__ == '__main__':
    main()


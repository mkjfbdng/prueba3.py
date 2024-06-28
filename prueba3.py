import csv


def registrar_propiedad(correlativo, tipo_propiedad, dormitorios, banos, precio):
    with open('REGISTRO_PROPIEDADES_USADAS.csv', 'a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow([correlativo, tipo_propiedad, dormitorios, banos, precio])
def listar_propiedades():
    with open('REGISTRO_PROPIEDADES_USADAS.csv', 'r', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for registro in lector_csv:
            print(registro)
def imprimir_propiedades_por_tipo(tipo_seleccionado):
    nombre_archivo = f'PROPIEDADES_{tipo_seleccionado.upper()}.csv'
    with open('REGISTRO_PROPIEDADES_USADAS.csv', 'r', newline='') as archivo_csv, \
         open(nombre_archivo, 'w', newline='') as archivo_salida:
        lector_csv = csv.reader(archivo_csv)
        escritor_csv = csv.writer(archivo_salida)
        escritor_csv.writerow(['Correlativo', 'Tipo de Propiedad', 'Número de Dormitorios', 'Número de Baños', 'Precio'])
        
        for registro in lector_csv:
            if registro[1].lower() == tipo_seleccionado.lower():
                escritor_csv.writerow(registro)

def main():
    while True:
        print("\nMenú Principal:")
        print("1. Registrar Propiedad")
        print("2. Listar Todas las Propiedades")
        print("3. Imprimir Propiedades por Tipo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            correlativo = input("Ingrese correlativo: ")
            tipo_propiedad = input("Ingrese tipo de propiedad (1=Casa, 2=Departamento): ")
            dormitorios = input("Ingrese número de dormitorios: ")
            banos = input("Ingrese número de baños: ")
            precio = input("Ingrese precio: ")
            
            if tipo_propiedad == '1':
                tipo_propiedad = 'Casa'
            elif tipo_propiedad == '2':
                tipo_propiedad = 'Departamento'
            else:
                print("Tipo de propiedad inválido.")
                continue
            
            registrar_propiedad(correlativo, tipo_propiedad, dormitorios, banos, precio)
            print("Propiedad registrada exitosamente.")
        
        elif opcion == '2':
            print("\nListado de Propiedades Registradas:")
            listar_propiedades()
        
        elif opcion == '3':
            print("\nImprimir Propiedades por Tipo:")
            print("Seleccione el tipo de propiedad:")
            print("1. Casa")
            print("2. Departamento")
            
            tipo_seleccionado = input("Ingrese el número del tipo de propiedad: ")
            
            if tipo_seleccionado == '1':
                imprimir_propiedades_por_tipo('Casa')
                print(f"Se ha generado el archivo PROPIEDADES_CASA.csv con las propiedades tipo Casa.")
            elif tipo_seleccionado == '2':
                imprimir_propiedades_por_tipo('Departamento')
                print(f"Se ha generado el archivo PROPIEDADES_DEPARTAMENTO.csv con las propiedades tipo Departamento.")
            else:
                print("Opción inválida.")
        
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción inválida. Por favor seleccione una opción válida.")

main()

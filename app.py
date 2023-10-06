import requests
import os

def buscar_documento(nombre_documento):
    ruta_documento = os.path.join("documentos", nombre_documento)
    if os.path.isfile(ruta_documento):
        return open(ruta_documento, "rb")
    else:
        return None

def descargar_documento(nombre_documento):
    documento = buscar_documento(nombre_documento)
    if documento is not None:
        with open(nombre_documento, "wb") as archivo:
            archivo.write(documento.read())
        print("Descarga exitosa.")
    else:
        print("El documento no existe.")

def descargar_documento_desde_url(url_documento):
    respuesta = requests.get(url_documento)
    if respuesta.status_code == 200:
        with open(os.path.basename(url_documento), "wb") as archivo:
            archivo.write(respuesta.content)
        print("Descarga exitosa.")
    else:
        print("Error al descargar el documento.")

if __name__ == "__main__":
    # Opción 1: Descargar un documento desde un directorio local
    nombre_documento = input("Ingrese el nombre del documento que desea descargar: ")
    descargar_documento(nombre_documento)

with open('html.txt', "r") as archivo:
    texto = archivo.read()

texto = texto.replace("<", "&lt;")
texto = texto.replace(">", "&gt;")

with open('legiblePrismHtml.txt', "w") as nuevo_archivo:
    nuevo_archivo.write(texto)

print("Archivo procesado y guardado exitosamente.\n")
import xml.etree.ElementTree as ET
import os

#funcion puede ser mejorada para dar lists de una pero whatever

def obtener_contenido_tier(xml_file):
    # Parsear el archivo XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Lista para almacenar el contenido de los elementos TIER con TIER_ID igual a "GLOSA"
    oracion_glosa = ""
    
        # Iterar sobre todos los elementos TIER
    for tier in root.findall('.//TIER'):
        # Obtener el atributo TIER_ID
        tier_id = tier.get('TIER_ID')
        
        # Verificar si el TIER_ID es "GLOSA"
        if tier_id == "GLOSA":
            # Iterar sobre los elementos ANNOTATION_VALUE dentro del TIER
            for annotation in tier.findall('.//ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE'):
                oracion_glosa += str(annotation.text + " ")
                        
        elif tier_id == "TRADUCCION":
            for annotation in tier.findall('.//ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE'):
                oracion = str(annotation.text)
                
        elif tier_id == "Traducción":
           for annotation in tier.findall('.//ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE'):
               oracion = str(annotation.text)
               


    return oracion_glosa, oracion

# Archivo XML de ejemplo
xml_file = 'D:/Classic/upc/2024-1/TP1/Código/datasets/PUCP 305 (glosas)/5. Segundo avance (corregido)/ABRIR/ABRIR_ORACION_1.eaf'
data_directory = 'D:/Classic/upc/2024-1/TP1/Código/datasets/PUCP 305 (glosas)/5. Segundo avance (corregido)'

# Llamar a la función para obtener el contenido del TIER "GLOSA"
#contenido_glosa, oracion_es = obtener_contenido_tier(xml_file)

# Imprimir el contenido obtenido

# for dirs in os.walk(data_directory) pasa por cada dir dentro de data_directory contandose a si mismo (como el mismo es el [0] tener cuidado de usar o no el primero de la lista) 
#       not necesario para el código qeu viene debajo (el if se encarga xd)



# for file in dirs[2] pasa por cada item dentro de dirs[2] (lista de archivos dentro del dir en el que estamos) 
# if file.endswith(".eaf") and file.__contains__('ORACION') if para comprobar si la variable file es agregada a la lsita
# direccion de lectura para los fors es -> | a menos que estemos con [] en cuyo caso es lo de afuera primero
# conseguimos la ruta al archivo .eaf juntando file (que es nombre de este) + su ruta + "/" y reemplazamos el\ existente 

xml_files = [str(dirs[0] + "/" + file).replace('\\','/') for dirs in os.walk(data_directory) for file in dirs[2] if file.endswith(".eaf") and file.__contains__('ORACION')]

dañado = xml_files[269]
print(dañado)
print(obtener_contenido_tier(dañado))

#with hacer .close() por nosotros
def generar_csv():
    with  open("datasets/español.csv", "w+", encoding="utf-8") as csv_es, open("datasets/glosa.csv", "w+", encoding="utf-8") as csv_glosa: 
        for file in xml_files:
            glosa, es = obtener_contenido_tier(file) #nos da la oracion en glosa y ES(pañol)
            if file == xml_files[-1]:
                csv_glosa.write(glosa)
                csv_es.write(es)
            else:
                csv_glosa.write(glosa + '\n')
                csv_es.write(es + '\n')
        
        
            

generar_csv()        

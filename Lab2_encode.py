import hashlib
################ Abrir archivo y guardar mensaje en variable
archivo_entrada = open('mensajedeentrada.txt', 'r')
mensaje = archivo_entrada.readlines()
mensaje = mensaje[0]
print('El mensaje de entrada es:',mensaje)
hash = hashlib.sha256(mensaje.encode('utf-8')).hexdigest()
print('Hash del mensaje en SHA256 es:',hash)


################## función para hacer un rot() para un numero n
def encriptar_rot_x(texto,numero):
    texto = texto.lower()
    num_rot = numero
    abc = "abcdefghijklmnopqrstuvwxyz"
    final = ""
    finalencrypted = ''
    rotacion = abc[num_rot:] + abc[:num_rot]

    for i in range(len(texto)):
        if texto[i].isalpha():
            final = rotacion[abc.index(texto[i])]
            finalencrypted += final
        else:
            finalencrypted += texto[i]
    return(finalencrypted)



#################### Cifrado de mensaje en rot()
rot13 = encriptar_rot_x(mensaje,13)
print('Rot(13) del mensaje:',rot13)
rot8 = encriptar_rot_x(rot13,8)
print('Rot(8) del anterior mensaje:',rot8)
rot2 = encriptar_rot_x(rot8,2)
print('Rot(2) del anterior mensaje:',rot2)


################### Exportar mensaje cifrado con el hash del mensaje original

Mensaje_cifrado = open('mensajeseguro.txt','w+')
Mensaje_cifrado.write(rot2)
Mensaje_cifrado.write('\n')
Mensaje_cifrado.write(hash)
Mensaje_cifrado.close()

